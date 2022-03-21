# Discover-Last-Weekly
Provide a copy of last week's Spotify Discover Weekly so you never forget!

## Setting up to project

1. Clone the repository to your local machine.
    ```
    git clone git@github.com:brandonvu12/Discover-Last-Weekly.git
    ```
2. Change into the project directory.
    ```
    cd Discover-Last-Weekly
    ``` 
3. Install the dependencies
    ```
    pip install -r requirements.txt
    ```   
    ### Getting Spotify API information
      1. Go to https://developer.spotify.com/dashboard/login and sign up/login.
      2. Create an App.
      3. Select Edit Settings.
      4. Add Redirect URI. (e.g. `http://localhost:8888/callback`)
      5. Copy the Client ID and Client Secret strings.
      6. Paste strings in `discover_last_weekly.py`.
 
        SPOTIPY_CLIENT_ID='spotify-client-id'

        SPOTIPY_CLIENT_SECRET='spotify-client-secret'

        SPOTIFY_REDIRECT_URI = 'spotify-redirect-uri' (e.g. `http://localhost:8888/callback`)
      

4. Run script
    ```
    python3 discover_last_weekly.py
    ```
    
## TODO
1. Automate script weekly on Sundays (before Discover Weekly updates for the week).
