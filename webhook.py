from os import environ
from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/deployed', methods=['POST'])
def hook():
    form = {x: request.form[x] for x in request.form}
    to_send = {
        'color': 'purple',
        'message': "{user} deployed <a href='{url}'>{app}</a> ({head}):<br>{git_log}".format(**form),
        'message_format': 'html'
    }
    url = "https://api.hipchat.com/v2/room/{HIPCHAT_ROOM}/notification?auth_token={HIPCHAT_TOKEN}".format(**environ)
    requests.post(url, json.dumps(to_send), headers={'Content-Type': 'application/json'})

    return ''

if __name__ == '__main__':
    app.debug = 'DEBUG' in environ
    app.run()
