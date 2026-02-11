from templating import Generator

# Generator().pdf_gen()
# Generator().html_gen()


# gen = Generator(auto_open=True)

# gen.pdf_gen()
# # gen.html_gen()

import winreg

def get_default_browser_windows():
    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice"
    ) as key:
        prog_id, _ = winreg.QueryValueEx(key, "ProgId")
        return prog_id

print(get_default_browser_windows())
