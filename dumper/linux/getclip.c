/*
 * getclip.exe <file>: writes the Windows clipboard text (CF_UNICODETEXT) as UTF-8 to <file>.
 * The dumper's stand-in for `powershell Get-Clipboard` when the Windows client runs under Wine
 * (panorama_generate_layout_xsd puts the layout XSD on the clipboard). Exit code 1: no text.
 *
 * x86_64-w64-mingw32-gcc -O2 -o getclip.exe getclip.c
 */
#include <stdio.h>
#include <windows.h>

int main(int argc, char **argv) {
  if (argc != 2) {
    fprintf(stderr, "usage: getclip.exe <file>\n");
    return 2;
  }
  for (int attempt = 0; attempt < 50 && !OpenClipboard(NULL); attempt++) Sleep(100);
  HANDLE data = GetClipboardData(CF_UNICODETEXT);
  const wchar_t *text = data ? (const wchar_t *)GlobalLock(data) : NULL;
  if (!text) {
    CloseClipboard();
    fprintf(stderr, "getclip: no text on the clipboard\n");
    return 1;
  }
  int size = WideCharToMultiByte(CP_UTF8, 0, text, -1, NULL, 0, NULL, NULL);
  char *utf8 = (char *)HeapAlloc(GetProcessHeap(), 0, size);
  WideCharToMultiByte(CP_UTF8, 0, text, -1, utf8, size, NULL, NULL);
  GlobalUnlock(data);
  CloseClipboard();

  FILE *out = fopen(argv[1], "wb");
  if (!out) {
    fprintf(stderr, "getclip: cannot write %s\n", argv[1]);
    return 2;
  }
  fwrite(utf8, 1, size - 1, out);
  fclose(out);
  return 0;
}
