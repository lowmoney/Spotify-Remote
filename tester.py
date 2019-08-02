import os,sys,json,spotipy,webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from remote import remote

# set username
username = '8s6vqyoln8bt6uegx72wy1r2h?si=otXcdLH1ToCIh7xjgIwaUw'

# set some constants
CLIENT_ID = '15e3935c4b0c4d78add824ceff2c5e97'
CLIENT_SECRET = '729b4af2031b4529b1c8e51883e72d25'
REDIRECT_URI = "https://example.com/callback/"
scope = 'user-read-private user-library-read playlist-read-private user-read-playback-state user-modify-playback-state'

try:
    token = util.prompt_for_user_token(username, scope, client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope, client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)


# create spotifyObject
sp = spotipy.Spotify(auth=token)

sp = remote(sp)