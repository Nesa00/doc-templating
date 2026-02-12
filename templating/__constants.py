class defaults:
    templates_folder:str = r"templates"
    data_file:str = r"data.json"
    md_template:str = r"report.md"
    css_style:str = r"style.css"
    html_file:str = r"base.html"
    output_pdf:str = r"output.pdf"
    output_html:str = r"output.html"
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
    __default_brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    __default_chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe" 
    __default_edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    paths = {
        "edge" : __default_edge_path,
        "chrome" : __default_chrome_path,
        "brave" : __default_brave_path
    }
