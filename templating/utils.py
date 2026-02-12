import winreg
import webbrowser
from templating.__constants import paths
from typing import Literal
import os

def get_default_browser_windows() -> str:
    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice"
    ) as key:
        prog_id, _ = winreg.QueryValueEx(key, "ProgId")
        return prog_id

def open_in_browser(browser: str, browser_path: str, file_path: str) -> None:
    webbrowser.register(browser, None, webbrowser.BackgroundBrowser(browser_path))
    webbrowser.get(browser).open('file://' + os.path.abspath(file_path))

def browser_selection(file_path, browser: Literal["edge", "chrome", "brave", "default"] = "default") -> None:
    if browser not in paths:
        raise ValueError(f"Unsupported browser: {browser}. Supported browsers are: {', '.join(paths.keys())} and 'default'.")
    if browser == "default":
        default_browser = get_default_browser_windows()
        for b in paths.keys():
            if b in default_browser.lower():
                browser = b
                break
    open_in_browser(browser, paths[browser], file_path)
