import logging
from typing import List

from src.message import Message

CLUE_PHRASES_FOR_FILTERING = (
    "повітряна тривога",
    "відбій повітряної тривоги",
)
log = logging.getLogger(__name__)


class AlertMessagesFilter:
    def __init__(
        self,
        clue_phrases_for_filtering: List[str] = CLUE_PHRASES_FOR_FILTERING,
        message_len_limit: int = 350,
    ):
        self._clue_phrases_for_filtering = clue_phrases_for_filtering
        self._message_len_limit = message_len_limit

    def filter_messages(self, messages: List[Message]) -> List[Message]:
        alert_messages = [
            message for message in messages if self._is_alert_message(message)
        ]
        log.info(f"Found {len(alert_messages)} alert messages")
        return alert_messages

    def _is_alert_message(self, message: Message) -> bool:
        return self._is_message_not_too_long(
            message
        ) and self._message_contains_filter_phrase(message)

    def _is_message_not_too_long(self, message: Message) -> bool:
        if message.text is None:
            return False
        return len(message.text) < self._message_len_limit

    def _message_contains_filter_phrase(self, message: Message) -> bool:
        if message.text is None:
            return False
        for phrase in self._clue_phrases_for_filtering:
            if phrase in message.text.lower():
                log.info(f"Found alert message {message.text}")
                return True
        return False
