import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID='spotify-client-id'

SPOTIPY_CLIENT_SECRET='spotify-client-secret'

# make the same redirect uri in Spotify dashboard.
SPOTIFY_REDIRECT_URI = 'spotify-redirect-uri'

scopes = 'playlist-read-private,playlist-modify-public'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = SPOTIPY_CLIENT_ID,
                                                client_secret= SPOTIPY_CLIENT_SECRET,
                                                redirect_uri= SPOTIFY_REDIRECT_URI,
                                                scope=scopes))

def get_curr_DW_tracks():
    ''' Get current Discover Weekly tracks. '''

    result = sp.search("Discover Weekly", limit=1, type='playlist')

    DW_play_ID = result['playlists']['items'][0]['id']

    DW_tracks = sp.playlist_items(DW_play_ID,fields='items.track.id,total',
                                    additional_types=['track'])
    DW_track_ids = []
    for each in DW_tracks['items']:
        DW_track_ids.append(each['track']['id'])

    return DW_track_ids

def make_DLW():
    ''' Make DLW playlist. '''

    user_id = sp.me()['id']
    sp.user_playlist_create(user_id, name= "Discover Last Weekly", 
                            description = "Your last week's Discover Weekly. Never worry about forgetting songs from last week!" )

def get_DLW_id():
    ''' Return the id of DLW or False if DLW does not exist. '''

    results = sp.current_user_playlists()
   
    for i, item in enumerate(results['items']):
        if 'Discover Last Weekly' in item['name']:
            DLW_id = item['id']
            return DLW_id

    return False


def add_DW_tracks_to_DLW(DW_tracks,DLW_id):
    ''' Add the current DW tracks to DLW. '''

    sp.playlist_add_items(DLW_id, DW_tracks)


def main():

    DLW_id = get_DLW_id()

    if DLW_id == False:
        make_DLW()
        DLW_id = get_DLW_id()

    DW_tracks = get_curr_DW_tracks()
    add_DW_tracks_to_DLW(DW_tracks,DLW_id)

if __name__ == '__main__':
    main()