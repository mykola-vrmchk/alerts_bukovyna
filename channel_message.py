from dataclasses import dataclass
from datetime import datetime


@dataclass
class ChannelMessage:
    id: str
    date: datetime
    text: str
