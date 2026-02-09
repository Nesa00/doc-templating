# HTML to PDF Generation Error: WeasyPrint/GTK Missing Libraries

## Error Message Example

```
OSError: cannot load library 'libgobject-2.0-0': error 0x7e.  Additionally, ctypes.util.find_library() did not manage to locate a library called 'libgobject-2.0-0'
```

## Cause
This error occurs because WeasyPrint requires system libraries (GTK, Cairo, Pango, etc.) that are not installed by default on Windows.

## Solution
1. **Download and install the GTK 3+ runtime for Windows:**
   - [GTK for Windows Runtime Environment Installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)

2. **Add GTK to your system PATH:**
   - After installation, add the GTK `bin` directory (e.g., `C:\Program Files\GTK3-Runtime Win64\bin`) to your PATH environment variable.
3. **Restart your terminal or VS Code.**
4. **Test:**
   - Try running your WeasyPrint script again.

---

For more details, see the [WeasyPrint installation documentation](https://weasyprint.readthedocs.io/en/latest/install.html#windows).
