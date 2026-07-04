# 環境変数を取得するためのライブラリ
import os

# DiscordへHTTPリクエストを送るためのライブラリ
import requests

# 日時を扱うライブラリ
from datetime import datetime, timedelta, timezone

# GitHub Secretsに登録したWebhook URLを取得
WEBHOOK_URL = os.environ["WEBHOOK_URL"]

# メンションしたいユーザーID
USER_ID = "1097404022228525137"

# 日本時間(JST = UTC+9)を設定
jst = timezone(timedelta(hours=9))

# 現在の日本時間を取得
now = datetime.now(jst)

# 現在時刻を「08:50」のような文字列に変換
current = now.strftime("%H:%M")

# 時間ごとの通知メッセージ
messages = {
    "08:50": "1限開始10分前",
    "10:40": "2限開始10分前",
    "12:46": "3限開始10分前",
    "15:00": "4限開始10分前",
    "16:50": "さっさと帰れ～",
    "19:00": "晩御飯の時間",
    "23:00": "なんと、もう11時",
    "00:00": "さっさと寝ろ～"
}

# 現在時刻に対応するメッセージがあれば送信
if current in messages:

    message = {
        "content": f"<@{USER_ID}> 🔔 {messages[current]}",
        "allowed_mentions": {
            "users": [USER_ID]
        }
    }

    response = requests.post(WEBHOOK_URL, json=message)

    print(response.status_code)
