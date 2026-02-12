__default_brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
__default_chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe" 
__default_edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

paths = {
    "edge" : __default_edge_path,
    "chrome" : __default_chrome_path,
    "brave" : __default_brave_path
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