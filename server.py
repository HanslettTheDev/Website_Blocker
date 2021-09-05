import json
import os
import webbrowser
from functools import wraps

from flask import Flask, render_template, jsonify, request, url_for
import webview

gui_dir = os.path.join(os.path.dirname(__file__), '..', 'assets') # parent directory of the server.py

if not os.path.exists(gui_dir):
    gui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets') # if the gui_dir link is broken, look for the absolute reference to the assets folder to load the frontend

server = Flask(__name__, static_folder=gui_dir, template_folder=gui_dir)
server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

# wait for the response from the json and verify the token
# cache decorator
def verify_token(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        data = json.loads(request.data)
        print(data)
        token = data.get('token')
        print(token)
        if token == webview.token:
            return function(*args, **kwargs)
        else:
            raise Exception('Authentication error! Connection was lost')

    return wrapper


@server.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

@server.route('/', methods=["GET", "POST"])
def home():
    url_link_name = "site.txt"

    if request.method == 'POST':
        url = request.form['url']
        with open(url_link_name, 'a') as file:
            file.write(url + "\n")
    with open(url_link_name, "r") as f:
        global web_url
        web_url = f.readlines()
    
    return render_template('index.html', token=webview.token, url=web_url)

def run_blocker():
    pass

def stop_blocker():
    pass