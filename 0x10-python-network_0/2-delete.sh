#!/bin/bash
# Script that sends a DELETE request to the URL passed as the first argument  displays the body of the responses
curl -sX DELETE "$1"
