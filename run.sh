#!/bin/bash

source "$HOME/newsfetcher-variables.sh"

cd "$HOME/newsfetcher" || exit

source venv/bin/activate

python main.py --mode=fetch

python main.py --mode=analyze
