import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os


load_dotenv("")

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")

SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")


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

def refresh_DLW(DLW_id, DW_tracks):
    ''' Delete existing DLW and add new DW tracks to DLW. '''
    
    DLW_tracks = sp.playlist_items(DLW_id,fields='items.track.id,total',
                                    additional_types=['track'])
    DLW_track_ids = []
    for each in DLW_tracks['items']:
        DLW_track_ids.append(each['track']['id'])

    sp.playlist_remove_all_occurrences_of_items(DLW_id, DLW_track_ids)

    add_DW_tracks_to_DLW(DW_tracks,DLW_id)

def main():
    print("Getting DLW id")
    DLW_id = get_DLW_id()
    print("Fetching DW tracks")
    DW_tracks = get_curr_DW_tracks()
    if DLW_id == False:
        print("Making new DLW and adding DW tracks")
        make_DLW()
        DLW_id = get_DLW_id() 
        add_DW_tracks_to_DLW(DW_tracks,DLW_id)
    else:
        print("Reresh DLW with DW tracks")
        refresh_DLW(DLW_id,DW_tracks)

if __name__ == '__main__':
    main()