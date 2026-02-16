import winreg
import webbrowser
from templating.constants import defaults
from typing import Literal
import os
import logging
import json

from collections import ChainMap

logger = logging.getLogger(__name__)

def get_default_browser_windows() -> str:
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice"
        ) as key:
            prog_id, _ = winreg.QueryValueEx(key, "ProgId")
            logger.debug(f"Default browser ProgId: {prog_id}")
            return prog_id
    except OSError as e:
        logger.error(f"Failed to read default browser from registry: {e}")
        raise


def open_in_browser(browser: str, browser_path: str, file_path: str) -> None:
    try:
        # Verify files exist
        if not os.path.isfile(browser_path):
            raise FileNotFoundError(f"Browser executable not found: {browser_path}")
        
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"HTML file not found: {file_path}")
        
        # Register browser with webbrowser module
        webbrowser.register(
            browser,
            None,
            webbrowser.BackgroundBrowser(browser_path)
        )
        logger.debug(f"Registered {browser} browser: {browser_path}")
        
        # Open file in browser
        file_url = 'file://' + os.path.abspath(file_path)
        webbrowser.get(browser).open(file_url)
        logger.info(f"Opened {file_path} in {browser}")
    except FileNotFoundError as e:
        logger.error(f"File not found when opening browser: {e}")
        raise
    except Exception as e:
        logger.error(f"Error opening browser: {e}", exc_info=True)
        raise


def browser_selection(
    file_path: str,
    browser: Literal["edge", "chrome", "brave", "default"] = "default"
) -> None:
    """Open HTML file in specified web browser.
    
    Opens the given HTML file in the specified browser. If browser is
    "default", detects and uses the system default browser.
    
    Supported browsers on Windows:
    - "edge": Microsoft Edge
    - "chrome": Google Chrome
    - "brave": Brave Browser
    - "default": System default browser (auto-detected)
    
    Args:
        file_path: Path to HTML file to open.
        browser: Browser to use. One of: "edge", "chrome", "brave", "default".
                Defaults to "default".
    
    Raises:
        FileNotFoundError: If file_path doesn't exist.
        ValueError: If browser is not one of the supported browsers.
        RuntimeError: If browser="default" and no supported default browser found.
    
    Examples:
        >>> browser_selection("report.html", "chrome")
        >>> browser_selection("report.html", "default")
    """
    # Validate file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Validate browser choice
    supported_browsers = list(defaults.paths.keys())
    if browser not in supported_browsers and browser != "default":
        raise ValueError(
            f"Browser '{browser}' not supported. "
            f"Choose from: {', '.join(supported_browsers)} or 'default'"
        )
    
    # Detect default browser if needed
    if browser == "default":
        browser = _detect_default_browser()
        logger.debug(f"Auto-detected default browser: {browser}")
    
    open_in_browser(browser, defaults.paths[browser], file_path)


def _detect_default_browser() -> str:
    """Detect system default browser from Windows registry.
    
    Queries the Windows registry to find the default browser and matches
    it against supported browsers (Chrome, Edge, Brave).
    
    Returns:
        str: Browser name: "edge", "chrome", or "brave".
    
    Raises:
        RuntimeError: If default browser is not one of the supported browsers.
    
    Note:
        This is a private helper function. Use browser_selection() with
        browser="default" instead.
    
    Examples:
        >>> browser = _detect_default_browser()
        >>> print(browser)
        'chrome'
    """
    try:
        default_browser = get_default_browser_windows()
        
        # Check if default browser matches any supported browser
        for browser_name in defaults.paths.keys():
            if browser_name in default_browser.lower():
                logger.info(f"Detected default browser: {browser_name}")
                return browser_name
    except Exception as e:
        logger.warning(f"Error reading default browser from registry: {e}")
    
    # No supported default browser found
    supported = ', '.join(defaults.paths.keys())
    raise RuntimeError(
        f"Default browser not supported. "
        f"Please specify one of: {supported}"
    )

def load_json(file_path: str) -> dict:
    """Load JSON data from a file.
    
    Args:
        file_path: Path to the JSON file to load.
    
    Returns:
        dict: Parsed JSON data.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in {file_path}: {e.msg}", e.doc, e.pos)
    return data

def load_data(*file_paths: str) -> dict:
    """Load and merge multiple JSON data files into a single dictionary.
    
    Args:
        *file_paths: Variable number of file paths to JSON files.
    
    Returns:
        dict: Merged dictionary containing data from all JSON files.
    
    Raises:
        FileNotFoundError: If any of the files do not exist.
        json.JSONDecodeError: If any of the files contain invalid JSON.
    """
    data_dicts = []
    for file_path in file_paths:
        data = load_json(file_path)
        data_dicts.append(data)
    return dict(ChainMap(*data_dicts))