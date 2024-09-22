from flask import Flask, request, send_file, render_template, redirect
from pathlib import Path

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}
# Example code

app = Flask(__name__, template_folder="./templates")

@app.get('/')
def about():
    return render_template("index.html")

@app.get("/manifest.json/")
def manifest():
    return send_file("./manifest.json")

@app.get("/icons/<icon>/")
def get_icon(icon):
    if (path := Path("./icons") / icon).resolve().parent != Path("./icons").resolve():
        return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return send_file(path)