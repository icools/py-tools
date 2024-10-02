#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <YouTube URL>"
  exit 1
fi

# Run the Docker command with the provided URL
docker run --rm -v ~/Downloads:/downloads yt-dlp-python "$1"