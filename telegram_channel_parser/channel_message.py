from dataclasses import dataclass
from datetime import datetime


@dataclass
class ChannelMessage:
    id: str = None
    datetime: datetime = None
    text: str = None
