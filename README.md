# Spotify Remote

A class that uses the Spotipy API to make Spotify API calls easier to use.
Only supports playing of track, pause track, goto next track, previous track, turn repeat on/off right now... more to come later


### Why use this?
It`s a little smarter.... in that it offers a nice search feature for YOUR library (might add feature to search other tracks that are not in user library)

An important thing to note is that the search takes your search input and compares that to your library 

For example lets say we want to play the song 'Drive Safe' by Rich Brian and we assume that this album or track is in the user`s library then we call the command
```
remote.play('Drive Safe')
```
Now if the user has a premium account for Spotify then it will start to play that song on the current active device.

But what if we spell the name of the track wrong or dont capitalize the char
like...
```
remote.play('drive safe')
remote.play('drivesafe')
remote.play('drvie safe')
```
Remote will still play Drive Safe
Remote uses fuzzywuzzy for the track search to make this possible

IMPORTANT NOTE
* The Spotipy API does not support track playback
* To get around this I pass the track you want to play twice 
* I`m Going to add skip track function after play to not have the track repeat

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* To run you`ll need to have spotipy and fuzzywuzzy installed
* fuzzywuzzy uses optional python-Levenshtein. They recomend the use of it as it speeds up string mathcing 

Use pip to install these two(three)
```
pip3 install spotipy
pip3 install fuzzywuzzy
pip3 install python-Levenshtein (optional)
```

### Installing

To install simply clone this git repository or download the zip file
Working on pip install instead
```
git clone https://github.com/lowmoney/Spotify-Remote.git
```

## Use

First import class
```
from remote import remote
```

Then use the Spotipy API to get a user token
Pass these paramters to scope when authenticating in quotes
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

# The scope is important, the order on how you put them does not matter what #matters is that it`s there
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
    * If key is given but no device name then    the kley will play on the current active   device
    * If key is not given and device is not      given then we resume playback at current   active device
* remote.pause(device=None)
    * If device is None then we pause the 
      current active device
    * If device id is given then pause that      device`s playback
* remote.next(device=None)
    * If device is None then we go to next       track
    * If device id is given then goto next       track on that device
* remote.last(device=None)
    * If device is None then we go to last       track
    * If device id is given then goto last       track on that device
* remote.rep(off=None,device=None)
    * Although there this function needs work and should not be used

## Built With

* [Spotipy](https://github.com/plamere/spotipy) - The Spotify API for Python
* [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) - String Matching

## Contributing

Just me right now

## Things that will be added... hopefully
* Playlist support
* Make device playback smarter
    * In that when a user types in 'desktop' it knows to choose the 'DESKTOP-#####' but making sure the pause and skip and last work the same way
* After playing track skip track since duplicate is added
    * Spotipy does not support the playback of single track
* Searching Spotify if the track is not in the User Library
* General optimzation and making things more readable
* Incorporating design-by-contract more in functions as this is the design structure
* Add more comments to give more info
* Lastly add install from package manager like pip

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* The Spotipy team for making this API
* The SeatGeek team for making FuzzyWuzzy open source
