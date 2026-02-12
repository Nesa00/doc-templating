from dataclasses import dataclass
from typing import Dict

@dataclass
class Defaults:
    """Default configuration for PDF/HTML generation."""
    
    # File/folder names
    templates_folder: str = r"templates"
    data_file: str = r"data.json"
    md_template: str = r"report.md"
    css_style: str = r"style.css"
    
    # Output files
    output_pdf: str = r"output.pdf"
    output_html: str = r"output.html"
    
    # HTML template
    html_base:str = """
<html>
<head>
    <link rel="stylesheet" href="{{style_path}}">
</head>
<body>
    {{html_content}}
    <script>
        print()
    </script>
</body>
</html>
"""
    # Browser paths
    paths: Dict[str, str] = None
    
    def __post_init__(self):
        """Initialize paths if not provided."""
        if self.paths is None:
            self.paths = {
                "edge": self._get_edge_path(),
                "chrome": self._get_chrome_path(),
                "brave": self._get_brave_path(),
            }
    
    @staticmethod
    def _get_edge_path() -> str:
        """Get Edge browser path."""
        return r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    
    @staticmethod
    def _get_chrome_path() -> str:
        """Get Chrome browser path."""
        return r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    
    @staticmethod
    def _get_brave_path() -> str:
        """Get Brave browser path."""
        return r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

defaults = Defaults()