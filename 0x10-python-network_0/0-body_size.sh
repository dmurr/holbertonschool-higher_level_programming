#!/bin/bash
# Sends request to URL and displays bytes of reponse
curl -sI $1 | grep Content-Length | cut -f2 -d' '
