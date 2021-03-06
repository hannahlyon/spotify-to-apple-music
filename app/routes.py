from flask import render_template, redirect
from app import app
from app.forms import SpotifyForm

# @app.route('/index', methods=['GET', 'POST'])
# def index():
#     form = LoginForm()
#     return render_template('app.html', form=form)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def spotify_login():
    return render_template('index.html')

@app.route('/spotify', methods=['GET', 'POST'])
def choose_spotify():
    form = SpotifyForm()
    return render_template('app.html', form=form)
    # results = sp.user_playlists('spotify')