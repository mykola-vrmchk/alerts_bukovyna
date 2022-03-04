from copy import copy

import requests

from config import BOT_TOKEN, ALERT_CHANNEL_ID
from src.message import Message


class ChatMessageSender:
    def __init__(self, bot_token: str = BOT_TOKEN, chat_id: str = ALERT_CHANNEL_ID):
        self._chat_id = chat_id
        self._url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        self._base_payload = {
            "chat_id": chat_id,
        }

    def send(self, message: Message) -> int:
        payload = copy(self._base_payload)
        payload["text"] = message.text
        response = requests.post(self._url, json=payload)
        return response.status_code
