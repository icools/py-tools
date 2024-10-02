# Py-Dl

> 只有這邊是我自己寫的，可以用來於docker跑下載yt影片到Downloa/下成一個mp3檔案用途，可以拿來跑wishper轉成字幕檔

Download MP3 files from YouTube for use Whisper-Transcriptor to generate SRT files. It can runs in docker.

要確保 `yt-dlp` 只下載音頻而不是整個影片，需要使用正確的參數。你之前提到的情況可能是因為缺少了一些必要的選項。

### 修改 `yt-dlp` 命令來只下載音頻

為了確保 `yt-dlp` 僅下載音頻，並且將其轉換為 MP3，應該使用以下參數：

1. **`-x`**：只提取音頻。
2. **`--audio-format mp3`**：將音頻轉換為 MP3 格式。
3. **`--audio-quality 0`**（可選）：指定最高質量的音頻（可根據需求調整）。

### 完整的 Dockerfile 範例

確保 Dockerfile 正確配置並且只下載音頻，這是你可以使用的最終 Dockerfile：

```Dockerfile
# 使用 Python 的官方輕量映像作為基礎
FROM python:3.10-slim

# 安裝 ffmpeg 和 yt-dlp
RUN apt-get update && apt-get install -y ffmpeg \
    && pip install --no-cache-dir yt-dlp \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 創建一個下載目錄
RUN mkdir -p /downloads

# 設置工作目錄
WORKDIR /downloads

# 設置默認入口點為 yt-dlp
ENTRYPOINT ["yt-dlp"]

# 默認只提取音頻並轉換為 mp3 格式
CMD ["-x", "--audio-format", "mp3", "--audio-quality", "0"]
```

### 構建 Docker 映像

使用下面的命令構建你的映像，這裡的名稱已改為 `yt-dlp-python`：

```bash
docker build -t yt-dlp-python .
```

### 運行 Docker 容器並下載音頻

執行以下命令來下載音頻並轉換為 MP3 格式，文件將會存儲在你的本地 `Downloads` 文件夾中：

```bash
docker run --rm -v ~/Downloads:/downloads yt-dlp-docker "https://www.youtube.com/watch?v=c0p8Srdau5s&ab_channel=Huan"
```

### 確認音頻下載

使用 `ls` 命令檢查下載的 MP3 文件是否正確保存到 `~/Downloads` 目錄：

```bash
ls ~/Downloads/
```

### 總結：
- **`-x`**：確保只提取音頻而不是整個影片。
- **`--audio-format mp3`**：將音頻轉換為 MP3 格式。
- **`--audio-quality 0`**：選擇最高質量的音頻（可選）。
