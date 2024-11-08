#!/usr/bin/env python3
"""setup flask"""

from flask import Flask, render_template
from jinja2 import Environment

app = Flask(__name__)

env = Environment(extensions=["jinja2.ext.autoescape", "jinja2.ext.with_"])

@app.route('/')
def home():
    """return simple home page"""
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run()
