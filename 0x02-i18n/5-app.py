#!/usr/bin/env python3
"""setup flask-babel"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional, Dict
from jinja2 import Environment


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """confg lang and timezone """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
env = Environment(extensions=["jinja2.ext.autoescape", "jinja2.ext.with_"])
app.config.from_object(Config)


def get_user() -> Optional[Dict]:
    """returns a user dictionary or None if the
    ID cannot be found or if login_as
    url parameter was not passed"""
    id = request.args.get("login_as", type=int)
    return users.get(id, None)


@app.before_request
def before_request() -> None:
    """find if valid user returns it in g.user"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ Use request.accept_languages to
    determine the best match with
    our supported languages"""

    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if (g.user):
        loc = g.user.get('locale')
    if loc and  loc in app.config['LANGUAGES']:
        return loc 
    loc = request.headers.get('locale', None)
    if loc in app.config['LANGUAGES']:
        return loc   
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> str:
    """return simple home page"""
    return render_template("5-index.html")


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
