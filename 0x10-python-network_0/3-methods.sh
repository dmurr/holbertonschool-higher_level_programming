#!/bin/bash
# Displays HTTP methods a server will accept
curl -sI 0.0.0.0:5000/route_4 | grep "Allow:" | cut -f2- -d' '
