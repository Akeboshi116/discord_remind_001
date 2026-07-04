# 環境変数を取得するためのライブラリ
import os

# DiscordへHTTPリクエストを送るためのライブラリ
import requests

# 日時を扱うライブラリ
from datetime import datetime, timedelta, timezone

# GitHub Secretsに登録したWebhook URLを取得
WEBHOOK_URL = os.environ["WEBHOOK_URL"]

# 日本時間(JST = UTC+9)を設定
jst = timezone(timedelta(hours=9))

# 現在の日本時間を取得
now = datetime.now(jst)

# 現在時刻を「08:50」のような文字列に変換
current = now.strftime("%H:%M")

# 時間ごとの通知メッセージ
messages = {
    "08:50": "1限開始10分前 @akeboshi1106",
    "10:40": "2限開始10分前 @akeboshi1106",
    "13:10": "3限開始10分前 @akeboshi1106",
    "15:00": "4限開始10分前 @akeboshi1106",
    "16:50": "さっさと帰れ～ @akeboshi1106",
    "19:00": "晩御飯の時間 @akeboshi1106",
    "23:00": "なんと、もう11時 @akeboshi1106",
    "00:00": "さっさと寝ろ～ @akeboshi1106"
}

# 現在時刻が辞書に登録されている場合のみ通知する
if current in messages:

    # Discordへ送信する内容
    message = {
        "content": messages[current]
    }

    # WebhookへPOSTして通知を送信
    response = requests.post(WEBHOOK_URL, json=message)

    # 成功したか確認（200系なら成功）
    print(response.status_code)
