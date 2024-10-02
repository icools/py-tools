import sys
import yt_dlp

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '/downloads/%(title)s.%(ext)s',  # 將文件保存到 /downloads 目錄
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python download_audio.py <YouTube_URL>")
        sys.exit(1)
    
    youtube_url = sys.argv[1]
    download_audio(youtube_url)