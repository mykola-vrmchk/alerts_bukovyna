from datetime import datetime

import pytest

from src.alerts_processor import AlertsProcessor
from src.message import Message


@pytest.fixture
def alerts_processor():
    return AlertsProcessor()


# @pytest.mark.skip(reason="did not have proper mocks and assert")
def test_get_new_messages(alerts_processor):
    test_alerts = [
        Message(id="1", text="Test id=1", datetime=datetime.now()),
        Message(id="2", text="Test id=2", datetime=datetime.now()),
        Message(id="3", text="Test id=3", datetime=datetime.now()),
        Message(id="1", text="Test id=1", datetime=datetime.now()),
    ]
    alerts_processor.process_messages(test_alerts)
