/*
 * Linux replacement for the vConsole message stream: follows the -condebug console.log of the
 * running client and turns it back into console messages.
 *
 * console.log prefixes the first line of every message with "MM/DD HH:MM:SS " and, for any channel
 * other than General, "[Channel] ". Continuation lines of a multi-line message carry no prefix.
 * vConsole delivers the bare message text, so both prefixes are stripped from message-start lines
 * only, and continuation lines are appended verbatim.
 */
import * as fs from 'fs';

const MESSAGE_START = /^\d\d\/\d\d \d\d:\d\d:\d\d (.*)$/s;
const CHANNEL_TAG = /^\[([^\]\n]{1,48})\] /;

// Spam from the software-rendered headless client (1-3 fps, no Steam/GC) that the Windows dump
// never contains. Dropped so it cannot land inside a section.
const NOISE: { channel?: string; text: RegExp }[] = [
  { text: /^Excessive frame time of / },
  { text: /^CSwapChainBase::QueuePresentAndWait\(\) looped / },
  { channel: 'GCClient', text: /^Trying to send message type / },
  { channel: 'InputSystem', text: /^Processing SDL events took / },
];

export type LogMessageCallback = (channel: string | undefined, message: string) => void;

export interface ConsoleLogFollower {
  stop(): void;
}

/**
 * Follows `file` from byte `startOffset`, calling `cb` once per complete message. A message is
 * complete when the next one starts, or when the log has been quiet for `flushAfterMs`.
 */
export function followConsoleLog(
  file: string,
  startOffset: number,
  cb: LogMessageCallback,
  { pollMs = 100, flushAfterMs = 400 } = {},
): ConsoleLogFollower {
  let offset = startOffset;
  let partialLine = '';
  let pending: { channel?: string; text: string } | null = null;
  let lastData = Date.now();
  let stopped = false;
  let fd: number | null = null;
  let openInode = -1;

  const emit = () => {
    if (!pending) return;
    const { channel, text } = pending;
    pending = null;
    if (NOISE.some((n) => (!n.channel || n.channel === channel) && n.text.test(text))) return;
    cb(channel, text);
  };

  const handleLine = (line: string) => {
    const start = MESSAGE_START.exec(line);
    if (start) {
      emit();
      let text = start[1];
      let channel: string | undefined;
      const tag = CHANNEL_TAG.exec(text);
      if (tag) {
        channel = tag[1];
        text = text.slice(tag[0].length);
      }
      pending = { channel, text };
    } else if (pending) {
      pending.text += line;
    }
  };

  // Returns whether anything new was read from the open file.
  const readNew = (): boolean => {
    const size = fs.fstatSync(fd!).size;
    if (size < offset) offset = 0; // truncated
    if (size <= offset) return false;
    const buffer = Buffer.alloc(size - offset);
    const read = fs.readSync(fd!, buffer, 0, buffer.length, offset);
    offset += read;
    const lines = (partialLine + buffer.toString('utf8', 0, read)).split(/(?<=\n)/);
    partialLine = lines[lines.length - 1].endsWith('\n') ? '' : lines.pop()!;
    for (const line of lines) handleLine(line);
    return read > 0;
  };

  const poll = () => {
    if (stopped) return;
    try {
      // Dota deletes and recreates console.log at startup: follow the path, not the first inode.
      const inode = fs.statSync(file).ino;
      if (fd !== null && inode !== openInode) {
        readNew();
        fs.closeSync(fd);
        fd = null;
      }
      if (fd === null) {
        fd = fs.openSync(file, 'r');
        offset = openInode === -1 ? startOffset : 0;
        openInode = inode;
      }
      if (readNew()) {
        lastData = Date.now();
      } else if (Date.now() - lastData > flushAfterMs) {
        if (partialLine) {
          handleLine(partialLine);
          partialLine = '';
        }
        emit();
      }
    } catch (err: any) {
      if (err.code !== 'ENOENT') throw err;
    }
    timer = setTimeout(poll, pollMs);
  };

  let timer = setTimeout(poll, 0);
  return {
    stop() {
      stopped = true;
      clearTimeout(timer);
      if (fd !== null) fs.closeSync(fd);
    },
  };
}

/** Converts a whole console.log (or a slice of one) into messages; used by the tests. */
export function parseConsoleLog(text: string): { channel?: string; text: string }[] {
  const messages: { channel?: string; text: string }[] = [];
  for (const line of text.split(/(?<=\n)/)) {
    const start = MESSAGE_START.exec(line);
    if (start) {
      let body = start[1];
      let channel: string | undefined;
      const tag = CHANNEL_TAG.exec(body);
      if (tag) {
        channel = tag[1];
        body = body.slice(tag[0].length);
      }
      messages.push({ channel, text: body });
    } else if (messages.length > 0) {
      messages[messages.length - 1].text += line;
    }
  }
  return messages.filter(
    (m) => !NOISE.some((n) => (!n.channel || n.channel === m.channel) && n.text.test(m.text)),
  );
}
