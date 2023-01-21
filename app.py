#!/usr/bin/env python3

from flask import Flask, render_template
app = Flask(__name__)

hello = "Hey World!"


@app.route('/')
def home():
    return render_template('index.html', hello = hello)
if __name__ == '__main__':
    app.run()
    #app.run(host='0.0.0.0',port=5000)
