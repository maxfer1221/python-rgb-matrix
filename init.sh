#!/bin/bash

# set these up in your spotify developer dashboard
export SPOTIPY_USERNAME='{username}'
export SPOTIPY_CLIENT_ID='{client id}'
export SPOTIPY_CLIENT_SECRET='{client secret}'

sudo -E python3 test.py
