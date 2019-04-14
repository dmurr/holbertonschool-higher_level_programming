#!/bin/bash
# Sends GET request with extra header and displays body of response
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
