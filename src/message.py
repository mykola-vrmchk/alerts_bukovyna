from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    id: str = None
    datetime: datetime = None
    text: str = None
