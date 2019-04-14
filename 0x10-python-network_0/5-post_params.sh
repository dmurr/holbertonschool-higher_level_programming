#!/bin/bash
# Sends POST request to the passed URL and displays response
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
