from dataclasses import dataclass
from datetime import datetime


@dataclass
class ChannelMessage:
    id: str
    datetime: datetime
    text: str
