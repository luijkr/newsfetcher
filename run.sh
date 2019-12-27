#!/bin/bash

cd /home/pi/newsfetcher

source venv/bin/activate

python main.py --mode=fetch

python main.py --mode=analyze
