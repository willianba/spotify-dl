[![GitHub license](https://img.shields.io/badge/license-GPLv2-blue.svg)](https://raw.githubusercontent.com/Facetracker-project/facetracker-core/master/COPYING)
[![GitHub license](https://img.shields.io/badge/packages-youtube--dl%2Fbs4-red.svg)](https://raw.githubusercontent.com/Facetracker-project/facetracker-core/master/COPYING)
[![GitHub license](https://img.shields.io/badge/author-naper-blue.svg)](https://raw.githubusercontent.com/Facetracker-project/facetracker-core/master/COPYING)
[![GitHub license](https://img.shields.io/badge/version-0.0.5-orange.svg)](https://raw.githubusercontent.com/Facetracker-project/facetracker-core/master/COPYING)
# spotify-dl
A script that allows you to download spotify songs or playlists, written in python

This README would normally document whatever steps are necessary to get spotify-dl up and running.

This repo was forked from [Hamza Bourrahim](https://github.com/invicnaper) and modified to download either tracks and playlists.

### What is this repository for? ###

* spotify-dl allows you to download spotify songs or playlists
* Version 0.0.5
* This repo contains spotify-dl source code

### Screen ###

![alt text](http://nsa37.casimages.com/img/2016/02/13/160213111903934479.png "spotify-dl screen")

# How to Install?
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
The new version of the spotify API require an access token for requests. You can check out https://developer.spotify.com/migration-guide-for-unauthenticated-web-api-calls/.
  
The easy way to get an access token is at https://developer.spotify.com/web-api/console/get-playlist-tracks/. Just click 'generate OAuth token' and copy it.

You can also get the access token from the url generated while executing: 

    $ ./spotify-dl.py --gen_url 
    
You must have to create an application on https://developer.spotify.com/.

To get the developer key, go to https://cloud.google.com/console, create an application and get the API key value from the APIs & auth > Registered apps. Please ensure that you have enabled the YouTube Data API for your project.

Then, change:

    CLIENT_ID="spotify-app-id"
    CALL_BACK_URL="url"
    ACCESS_TOKEN="token"
    DEVELOPER_KEY="youtube-api-key"

# How to use?
## Tracks
You can download a single track by providing an ID. Ex.:

    $ ./spotify-dl.py --track {spotify_song_id}
    
This will download the track and save it as mp3 format.

You can get the song ID by getting the spotify URI of the song:

Spotify URI: spotify:track:2iuZJX9X9P0GKaE93xcPjk

The song ID will be: 2iuZJX9X9P0GKaE93xcPjk

## Playlists 
You can download an entire playlist by providing its user and ID:

    $ ./spotify-dl.py --playlist {playlist_user_id} {playlist_id}

If you want to set an output folder, you can do it providing the folder name between "". Ex.:

    $ ./spotify-dl.py --playlist {playlist_user_id} {playlist_id} --folder {"folder name"}

Ex.:

Spotify URI: spotify:user:spotify:playlist:37i9dQZF1DZ06evO1c6rSg

The user is: spotify

The playlist ID is: 37i9dQZF1DZ06evO1c6rSg

The usage is:

	$ ./spotify-dl.py --playlist spotify 37i9dQZF1DZ06evO1c6rSg

## Access Tokens
Sometimes the access tokens get expired, causing the script to show "An error occurred".

This way, it is necessary a **new access token** in order to properly use Spotify API.

### Author ###
* Hamza Bourrahim

### Contributors ###
* Willian Alves
