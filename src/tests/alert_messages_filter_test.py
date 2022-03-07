import pytest

from src.alert_messages_filter import AlertMessagesFilter
from src.message import Message


@pytest.fixture
def alert_messages_filter():
    return AlertMessagesFilter()


def test_if_alert_messages_gets_filtered_by_phrases(alert_messages_filter):
    messages = [
        Message(id="1", text="asdfkasd;kf;lasdkfПоВіТрЯнА ТрИвоГаdfkasdjfjkasdhjfkjl"),
        Message(id="2", text="фів"),
        Message(id="3", text="Відбій Повітряної Тривоги"),
    ]
    filtered_messages = alert_messages_filter.filter_messages(messages)
    assert len(filtered_messages) == 2 and {
        message.id for message in filtered_messages
    } == {"1", "3"}


def test_if_too_long_messages_gets_filtered(alert_messages_filter):
    messages = [
        Message(
            id="3",
            text="Відбій Повітряної Тривоги Повітряної Тривоги Повітряної Тривоги ПоВіТрЯнА ТрИвоГ"
                 "аПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГа"
                 "аПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГа"
                 "аПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГа"
                 "аПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГаПоВіТрЯнА ТрИвоГа",
        ),
    ]
    filtered_messages = alert_messages_filter.filter_messages(messages)
    assert len(filtered_messages) == 0
