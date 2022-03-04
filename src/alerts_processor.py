import json
import logging
import os
from dataclasses import asdict
from pathlib import Path
from typing import Set

from src.message import Message
from src.chat_message_sender import ChatMessageSender

JSON_ALERTS_LOG_PATH = Path(os.path.abspath(__file__)).parent / "alerts_log.json"
log = logging.getLogger(__name__)


class AlertsProcessor:
    def __init__(
        self,
        chat_message_sender: ChatMessageSender = ChatMessageSender(),
        json_alerts_log_path: Path = JSON_ALERTS_LOG_PATH,
    ):
        self._chat_message_sender = chat_message_sender
        self._json_alerts_log_path = json_alerts_log_path
        self._alerts_log = self._load_alerts_log()

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
        self._update_alerts_log({asdict(alert_message)})
        log.info("SENT")

    def _is_message_processed(self, message: Message) -> bool:
        if message.id in self._get_processed_alert_ids():
            return True
        return False

    def _get_processed_alert_ids(self):
        return [alert_dict["id"] for alert_dict in self._alerts_log]

    def _load_alerts_log(self) -> Set[dict]:
        with open(self._json_alerts_log_path, "r") as file:
            return set(json.load(file))

    def _update_alerts_log(self, new_alerts: Set[dict]):
        all_alerts = self._alerts_log.union(new_alerts)
        self._alerts_log = all_alerts
        with open(self._json_alerts_log_path, "w") as file:
            json.dump(list(all_alerts), file)
