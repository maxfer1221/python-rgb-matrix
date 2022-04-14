import time
import os
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

import requests

import subprocess

scope = 'user-read-currently-playing'
# scope = 'user-read-playback-state'
# works as well

username = os.environ["SPOTIPY_USERNAME"]

spotify = spotipy.client.Spotify(requests_timeout=3, auth_manager=SpotifyOAuth(
    open_browser=False, scope=['user-read-currently-playing', 'user-read-recently-played'],
))

track = None
saved_url  = None
active_url = None

while True:
    time.sleep(1)

    
    try:
        track = spotify.current_user_playing_track()
    except Exception as e:
        print("failed to get current track: ", e)
        continue

    if track is None:
        continue
    
    images = track['item']['album']['images']
    # images = track['album']['images']
    urls = map(lambda el: el['url'], images)

    if active_url in urls:
        continue

    if saved_url not in urls:
        image_url = images[0]['url']
        for image in images:
            if image['height'] == 64:
                image_url = image['url']

        try:
            print("getting image")
            img_data = requests.get(image_url, verify=False, timeout=1).content
            saved_image = image_url
        except Exception as e:
            print("failed to get images: ", e)
            continue

    with open(f'album_cover', 'wb') as handler:
        handler.write(img_data)
    
    pids = []

    try:
        ps = subprocess.Popen(('ps', '-A'), stdout=subprocess.PIPE)
        grep = subprocess.Popen(('grep', 'led-image-viewe'), stdout=subprocess.PIPE, stdin=ps.stdout)
        pids = subprocess.check_output(('awk', '{ print $1 }'), stdin=grep.stdout)
        pids = pids.split(b'\n')
        pids = map(lambda el: el.decode('utf-8'), pids)

        pids = filter(lambda el: el != '', pids)
        pids = map(lambda el: int(el), pids)
    
    except subprocess.CalledProcessError as err:
        print("piping failed, " + err)

    subprocess.Popen([
        "sudo",
        "../led-image-viewer",
        "album_cover",
        "--led-cols=64",
        "--led-brightness=70",
        "--led-rows=64",
        "--led-gpio-mapping=adafruit-hat",
        "--led-slowdown-gpio=5"
    ])

    active_url = image_url

    for pid in pids:
        os.system(f'sudo kill -9 {pid}')
    else:
        continue

def map_tracks(track):
    if track is None:
        return None
    return track['track']['images']
