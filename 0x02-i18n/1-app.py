#!/usr/bin/env python3
"""setup flask-babel"""

from flask import Flask, render_template
from flask_babel import Babel
from jinja2 import Environment

app = Flask(__name__)
babel = Babel(app)
env = Environment(extensions=["jinja2.ext.autoescape", "jinja2.ext.with_"])

class Config:
    """confg lang and timezone """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def home():
    """return simple home page"""
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run()
