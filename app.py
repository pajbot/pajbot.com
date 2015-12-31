#!/usr/bin/env python3

import sys
import argparse
import os
import configparser
import json
import math
import logging
import subprocess
import datetime
from functools import wraps, update_wrapper

from flask import Flask
from flask import request
from flask import render_template
from flask import Markup
from flask import redirect
from flask import url_for
from flask import session
from flask import jsonify
from flask import make_response
from flask.ext.assets import Environment, Bundle

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

app = Flask(__name__)
app._static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
assets = Environment(app)
# assets.url_expire = True

css = Bundle('dist/semantic.min.css', 'css/main.min.css', output='dist/bundle.%(version)s.css')
assets.register('css_all', css)

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return update_wrapper(no_cache, view)

class TwitchBot:
    def __init__(self, **options):
        self.__dict__ = options

bots = [
        TwitchBot(
            website='https://forsen.tv',
            bot='Snusbot',
            streamer=('forsenlol', 'Forsen'),
            ),
        TwitchBot(
            website='https://imaqtpie.pajlada.se',
            bot='wowsobot',
            streamer=('imaqtpie', 'imaqtpie'),
            ),
        TwitchBot(
            website='https://paj.pajlada.se',
            bot='pajbot',
            streamer=('pajlada', 'pajlada'),
            ),
        TwitchBot(
            website='https://nymn.pajlada.se',
            bot='botnextdoor',
            streamer=('nymn_hs', 'NymN'),
            ),
        TwitchBot(
            website='http://amaz.pajlada.se',
            bot='ScamazBot',
            streamer=('amazhs', 'Amaz'),
            ),
        TwitchBot(
            website='http://eloise.pajlada.se',
            bot='Niconicobot',
            streamer=('eloise_ailv', 'Eloise'),
            ),
        TwitchBot(
            website='http://trans.pajlada.se',
            bot='misoobot',
            streamer=('transcendence9', 'Transcendence9'),
            ),
        TwitchBot(
            website='https://tyggbar.pajlada.se',
            bot='tyggbot',
            streamer=('tyggbar', 'Tyggbar'),
            ),
        TwitchBot(
            website='https://nani.pajlada.se',
            bot='reipbot',
            streamer=('naniheichou', 'NaniHeichou'),
            ),
        ]

@app.route('/')
def home():
    return render_template('home.html',
            bots=bots)

@app.template_filter('remove_protocol')
def remove_protocol(url):
    return url.replace('http://', '').replace('https://', '')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_errors(e):
    return render_template('errors/500.html'), 500

@app.errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html'), 403

@app.errorhandler(Exception)
def all_exception_handler(error):
    log.exception('Unhandled exception')
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run()
