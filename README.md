[![GitHub license](https://img.shields.io/badge/license-GPLv2-blue.svg)](https://raw.githubusercontent.com/Facetracker-project/facetracker-core/master/COPYING)
[![GitHub license](https://img.shields.io/badge/packages-youtube--dl%2Fbs4-red.svg)](https://raw.githubusercontent.com/Facetracker-project/facetracker-core/master/COPYING)
[![GitHub license](https://img.shields.io/badge/author-naper-blue.svg)](https://raw.githubusercontent.com/Facetracker-project/facetracker-core/master/COPYING)
[![GitHub license](https://img.shields.io/badge/version-0.0.2-orange.svg)](https://raw.githubusercontent.com/Facetracker-project/facetracker-core/master/COPYING)
# spotify-dl
A script that allows you to download spotify songs or playlists, written in python

This README would normally document whatever steps are necessary to get spotify-dl up and running.

This repo was forked from [Hamza Bourrahim](https://github.com/invicnaper) and modified to download either tracks and playlists.

### What is this repository for? ###

* spotify-dl allows you to download spotify songs or playlist
* Version 0.0.4
* This repo contains spotify-dl source code

### Screen ###

![alt text](http://nsa37.casimages.com/img/2016/02/13/160213111903934479.png "spotfy-dl screen")

# How to Install ?
To use spotify-dl, you need to install thoses packages :
  * bs4
  * youtube-dl
  
# MAC OSx
You can use brew to install youtube-dl:
  
    $ brew install youtube-dl
    
And pip to install bs4:
  
    $ pip install beautifulsoup4
    
# Linux (debian)
Use apt-get install to install youtube-dl:

    $ sudo apt-get install youtube-dl
    
And pip to install bs4:
  
    $ pip install beautifulsoup4

# Spotify API
The new version of the spotify api require an access_token for requests you can check out https://developer.spotify.com/migration-guide-for-unauthenticated-web-api-calls/.

The new patch of spotify-dl have a new argument called: --access_token, so the new usage of spotify-dl would be:
  
    $ ./spotify-dl --track {spotify_song_id} --dl youtube --access_token <your_access_token>
    
You can get the access token from the url generated while executing: 

    $ ./spotify-dl --gen_url 
    
You also have to create an application on https://developer.spotify.com/.

Or you can get one on https://developer.spotify.com/web-api/console/get-playlist-tracks/, just click 'generate oauth token' and copy it.

Then, change:

    CLIENT_ID="spotify-app-id"
    CALL_BACK_URL="url"
    DEVELOPER_KEY="youtube-api-key"

# How to use ?
You can either use your spotify account or downloading single track or playlist by providing an ID. Ex.:

    $ ./spotify-dl --track {spotify_song_id} --dl youtube
    
This will download the track and save it as mp3 format

You can get the song ID by getting the spotify URI of the song

{spotify_song_id_ex} : 28Ct4qwkQXY2W5yyNCLuVI

You can download an entire playlist by providing the playlist's user and link:

    $ ./spotify-dl --playlist {spotify_playlist_link} --user {playlist_user} --dl youtube --access_token <your_access_token>

If you want to set an output folder, you can do it providing the folder name between "". Ex.:

    $ ./spotify-dl --playlist {spotify_playlist_link} --user {playlist_user} --dl youtube --access_token <your_access_token> --folder {"folder name"}


### Contributors ###
* Hamza Bourrahim
* Willian Alves