import json

from flask import (Flask, render_template, redirect,
                   url_for, request, make_response,
                   flash)
from options import DEFAULTS

app = Flask(__name__)
app.secret_key = "fewef4f4f43fVREBVTREGY$%^$#%#REFGsadwq#@$##"


def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/')
def index():
    return render_template('index.html', saves=get_saved_data())


@app.route('/builder')
def builder():
    return render_template(
        'builder.html',
        saves=get_saved_data(),
        options=DEFAULTS
    )

@app.route('/save', methods=['POST'])
def save():
    flash("Alright! That looks awesome!")
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    if 0:
        import flask, werkzeug
        isinstance(response, flask.wrappers.Response)
    response.set_cookie('character', json.dumps(dict(data)))
    return response

if __name__ == '__main__':
    from os import environ
    if 'WINGDB_ACTIVE' not in environ:
        app.debug = True
    app.run(port=8000, host='192.168.1.114', use_reloader=True)    