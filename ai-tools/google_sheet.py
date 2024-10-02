# google_sheet.py
import requests
import time
import os

def log_to_google_sheet(message):
    log_to_google_sheet_with(
        sheet_id = os.getenv("GOOGLE_SHEET_ID"),
        cookie = os.getenv("GOOGLE_SHEET_COOKIE"), 
        fbzx = os.getenv("GOOGLE_SHEET_FBZX"),
        message = message
    )

def log_to_google_sheet_with(sheet_id,cookie,fbzx,message):
    url = f'https://docs.google.com/forms/d/e/{sheet_id}/formResponse'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-TW,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie,
        'dnt': '1',
        'origin': 'https://docs.google.com',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '64',
        'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.138", "Not;A=Brand";v="24.0.0.0", "Google Chrome";v="128.0.6613.138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"macOS"',
        'sec-ch-ua-platform-version': '"11.7.10"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }
    data = {
        'entry.541674348': message,
        'fvv': '1',
        'partialResponse': f'[null,null,"{fbzx}"]',
        'pageHistory': '0',
        'fbzx': fbzx,
        'submissionTimestamp': str(int(time.time() * 1000))  # 動態生成時間戳
    }
    
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print("Successfully logged to Google Sheet")
    else:
        print(f"Failed to log to Google Sheet: {response.status_code}")