import pytest

from src.channel_messages_parser import ChannelMessagesParser


@pytest.fixture
def channel_messages_parser():
    return ChannelMessagesParser()


@pytest.mark.skip(reason="did not have proper mocks and assert")
def test_get_new_messages(channel_messages_parser):
    assert channel_messages_parser.get_new_messages() == 0
