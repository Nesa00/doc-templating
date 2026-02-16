from dataclasses import dataclass

@dataclass
class Defaults:
    """Default configuration for PDF/HTML generation."""
    templates_folder = "template"
    base_html = "main.html"
    output_pdf = "output.pdf"
    output_html = "output.html"
    paths = {
        "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    }
    
defaults = Defaults()