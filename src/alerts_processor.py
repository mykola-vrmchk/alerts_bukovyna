import json
import logging
import os
from dataclasses import asdict
from pathlib import Path
from typing import List

from src.chat_message_sender import ChatMessageSender
from src.message import Message

JSON_ALERTS_LOG_PATH = Path(os.path.abspath(__file__)).parent / "alert_ids_log.json"
log = logging.getLogger(__name__)


class AlertsProcessor:
    def __init__(
            self,
            chat_message_sender: ChatMessageSender = ChatMessageSender(),
            json_alerts_log_path: Path = JSON_ALERTS_LOG_PATH,
    ):
        self._chat_message_sender = chat_message_sender
        self._json_alerts_log_path = json_alerts_log_path
        self._alert_ids_log = self._load_alert_ids_log()

    def process_messages(self, alerts_messages):
        for alert_message in alerts_messages:
            self._process_alert(alert_message)

    def _process_alert(self, alert_message: Message):
        log.info(f"Processing alert {asdict(alert_message)}")
        if self._is_message_processed(alert_message):
            log.info(f"Had been processed earlier")
            return
        status_code = self._chat_message_sender.send(alert_message)
        if status_code != 200:
            log.warning("Message has not been sent")
            raise Exception("message has not been sent")
        self._push_to_alerts_log(alert_message)
        log.info("SENT")

    def _is_message_processed(self, message: Message) -> bool:
        if message.id in self._alert_ids_log:
            return True
        return False

    def _load_alert_ids_log(self) -> List[str]:
        with open(self._json_alerts_log_path, "r") as file:
            return json.load(file)

    def _push_to_alerts_log(self, message: Message):
        self._alert_ids_log.append(message.id)
        with open(self._json_alerts_log_path, "w") as file:
            json.dump(self._alert_ids_log, file)
