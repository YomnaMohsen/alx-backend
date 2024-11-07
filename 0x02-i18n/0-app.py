#!/usr/bin/python3
"""setup flask"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """return simple home page"""
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run()
