import * as net from 'net';

export async function connect(port: number): Promise<net.Socket> {
const MAX_TRIES = 10;
const RETRY_DELAY = 1000; //ms
const BACKOFF_MULT = 1.5;
  let tries = 0;

  return new Promise((resolve, reject) => {
    const socket = new net.Socket();
    socket.on('connect', () => {
      resolve(socket);
    });
    socket.on('error', (err) => {
      if (++tries < MAX_TRIES) {
        const delay = Math.round(RETRY_DELAY * Math.pow(BACKOFF_MULT, tries - 1));
        console.log(`vConsole connect attempt ${tries} failed, retrying in ${delay}ms...`);
        setTimeout(() => {
          socket.connect({ host: '127.0.0.1', port });
        }, delay);
      } else {
        console.error('vConsole connect failed after max retries:', err);
        reject(err);
      }
    });

    socket.connect({ host: '127.0.0.1', port });
  });
}

const cmndTypeBytes = 'CMND'.split('').map((c) => c.charCodeAt(0));

export async function execute(socket: net.Socket, command: string): Promise<void> {
  return new Promise((resolve, reject) => {
    const version = [0x00, 0xd4, 0x00, 0x00];
    const length = command.length + 12 + 1;
    const byteBuffer = new Uint8Array([
      ...cmndTypeBytes,
      ...version,
      ...encodeUint16(length),
      ...encodeUint16(0),
    ]);

    var headerBuffer = Buffer.from(byteBuffer, 0, 12);
    var commandBuffer = Buffer.from(command + '\0', 'ascii');

    const bufferToSend = Buffer.concat([headerBuffer, commandBuffer], length);

    socket.write(bufferToSend, (err) => {
      if (err) {
        reject(err);
      } else {
        resolve();
      }
    });
  });
}

export type MessageCallback = (type: string, channel: number | undefined, message: string) => void;
export function onMessage(socket: net.Socket, cb: MessageCallback): void {
  // The vConsole protocol is a continuous TCP byte stream of length-prefixed
  // packets. A single 'data' event is NOT guaranteed to contain whole packets:
  // for a multi-megabyte dump, packets are routinely split across several
  // events. We therefore accumulate bytes and only decode a packet once all of
  // it has arrived, keeping any partial tail for the next event. (The previous
  // implementation parsed each 'data' event from offset 0, which desynced on a
  // split packet and could read a zero length → infinite loop that blocked the
  // event loop, stalled the socket, and froze Dota.)
  let acc: Buffer = Buffer.alloc(0);

  socket.on('data', (buffer) => {
    acc = acc.length === 0 ? buffer : Buffer.concat([acc, buffer]);

    let offset = 0;
    while (acc.length - offset >= 12) {
      const length = (acc[offset + 8] << 8) + acc[offset + 9];

      // A valid packet is at least its 12-byte header. A smaller length means
      // we are not on a real packet boundary; skip one byte to try to resync
      // instead of spinning forever on a zero/garbage length.
      if (length < 12) {
        offset += 1;
        continue;
      }

      // The full packet has not arrived yet — wait for the next data event.
      if (acc.length - offset < length) break;

      const type = acc.toString('utf8', offset, offset + 4);
      if (type === 'PRNT') {
        const channelId =
          (acc[offset + 12] << 24) +
          (acc[offset + 13] << 16) +
          (acc[offset + 14] << 8) +
          acc[offset + 15];
        const textStart = offset + 40;
        const textEnd = offset + length - 1; // drop the trailing null terminator
        const msg = textEnd > textStart ? acc.toString('utf8', textStart, textEnd) : '';
        cb(type, channelId, msg);
      }

      offset += length;
    }

    // Retain the unparsed tail (a partial packet) for the next data event.
    acc = offset >= acc.length ? Buffer.alloc(0) : acc.subarray(offset);
  });
}

export async function disconnect(socket: net.Socket): Promise<void> {
  return new Promise((resolve) => {
    socket.on('close', () => {
      resolve();
    });
    socket.destroy();
  });
}

function encodeUint16(v: number): number[] {
  return [(v >> 8) % 256, v % 256];
}
