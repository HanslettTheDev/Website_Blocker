import json
import os
from functools import wraps
from datetime import datetime as dt
import sys 

from flask import Flask, render_template, jsonify, request, url_for
import webview

gui_dir = os.path.join(os.path.dirname(__file__), '..', 'assets') # parent directory of the server.py

if not os.path.exists(gui_dir):
    gui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets') # if the gui_dir link is broken, look for the absolute reference to the assets folder to load the frontend

server = Flask(__name__, static_folder=gui_dir, template_folder=gui_dir)
server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

# wait for the response from the json and verify the token
# cache decorator

host_temp = "hosts"
redirect = "127.0.0.1"

def verify_token(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        data = json.loads(request.data)
        print(data,file=sys.stderr)
        token = data.get('token')
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
    with open(url_link_name, "r") as f:
        global web_url
        web_url = f.readlines()

    if request.method == 'POST':
        if request.form.get('add'): 
            url = request.form['url']
            print(url,file=sys.stderr)
            with open(url_link_name, 'a') as file:
                file.write(url)
                file.write("\n")
    
    with open(url_link_name, 'r') as file:
        global links
        links = file.readlines()
    
    if request.method == 'POST':
        if request.form.get('run'):
            while True:
                with open(host_temp, "r+") as file:
                    hosts_content = file.read()
                    for low in links:
                        if low in hosts_content:
                            pass
                        else:
                            file.write(redirect + " " + low + "\n")
        elif request.form.get('stop'):
            while True:
                with open(host_temp, 'r+') as file:
                    hosts_content = file.readlines()
                    file.seek(0)
                    for hc in hosts_content:
                        if not any(website in hc for website in links):
                            file.write(hc)
                    file.truncate()
    
    return render_template('index.html', token=webview.token, url=links)