import pytest

from src.chat_message_sender import ChatMessageSender
from src.message import Message


@pytest.fixture
def chat_message_sender():
    return ChatMessageSender()


def test_if_message_gets_sent(chat_message_sender):
    assert (
        chat_message_sender.send(
            Message(text="🚨09:57 ПОВІТРЯНА ТРИВОГА.\nЧернівецька область")
        )
        == 200
    )
