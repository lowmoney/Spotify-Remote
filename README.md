# Spotify Remote

A class that uses the Spotipy API to make Spotify API calls easier to use and more intuitive.
Currently supports playing of track, pause track, goto next track, previous track, turn repeat on/off right now... more to come later


### Why use this?
It`s a little smarter.... in that it offers a nice search feature for YOUR library (might add feature to search other tracks that are not in user library)

An important thing to note is that the search matches your argument to the user generated library

For example, lets say we want to play the song 'Drive Safe' by Rich Brian from his new album The Sailor, we call the command
```
remote.play('Drive Safe')
```
Now if the user has a premium account for Spotify then it will start to play that song on the current active device.

But what if we spell the name of the track wrong or we don`t capitalize the first characters
like...
```
remote.play('drive safe')
remote.play('drivesafe')
remote.play('drvie safe')
```
Remote will still play 'Drive Safe' by Rich Brian,
Remote uses fuzzywuzzy for the track search to make this possible

IMPORTANT NOTE(S)
* As of right now, only the users current album tracks are usable for the search function
    * Will work on adding searching Spotify if the track cannot be found on the users library

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* To run you`ll need to have spotipy and fuzzywuzzy installed
* fuzzywuzzy uses optional python-Levenshtein. They recomend the use of it as it speeds up string matching 

Use pip to install these two or three packages
```
pip3 install spotipy
pip3 install fuzzywuzzy
pip3 install python-Levenshtein (this package is optional)
```

### Installing

To install simply clone this git repository or download the zip file
Hoping to have a pip install later on when all features are added
```
git clone https://github.com/lowmoney/Spotify-Remote.git
```

## How to Use
Copy over the remote.py file to your project
Then import class
```
from remote import remote
```

Then use the Spotipy API to get a user token
You must pass these paramters, in quotes, to scope when authenticating for proper use and full functionality
* user-read-private
* user-read-playback-state
* user-library-read
* playlist-read-private
* user-modify-playback-state

I`ll give an example
```
CLIENT_ID = '######'
CLIENT_SECRET = '######'
REDIRECT_URI = 'https://example.com/callback/'

# The scope is important, the order on how you put them does not matter 
#what matters is that it`s there
scope = 'user-read-private user-library-read playlist-read-private 

user-read-playback-state user-modify-playback-state'

try:
    token = util.prompt_for_user_token(SpotifyId, scope, client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(SpotifyId, scope, client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)

spotify_object = spotipy.Spotify(auth=token)
```

Now we can use our class
```
remote = remote(spotify_object)
```
Finnaly we can call our commands as follows
We`re going to use the play() function to play a track 
```
remote.play('track name')
```

## Commands
A list of commands you`ll use
* remote.play(key=None,device=None)
    * key is the search
    * device is name of the device to play on
    * If no arguments are given then play current song on current playback device
    * If key is given and no device then play key at current playback device
    * If key is not given and device is given then play current song at given device
    * If key and device are given then play key at device
* remote.pause(device=None)
    * If device is None then we pause the current active device
    * If device is given then pause that device`s playback
* remote.next(device=None)
    * If device is None then we go to next track
    * If device is given then goto next track on that device
* remote.last(device=None)
    * If device is None then we go to last track played before current track
    * If device is given then goto last track played on that device
* remote.rep(off=False,device=None)
    * If device is not given and off is False then repeat track
    * If off is not False then turn repeat off
    * If device is not None and off is False then turn repeat on at device

## Built With

* [Spotipy](https://github.com/plamere/spotipy) - A Spotify API for Python
* [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) - String Matching Magic

## Contributing

Just me right now

## Things that will be added... hopefully
* Playlist support
* Searching Spotify if the track is not in the User Library
* Lastly add install from package manager like pip

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* The Spotipy team for making the Spotify API available on Python
* The SeatGeek team for making FuzzyWuzzy open source
