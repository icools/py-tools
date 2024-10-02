#!/bin/bash

# Check if three arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <YouTube URL> <duration> <format>"
    exit 1
fi

YOUTUBE_URL=$1
DURATION=$2
FORMAT=$3

# Set the output directory
OUTPUT_DIR=~/Downloads

# Run docker and pass the arguments
docker run -v "$OUTPUT_DIR:/root/Downloads" yt-dlp-stream-clip "$YOUTUBE_URL" "$DURATION" "$FORMAT"