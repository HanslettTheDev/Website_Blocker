import os
import sys
from dataclasses import dataclass
import pathlib

from flask import Flask, render_template

import webview
from src.api import API
from src.utils import text_file

if getattr(sys, "frozen", False):
    MAIN_DIR = pathlib.Path(os.path.dirname(sys.executable))
elif __file__:
    MAIN_DIR = pathlib.Path(os.path.dirname(__file__))

app = Flask(__name__, static_folder=str(MAIN_DIR / 'assets'), template_folder=str(MAIN_DIR / 'templates'))

@app.route('/')
def home():
    with open(text_file, 'r') as file:
        global websites
        websites = file.readlines()
    return render_template('index.html', context={"name": "Web Blocker"}, websites=websites)



if __name__ == "__main__":
    js_api = API()
    window = webview.create_window("Web Blocker", app, js_api=js_api, width=1200)
    webview.start(debug=True)