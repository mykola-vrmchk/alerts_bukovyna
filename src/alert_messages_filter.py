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
        self, clue_phrases_for_filtering: List[str] = CLUE_PHRASES_FOR_FILTERING
    ):
        self._clue_phrases_for_filtering = clue_phrases_for_filtering

    def filter_messages(self, messages: List[Message]) -> List[Message]:
        alert_messages = [
            message
            for message in messages
            if self._message_contains_filter_phrase(message)
        ]
        log.info(f"Found {len(alert_messages)} messages with clue alert phrases")
        return alert_messages

    def _message_contains_filter_phrase(self, message: Message) -> bool:
        if message.text is None:
            return False
        for phrase in self._clue_phrases_for_filtering:
            if phrase in message.text.lower():
                log.info(f"Found alert message {message.text}")
                return True
        return False
