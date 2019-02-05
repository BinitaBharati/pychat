#!/bin/bash
set -x

pip3 install Django
#python3 -m django --version

#install Djangio channels for websocket support
pip3 install -U channels
pip3 install channels_redis

#Unused Jinja, but my code is referring. Need to clean that up.
pip3 install Jinja2

