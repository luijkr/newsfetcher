#!/bin/bash

source /home/pi/newsfetcher-variables.sh

cd /home/pi/newsfetcher || exit

source venv/bin/activate

python main.py --mode=fetch

python main.py --mode=analyze
