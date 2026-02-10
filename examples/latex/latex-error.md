# LaTeX PDF Generation Error: 'pdflatex' Not Recognized

## Error Message

```
'pdflatex' is not recognized as an internal or external command,
operable program or batch file.
```

## Cause
This error occurs because the LaTeX compiler (`pdflatex`) is not installed or not added to your system PATH.

## Solution
1. **Install a LaTeX distribution:**
   - [MiKTeX](https://miktex.org/download) (recommended for Windows)
   - [TeX Live](https://www.tug.org/texlive/acquire-netinstall.html)
2. **Add LaTeX to PATH:**
   - During installation, ensure the option to add LaTeX binaries to your PATH is selected.
   - If not, manually add the path (e.g., `C:\Program Files\MiKTeX\miktex\bin\x64`) to your system PATH.
3. **Restart your terminal or VS Code.**
4. **Test:**
   - Open a new terminal and run:
     ```
     pdflatex --version
     ```
   - You should see version information if installed correctly.

---

If you need more help, see the official documentation for your LaTeX distribution.