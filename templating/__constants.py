default_brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
default_chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe" 
default_edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

paths = {
    "edge" : default_edge_path,
    "chrome" : default_chrome_path,
    "brave" : default_brave_path
}

html_base = """
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