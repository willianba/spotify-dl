#!/usr/bin/python

import os
import sys
import json
import urllib
import urllib2
import argparse
import traceback
import subprocess
from bs4 import BeautifulSoup
from StringIO import StringIO

RED     = "\033[31m"
GREEN   = "\033[32m"
BLUE    = "\033[34m"
YELLOW  = "\033[36m"
DEFAULT = "\033[0m"

ACTION  = BLUE + "[+] " + DEFAULT
ERROR   = RED + "[+] " + DEFAULT
OK      =  GREEN + "[+] " + DEFAULT

#=======================
#   Spotify application
#=======================
CLIENT_ID="REPLACE_HERE"
# The callback can be http://127.0.0.1
CALL_BACK_URL="REPLACE_HERE"

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "REPLACE_HERE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))

  print "Videos:\n", "\n".join(videos), "\n"
  print "Channels:\n", "\n".join(channels), "\n"
  print "Playlists:\n", "\n".join(playlists), "\n"

def searchYoutube(trackname):
    textToSearch = trackname
    query = urllib.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    #we return the first result
    return "https://youtube.com" + soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]['href']

def getTrackName(id, access_token):
    """ get the spotify track name from id """
    print ACTION + "Getting track name"
    proc = subprocess.Popen('curl -sS -X GET "https://api.spotify.com/v1/tracks/'+ id +'?market=ES" -H "Authorization: Bearer '+ access_token +'"', shell=True, stdout=subprocess.PIPE)
    tmp = proc.stdout.read()
    data = json.loads(tmp)
    if 'error' in data:
        print ERROR + "can't found song name"
        print ERROR + data['error']['message']
        return None
    else:
        print OK + "Name is " + data["name"]
        return data["name"]

def getPlaylistSongs(user, playlist, access_token):
    """ get the spotify tracks names from playlist link """
    print ACTION + "Getting tracks names"
    proc = subprocess.Popen('curl -sS -X GET "https://api.spotify.com/v1/users/' + user + '/playlists/' + playlist + '/tracks?market=ES&fields=items(track)" -H "Authorization: Bearer '+ access_token +'"', shell=True, stdout=subprocess.PIPE)
    tmp = proc.stdout.read()
    data = json.loads(tmp)
    names = []
    for item in data['items']:
        if 'error' in data:
            print ERROR + "Can't found song name"
            print ERROR + data['error']['message']
            return None
        else:
            name = str(item['track']['name'])
            names.append(name)
    return names

def genUrl():
    """ gen url for getting access token """
    print ACTION + "Generating url for access token"
    print OK +  "https://accounts.spotify.com/authorize?client_id="+ CLIENT_ID + "&response_type=token&redirect_uri=" + CALL_BACK_URL

def getAccessToken():
    """ get access token """
    print ACTION + "Getting access token"
    proc = subprocess.Popen('curl -sS -X GET "https://accounts.spotify.com/authorize?client_id='+ CLIENT_ID +'&response_type=token&redirect_uri='+ CALL_BACK_URL +'" -H "Accept: application/json"', shell=True, stdout=subprocess.PIPE)
    tmp = proc.stdout.read()
    data = json.loads(tmp)

    print data

def downloadYoutube(link):
    """ downloading the track """
    print ACTION + "Downloading song"
    proc = subprocess.Popen('youtube-dl -x --format best --audio-format=mp3 --audio-quality=0 -o %\(title\)s.%\(ext\)s '+ link, shell=True, stdout=subprocess.PIPE)
    tmp = proc.stdout.read()
    print OK + "Song Downloaded"

def rename_songs(path):
    filenames = os.listdir(path)
    for filename in filenames:
        new_name = filename.split('-')[0] + "-" + filename.split('-')[1] + ".mp3"
        os.rename(path + "/" + filename, path + "/" + new_name)

def header():
    """ header informations """
    print RED + "@ spotify-dl.py version 0.0.4"
    print YELLOW + "@ author : Naper"
    print BLUE + "@ Designed for OSx/linux"
    print "" + DEFAULT


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='spotify-dl allows you to download your spotify songs')
    parser.add_argument('--verbose', action='store_true', help='verbose flag')
    parser.add_argument('--dl', nargs=1, help="set the download methode")
    parser.add_argument('--user', nargs=1, help="set the spotify login")
    parser.add_argument('--password', nargs=1, help="set the spotify password")
    parser.add_argument('--traceback', action='store_true', help="enable traceback")
    parser.add_argument('--gen_url', action='store_true', help="generate url for getting access_token")
    parser.add_argument('--track', nargs=1, help="spotify track id")
    parser.add_argument('--playlist', nargs=2, help="spotify playlist's user and link")
    parser.add_argument('--access_token', nargs=1, help="set the access_token")
    parser.add_argument('--folder', nargs=1, help="set output folder")
    parser.add_argument('-m', nargs=1, help="set a methode")

    args = parser.parse_args()

    reload(sys)  
    sys.setdefaultencoding('utf-8')

    try:
        header();
        if args.gen_url:
            genUrl()
        else:
            if args.dl and args.access_token and args.dl[0] == 'youtube':
                if args.track:
                    name = getTrackName(args.track[0], args.access_token[0])
                    link = searchYoutube(name)
                    downloadYoutube(link)
                elif args.playlist:
                    names = getPlaylistSongs(args.playlist[0], args.playlist[1], args.access_token[0])
                    for song in names:
                        if song != None:
                            print OK + "Name is " + song
                            link = searchYoutube(song)
                            downloadYoutube(link)
                if args.folder:
                    if not os.path.isdir(args.folder[0]):
                        create_folder = 'mkdir "'+ args.folder[0] +'"'
                        os.system(create_folder)
                    move = 'mv *.mp3 ' + os.getcwd() + '/' + args.folder[0]
                    os.system(move)
                    rename_songs(args.folder[0])
            else:
                print ERROR + "Use --help for help"
    except Exception, err:
        print ERROR + "An HTTP error occurred\n"
        if args.traceback:
            traceback.print_exc()
