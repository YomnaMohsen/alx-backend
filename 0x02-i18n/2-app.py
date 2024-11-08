#!/usr/bin/env python3
"""setup flask-babel"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """ Use request.accept_languages to
    determine the best match with
    our supported languages"""
    
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """return simple home page"""
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run()
