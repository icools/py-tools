import subprocess
import sys
import os
import re
import unicodedata

def download_stream_clip(url, duration, format_type):
    """
    使用 yt-dlp 和 ffmpeg 從直播下載指定秒數的片段，並下載到 ~/Downloads/。
    可以指定下載格式為 mp4 或 mp3，並移除檔案名稱中的特殊字元。

    :param url: 直播的網址
    :param duration: 下載的秒數
    :param format_type: 下載格式 (mp4 或 mp3)
    """
    try:
        # 獲取下載目錄
        download_dir = os.path.expanduser('~/Downloads/')

        # 使用 yt-dlp 抓取影片標題
        title_command = [
            'yt-dlp',
            '--get-title',
            url
        ]
        title = subprocess.check_output(title_command).decode().strip()

        # 標準化檔名，移除特殊字元，避免檔案系統問題
        safe_title = unicodedata.normalize('NFKD', title)
        safe_title = re.sub(r'[\\/*?:"<>|]', "", safe_title).replace(" ", "_")

        # 根據 format_type 決定輸出文件格式
        if format_type == 'mp3':
            output_filename = f"{safe_title}.mp3"
        else:
            output_filename = f"{safe_title}.mp4"
            
        output_path = os.path.join(download_dir, output_filename)

        # 使用 yt-dlp 抓取直播的 m3u8 串流地址
        command = [
            'yt-dlp',
            '--no-part',  # 避免產生部分下載文件
            '-g',         # 只取得串流的 URL
            url
        ]
        stream_url = subprocess.check_output(command).decode().strip()

        # 使用 ffmpeg 根據格式下載指定時間的直播片段
        if format_type == 'mp3':
            ffmpeg_command = [
                'ffmpeg',
                '-i', stream_url,   # 串流的來源 URL
                '-t', str(duration), # 指定下載的秒數
                '-q:a', '0',         # 保持高音質
                '-vn',               # 只抓取音訊
                output_path          # 保存文件的完整路徑
            ]
        else:
            ffmpeg_command = [
                'ffmpeg',
                '-i', stream_url,   # 串流的來源 URL
                '-t', str(duration), # 指定下載的秒數
                '-c', 'copy',        # 直接複製，避免重新編碼
                output_path          # 保存文件的完整路徑
            ]
        
        subprocess.run(ffmpeg_command, check=True)

        print(f"下載完成，已保存到 {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"發生錯誤: {e}")

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("請提供 URL、秒數 和 格式 (mp4 或 mp3)")
        sys.exit(1)

    url = sys.argv[1]
    duration = int(sys.argv[2])
    format_type = sys.argv[3]

    download_stream_clip(url, duration, format_type)