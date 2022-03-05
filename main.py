import logging
import sys
import time
import traceback
from random import random

from src.alert_messages_filter import AlertMessagesFilter
from src.alerts_processor import AlertsProcessor
from src.channel_messages_parser import ChannelMessagesParser


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

log = logging.getLogger(__name__)


def wait_15_sec():
    log.info("Sleeping 15 seconds")
    time.sleep(9.73 + random() * 10)


def main():
    while True:
        try:
            new_messages = ChannelMessagesParser().get_new_messages()
            alerts_messages = AlertMessagesFilter().filter_messages(new_messages)
            AlertsProcessor().process_messages(alerts_messages)
            wait_15_sec()
        except Exception as error:

            log.error(traceback.format_exc())
            log.error(str(error))


if __name__ == "__main__":
    main()
