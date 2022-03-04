from datetime import datetime

import pytest
from bs4 import BeautifulSoup

from telegram_channel_parser import ChannelMessage
from telegram_channel_parser.channel_message_getter import ChannelMessageGetter


message_wrap_tag = "\n".join(
    [
        '<div class="tgme_widget_message_wrap js-widget_message_wrap"><div class="tgme_widget_message js-widget_message" data-post="your_Bukovyna/5179" data-view="eyJjIjotMTE3MjUwMjAyMCwicCI6NTE3OSwidCI6MTY0NjQwMTYzMiwiaCI6ImVkZTY3MGZmMjI4ZGIyYjc4MCJ9">',
        '<div class="tgme_widget_message_user"><a href="https://t.me/your_Bukovyna"><i class="tgme_widget_message_user_photo bgcolor4" data-content="Т"><img src="https://cdn4.telesco.pe/file/As3qZDfA85sXIdd_AQfHb_tIV452IKQ5ALmMpAv7AdoLpCfXDP1bE-Xb3AsNy57f4LekaCSzVANv0y_Z8Ie-YeKqBBU0pddrHNZcOxRTa97aaOjcRz2dDOH-mJe_x1dV-jEIfj6OwPgvultZGinPbs7gAkgq_q1YQPRGczi3jdJhBoIkluIBj5-FYB_lGvjkLvWnMwu8wnknncbLRTUMVJjoJHoibu1EvqauFw-71Z1ldn-Io-k8_uXj34svfAfrU7KiauogtdE6qiKNB7l1Fn2PvgFOMfbEbdnlnqmbmQ8Bkc4rrAGqGoZptMo3pj8ifJFBEih3W-iBn3tTKr8wkg.jpg"></i></a></div>',
        '<div class="tgme_widget_message_bubble">',
        "",
        '<i class="tgme_widget_message_bubble_tail">',
        '<svg class="bubble_icon" width="9px" height="20px" viewBox="0 0 9 20">',
        "</svg>",
        "</i>",
        '<div class="tgme_widget_message_text js-message_text before_footer" dir="auto">ТРИВОГА<span style="display: inline-block; width: 97px;"></span></div>',
        "",
        '<div class="tgme_widget_message_footer compact js-message_footer">',
        "",
        '<div class="tgme_widget_message_info short js-message_info">',
        '<span class="tgme_widget_message_views">33.0K</span><span class="copyonly"> views</span><span class="tgme_widget_message_meta"><a class="tgme_widget_message_date" href="https://t.me/your_Bukovyna/5179"><time datetime="2022-03-04T06:01:49+00:00" class="time">08:01</time></a></span>',
        "</div>",
        "</div>",
        "</div>",
        "",
        '</div><div class="tgme_widget_message_service_date_wrap"><div class="tgme_widget_message_service_date">March 4</div></div></div>',
    ]
)


@pytest.fixture
def channel_message_getter():
    return ChannelMessageGetter()


@pytest.fixture
def soup_message_wrap_tag():
    return BeautifulSoup(message_wrap_tag, "html.parser")


def test_if_returns_channel_message_with_properly_parsed_fields(
    channel_message_getter, soup_message_wrap_tag
):
    assert channel_message_getter.get_channel_message(
        soup_message_wrap_tag
    ) == ChannelMessage(
        id="your_Bukovyna/5179",
        datetime=datetime(2022, 3, 4, 6, 1, 49),
        text="ТРИВОГА",
    )
