#!/bin/bash

cd "$(dirname "$0")"

git pull

./sidep.py

DATE=$(date)
git commit -am "Update for ${DATE}"
git push
