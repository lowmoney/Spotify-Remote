import spotipy
from fuzzywuzzy import fuzz

class remote:
    def __init__(self,spotify_object):
        self.spotify_object = spotify_object
        self.user_albums = self.album_maker(spotify_object)
        self.user = (spotify_object.me())['product']
    

    def album_maker(self,spotipy_object):
        names = []
        album = []
        user_spotify_album = spotipy_object.current_user_saved_albums(limit=50,offset=0)

        for x in range (0,len(user_spotify_album['items'])):
            names.append(((user_spotify_album['items'][x]['album']['name']),(user_spotify_album['items'][x]['album']['uri'])))
        
        for x in range (0,len(names)):
            album.append((names[x],self.scrape_track(user_spotify_album,x)))
        return album

    def scrape_track(self,user_album,album_num):
        tracks = []
        track_ammount = int(user_album['items'][album_num]['album']['total_tracks'])

        for x in range (0,track_ammount):
            tracks.append(((user_album['items'][album_num]['album']['tracks']['items'][x]['name']),(user_album['items'][album_num]['album']['tracks']['items'][x]['uri'])))
        
        return tracks
    
    def search(self,key):
        location = []
        for x in range(0,len(self.user_albums)):
            for y in range (0,len(self.user_albums[x][1])):
                # Add FuzzyWuzzy to make search better
                # If the key len is bigger than five, average length of a word, use fuzz.token_sort_ratio for maybe better results
                if len(key) > 5:
                    if fuzz.token_sort_ratio(key,self.user_albums[x][1][y][0]) > 70:
                        location.append(x)
                        location.append(y)
                # If the key len is less than five, average length of a word, use fuzz.ratio to find if string are simialr
                elif len(key) < 5:
                    if fuzz.ratio(key,self.user_albums[x][1][y][0]) > 50:
                        location.append(x)
                        location.append(y)
        

        return location

    # Save devices locally so we can look at devices?
    # Add FuzzyWuzzy to make search easy
    def devices(self):
        device = self.spotify_object.devices()
        devices = []

        for x in range(0, len(device['devices'])):
            devices.append((device['devices'][x]['name'],device['devices'][x]['id']))
        return devices

    def findDevice(self,device):
        devices = self.devices()
        for x in range (0,len(devices)):
            # Add FuzzyWuzzy to make search easy
            if fuzz.token_sort_ratio(device,devices[x][0]) > 65:
                try:
                    return devices[x][1]
                except IndexError:
                    print("Spotify is not opened  on any device")
            # Safe bet
            # if device in devices[x][0]:
            #     try:
            #         return devices[x][1]
            #     except IndexError:
            #         print("Spotify is not opened on any device")

    def activeDevice(self):
        devices = self.spotify_object.devices()
        for x in range (0,len(devices)):
            try:
                if devices['devices'][x]['is_active']:
                    # This try except might be useless
                    try:
                        return devices['devices'][x]['id']
                    except IndexError:
                        print("No active devices found or no device has Spotify opened")
            except IndexError:
                print("No active devices found or no device has Spotify opened")

    # Add a better way to choose deivces
    def play(self,key=None,location=None):
        # Check some states
        # See if user can even use play method
        if self.user == 'open' or self.user == 'free':
            return 'must have premium'
        # If user gives no key and no location then resume playback on current location
        elif key is None and location is None:
            self.spotify_object.start_playback(uris = [((self.spotify_object.currently_playing())['item']['uri']),((self.spotify_object.currently_playing())['item']['uri'])])
        # If user gives no location play given key at current device playback
        elif location is None and key is not None:
            album_location = self.search(str(key))
            track_id = str(self.user_albums[album_location[0]][1][album_location[1]][1])
            self.spotify_object.start_playback(uris = [track_id,track_id])
        # If user gives key and location then play key at device
        elif key is not None and location is not None:
            album_location = self.search(str(key))
            track_id = self.user_albums[album_location[0]][1][album_location[1]][1]
            location = self.findDevice(location)
            self.spotify_object.start_playback(device_id=location,uris=[track_id,track_id])

    # Pause playback
    def pause(self,device=None):
        # See if user has premium
        if self.user == 'open' or self.user == 'free':
            return 'must have premium'
        # If user gives us no device then assume the current playing device
        elif device is None:
            self.spotify_object.pause_playback(device_id = self.activeDevice())
        elif device is not None:
            self.spotify_object.pause_playback(device_id = device)

    # Go to next track
    def next(self,device=None):
        if device is None:
            self.spotify_object.next_track()
        else:
            self.spotify_object.next_track(device)

    # Go to previous track
    def last(self,device=None):
        if device is None:
            self.spotify_object.previous_track()
        else:
            self.spotify_object.previous_track(device_id=device)
    
    # Repeat song
    def rep(self,off=False,device=None):
        if device is None:
            self.spotify_object.repeat('track')
        if not off:
            self.spotify_object.repeat('off')
        else:
            self.spotify_object.repeat('track',device_id=device)