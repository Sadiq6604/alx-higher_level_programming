#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me that is causes the server to resooopond with a message containing You got me!, in the body of the response.
curl -s 0.0.0.0:5000/catch_me -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool"
