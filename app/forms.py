# from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from flask_wtf import *
# from flask_wtf.validators import DataRequired
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyForm(FlaskForm):
    # get user's spotify playlists
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    s_playlists = []
    playlists = sp.user_playlists('spotify')
    while playlists:
        for i, p in enumerate(playlists['items']):
            s_playlists.append(p)
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
    # show drop down select of all their playlists and submit button
    state = SelectField(label='Choose a Playlist', choices=s_playlists)
    s_playlist = StringField('Spotify Playlist URL')
    submit = SubmitField('Convert')