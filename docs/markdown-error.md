# Markdown to PDF Generation Error: Pandoc Not Recognized

## Error Message

```
'pandoc' is not recognized as an internal or external command,
operable program or batch file.
```

## Cause
This error occurs because Pandoc is not installed or not added to your system PATH.

## Solution
1. **Install Pandoc:**
   - Download the installer from the official site: [https://pandoc.org/installing.html](https://pandoc.org/installing.html)
   - Run the installer and follow the instructions.
2. **Add Pandoc to PATH:**
   - The installer usually adds Pandoc to your PATH automatically.
   - If not, manually add the Pandoc installation directory (e.g., `C:\Program Files\Pandoc`) to your system PATH.
3. **Restart your terminal or VS Code.**
4. **Test:**
   - Open a new terminal and run:
     ```
     pandoc --version
     ```
   - You should see version information if installed correctly.

---

For more help, see the [Pandoc documentation](https://pandoc.org/installing.html).