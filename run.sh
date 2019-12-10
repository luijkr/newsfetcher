#!/usr/bin/env bash

num_instances=$(ps -ef | grep mongod | grep -v grep | wc -l | tr -d ' ')
if [ "$num_instances" -eq "0" ]; then
  echo "Mongo not running, starting now."
   brew services start mongodb-community@4.2
fi

echo "Starting program."
python main.py
