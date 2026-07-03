import os
import requests

WEBHOOK_URL = os.environ["WEBHOOK_URL"]

message = {
    "content": "🔔 リマインドです！"
}

response = requests.post(WEBHOOK_URL, json=message)

print(response.status_code)
