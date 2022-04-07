#!/bin/bash

# set these up in your spotify developer dashboard
export SPOTIPY_USERNAME='{username}'
export SPOTIPY_CLIENT_ID='{client id}'
export SPOTIPY_CLIENT_SECRET='{client secret}'
export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'

sudo -E python3 test.py
