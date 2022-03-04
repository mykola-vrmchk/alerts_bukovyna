from datetime import datetime

from bs4 import Tag

from telegram_channel_parser.channel_message import ChannelMessage


class ChannelMessageGetter:
    def get_channel_message(self, soup_message_wrap_tag: Tag) -> ChannelMessage:
        return ChannelMessage(
            id=self._get_id(soup_message_wrap_tag),
            datetime=self._get_datetime(soup_message_wrap_tag),
            text=self._get_text(soup_message_wrap_tag),
        )

    @staticmethod
    def _get_id(soup_message_wrap_tag: Tag) -> str:
        return soup_message_wrap_tag.find(
            "div", attrs={"class": "tgme_widget_message"}
        ).attrs["data-post"]

    @staticmethod
    def _get_datetime(soup_message_wrap_tag: Tag) -> datetime:
        return datetime.strptime(
            soup_message_wrap_tag.find_all("time")[-1].attrs["datetime"],
            "%Y-%m-%dT%H:%M:%S+00:00",
        )

    @staticmethod
    def _get_text(soup_message_wrap_tag: Tag) -> str:
        text_tag = soup_message_wrap_tag.find(
            "div", attrs={"class": "tgme_widget_message_text"}
        )
        if text_tag is not None:
            return soup_message_wrap_tag.find(
                "div", attrs={"class": "tgme_widget_message_text"}
            ).text
