import logging
from typing import List

import requests
from bs4 import BeautifulSoup, Tag

from src.bs_message_getter import BSMessageGetter
from src.message import Message

YOUR_BUKOVYNA_URL = "https://t.me/s/your_Bukovyna"
UESER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/96.0.4664.110 Safari/537.36"
)
log = logging.getLogger(__name__)


class ChannelMessagesParser:
    def __init__(
        self,
        channel_url: str = YOUR_BUKOVYNA_URL,
        timeout: int = 10,
        bs_message_getter: BSMessageGetter = BSMessageGetter(),
    ):
        self._channel_url = channel_url
        self._timeout = timeout
        self._bs_message_getter = bs_message_getter

    def get_new_messages(self) -> List[Message]:
        return [
            self._bs_message_getter.get_message(soup_message_tag)
            for soup_message_tag in self._get_new_soup_message_wrap_tags()
        ]

    def _get_new_soup_message_wrap_tags(self) -> List[Tag]:
        soup = self._get_channel_soup()
        soup_message_wrap_tags = soup.find_all(
            "div", attrs={"class": "tgme_widget_message_wrap"}
        )
        log.info(
            f"Parsed {len(soup_message_wrap_tags)} latest messages from {self._channel_url}"
        )
        return soup_message_wrap_tags

    def _get_channel_soup(self):
        return BeautifulSoup(self._get_channel_content(), "html.parser")

    def _get_channel_content(self):
        headers = {"User-Agent": UESER_AGENT}
        response = requests.get(
            self._channel_url, timeout=self._timeout, headers=headers
        )
        return response.content
