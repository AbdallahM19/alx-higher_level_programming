#!/bin/bash
#Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -s -I "$1" | grep "Allow" | cut -d ': ' -f 2-
