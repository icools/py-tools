#!/bin/bash
# docker build -t yt-dlp-stream-clip .    
# ./run.sh 10 mp4 ${url}

# Check if three arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <duration> <format> <YouTube URL>"
    exit 1
fi

DURATION=$1
FORMAT=$2
YOUTUBE_URL=$3

# Set the output directory
OUTPUT_DIR=~/Downloads

# Run docker and pass the arguments
docker run -v "$OUTPUT_DIR:/root/Downloads" yt-dlp-stream-clip "$YOUTUBE_URL" "$DURATION" "$FORMAT"