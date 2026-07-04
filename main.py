# 環境変数を取得するためのライブラリ
import os

# DiscordへHTTPリクエストを送るためのライブラリ
import requests

# GitHub Secretsに登録したWebhook URLを取得
WEBHOOK_URL = os.environ["WEBHOOK_URL"]

# GitHub Actionsから渡されたメッセージを取得
MESSAGE = os.environ["MESSAGE"]

# メンションしたいユーザーID
USER_ID = "1097404022228525137"

# Discordへ送信する内容を作成
message = {
    # ユーザーをメンションしてメッセージを送信
    "content": f"<@{USER_ID}> 🔔 {MESSAGE}",

    # 指定したユーザーへのメンションを有効にする
    "allowed_mentions": {
        "users": [USER_ID]
    }
}

# Discord Webhookへ通知を送信
response = requests.post(
    WEBHOOK_URL,
    json=message
)

# ステータスコードを表示
# 204なら送信成功
print(f"Status Code: {response.status_code}")

# エラーが発生した場合は内容も表示
if response.status_code != 204:
    print(response.text)
