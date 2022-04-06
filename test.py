import time
import os
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

import requests

import subprocess

scope = 'user-read-currently-playing'
# scope = 'user-read-playback-state'
# works as well

envs = os.environ

username = envs["SPOT_USERNAME"]
client_id = envs["SPOT_CLIENT_ID"]
client_secret = envs["SPOT_CLIENT_SECRET"]
redirect_uri = 'http://localhost:8888/callback'

token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

spotify = spotipy.Spotify(auth=token)

tracks = {
    'old': { 'id': 'old' },
    'curr': { 'id': 'curr' }
}

i = 0

while True:
    time.sleep(1)
    tracks['old'] = tracks['curr']
    tracks['curr'] = spotify.current_user_playing_track()['item']

    # print(tracks['curr'] )

    # print

    if tracks['curr'] == None:
        # print('none')
        continue
    elif tracks['old']['id'] == tracks['curr']['id']:
        continue
    else:
        print('requesting')

        images = tracks['curr']['album']['images']
        image_url = images[0]['url']
        for image in images:
            if image['height'] == 64:
                image_url = image['url']
        img_data = requests.get(image_url).content
        if i == 2:
            i = 0
        else:
            i += 1
        with open(f'album_cover_{i}', 'wb') as handler:
            handler.write(img_data)


        subprocess.Popen([
            "sudo",
            "./led-image-viewer",
            "--led-cols=64",
            "--led-rows=64",
            "--led-gpio-mapping=adafruit-hat",
            "--led-slowdown-gpio=5"
        ])
        # print('huh')
