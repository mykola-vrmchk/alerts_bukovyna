from typing import List

import requests
from bs4 import BeautifulSoup, Tag

from telegram_channel_parser.channel_message import ChannelMessage
from telegram_channel_parser.channel_message_getter import (
    ChannelMessageGetter,
)

YOUR_BUKOVYNA_URL = "https://t.me/s/your_Bukovyna"
UESER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/96.0.4664.110 Safari/537.36"
)


class ChannelMessagesParser:
    def __init__(
        self,
        channel_url=YOUR_BUKOVYNA_URL,
        channel_message_getter: ChannelMessageGetter = ChannelMessageGetter(),
    ):
        self._channel_url = channel_url
        self._channel_message_getter = channel_message_getter

    def get_new_messages(self) -> List[ChannelMessage]:
        return [
            self._channel_message_getter.get_channel_message(soup_message_tag)
            for soup_message_tag in self._get_new_soup_message_wrap_tagss()
        ]

    def _get_new_soup_message_wrap_tagss(self) -> List[Tag]:
        soup = self._get_channel_soup()
        return soup.find_all("div", attrs={"class": "tgme_widget_message_wrap"})

    def _get_channel_soup(self):
        return BeautifulSoup(self._get_channel_content(), "html.parser")

    def _get_channel_content(self):
        headers = {"User-Agent": UESER_AGENT}
        response = requests.get(self._channel_url, headers=headers)
        return response.content
