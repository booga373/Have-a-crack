#!/usr/bin/env python3
"""Build Have a Crack.

Edit src/app.html (the whole app: markup, styles, script), then run:
    python3 build.py
It writes index.html (the live site) and dist/preview.html (the same page without
<html>/<head>, used for the Claude preview). Never edit index.html by hand.
"""
import base64, pathlib, subprocess, sys
root = pathlib.Path(__file__).parent
src = (root / "src/app.html").read_text()
css = (root / "src/leaflet.css").read_text()
icon = "data:image/jpeg;base64," + base64.b64encode((root / "src/icon.jpg").read_bytes()).decode()
import time
body = src.replace("/*LEAFLET_CSS*/", css).replace("ICON_DATA", icon).replace('const BUILD="BUILD_ID"', 'const BUILD="' + time.strftime("%Y%m%d%H%M%S") + '"')
head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Have a Crack">
<link rel="apple-touch-icon" href="{icon}">
<link rel="icon" href="{icon}">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0;font:14px system-ui,sans-serif}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
"""
(root / "index.html").write_text(head + body + "\n</body>\n</html>\n")
(root / "dist").mkdir(exist_ok=True)
(root / "dist/preview.html").write_text(body)
# syntax check the app script
import re
m = re.search(r"<script>\n([\s\S]*?)</script>", body)
r = subprocess.run(["node", "-e", "new Function(require('fs').readFileSync(0,'utf8'))"], input=m.group(1), text=True, capture_output=True)
if r.returncode:
    print("SCRIPT ERROR:\n" + r.stderr); sys.exit(1)
print("Built index.html and dist/preview.html — script OK")
