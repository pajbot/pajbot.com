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

from pajbot.managers import RedisManager

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

RedisManager.init()

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
            website='https://imaqtpie.pajbot.com',
            bot='wowsobot',
            streamer=('imaqtpie', 'imaqtpie'),
            ),
        TwitchBot(
            website='https://paj.pajlada.se',
            bot='pajbot',
            streamer=('pajlada', 'pajlada'),
            ),
        TwitchBot(
            website='https://nymn.pajbot.com',
            bot='botnextdoor',
            streamer=('nymn_hs', 'NymN'),
            ),
        TwitchBot(
            website='https://amaz.pajbot.com',
            bot='ScamazBot',
            streamer=('amazhs', 'Amaz'),
            ),
        TwitchBot(
            website='https://anniefuchsia.gigglearrows.com',
            bot='Annies_Bot',
            streamer=('anniefuchsia', 'AnnieFuchsia'),
            ),
        TwitchBot(
            website='https://eloise.pajbot.com',
            bot='Niconicobot',
            streamer=('eloise_ailv', 'Eloise'),
            ),
        TwitchBot(
            website='https://trans.pajbot.com',
            bot='misoobot',
            streamer=('transcendence9', 'Transcendence9'),
            ),
        TwitchBot(
            website='https://tyggbar.pajbot.com',
            bot='tyggbot',
            streamer=('tyggbar', 'Tyggbar'),
            ),
        TwitchBot(
            website='https://nani.pajbot.com',
            bot='reipbot',
            streamer=('naniheichou', 'NaniHeichou'),
            ),
        TwitchBot(
            website='https://amaliuz.gigglearrows.com',
            bot='ProxyMyBot',
            streamer=('amaliuz', 'Amaliuz'),
            ),
        TwitchBot(
            website='https://linneafly.gigglearrows.com',
            bot='Linneasbot',
            streamer=('linneafly', 'Linneafly'),
            ),
        TwitchBot(
            website='https://snooki.pajbot.com',
            bot='Snookibot',
            streamer=('snookipoof', 'SnookiPoof'),
            ),
        TwitchBot(
            website='http://dyrus.pajlada.se',
            bot='BotSeventeen',
            streamer=('tsm_dyrus', 'Dyrus'),
            ),
        TwitchBot(
            website='https://jax.pajbot.com',
            bot='Boterie',
            streamer=('jaxerie', 'Jaxerie'),
            ),
        TwitchBot(
            website='https://reckful.pajbot.com',
            bot='exDeeBot',
            streamer=('reckful', 'Reckful'),
            ),
        TwitchBot(
            website='https://nanonoko.pajbot.com',
            bot='NanoNoBot',
            streamer=('nanonoko', 'Nanonoko'),
            ),
        TwitchBot(
            website='https://debound.pajbot.com',
            bot='PepsimaxBot',
            streamer=('debound', 'Debound'),
            ),
        TwitchBot(
            website='https://raz.pajbot.com',
            bot='Bot_Raz',
            streamer=('raz', 'Raz'),
            ),
        TwitchBot(
            website='https://akawonder.pajbot.com',
            bot='akawonderbot',
            streamer=('akawonder', 'akawonder'),
            ),
        TwitchBot(
            website='https://taruli.pajbot.com',
            bot='CougarBot',
            streamer=('tarulihs', 'TaruliHS'),
            ),
        ]

@app.route('/')
def home():
    redis = RedisManager.get()
    values = redis.hgetall('stream_data')
    for x in bots:
        x.online = values.get('{streamer}:online'.format(streamer=x.streamer[0])) == 'True'
        try:
            x.viewers = int(values.get('{streamer}:viewers'.format(streamer=x.streamer[0])))
        except:
            x.viewers = -1
        x.viewers_str = millify(x.viewers)
        x.game = values.get('{streamer}:game'.format(streamer=x.streamer[0]))
    bots.sort(key=
            lambda x: (x.online,
                x.viewers,
                x.bot), reverse=True,
            )
    return render_template('home.html',
            bots=bots,
            values=values)

millnames = ['', 'k', 'm']
import math
def millify(n):
    n = float(n)
    millidx = max(0, min(len(millnames)-1,
                     int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    if millidx > 0:
        num = '{:.1f}'.format(n / 10**(3 * millidx)).rstrip('0').rstrip('.')
        return '{}{}'.format(num, millnames[millidx])
    else:
        return '{:.0f}'.format(n / 10**(3 * millidx))

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
