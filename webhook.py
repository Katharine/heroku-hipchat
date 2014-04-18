from os import environ
from flask import Flask, request, make_response
import urllib2

app = Flask(__name__)

@app.route('/deployed', methods=['POST'])
def hook():
    to_send = {
        'color': 'purple',
        'message': "{user} deployed <a href='{url}'>{app}</a> ({head}):<br>{git_log}".format(request.form),
        'message_format': 'html'
    }
    req = urllib2.urlopen("https://api.hipchat.com/v2/room/{HIPCHAT_ROOM}/notification?auth_token={HIPCHAT_TOKEN}".format(environ))
    try:
        req.read()
    finally:
        req.close()

if __name__ == '__main__':
    app.debug = 'DEBUG' in environ
    app.run()
