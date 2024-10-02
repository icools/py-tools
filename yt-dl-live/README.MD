# YT-DLP

can download YT live, and set time and file type (mp3 | mp4), sure u can use docker to run this.


# Mp3
```
docker run -v ~/Downloads:/root/Downloads yt-dlp-stream-clip "https://www.youtube.com/watch?v=DYHVnc0kRWE&ab_channel=%E5%8F%B0%E7%81%A3%E9%A2%B1%E9%A2%A8%E8%AB%96%E5%A3%87" 10 mp3
```

# Mp4
```
docker run -v ~/Downloads:/root/Downloads yt-dlp-stream-clip "https://www.youtube.com/watch?v=DYHVnc0kRWE&ab_channel=%E5%8F%B0%E7%81%A3%E9%A2%B1%E9%A2%A8%E8%AB%96%E5%A3%87" 10 mp4
```