#!/bin/bash

export SPOTIPY_USERNAME='lsxm86rfu1qw89r7ph5lsbz53'
export SPOTIPY_CLIENT_ID='5b6b1445709449c18cec4d828f483d6f'
export SPOTIPY_CLIENT_SECRET='2d55c6bb7f6d449cac5a9bfbd584db61'
export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'

sudo -E python3 test.py
