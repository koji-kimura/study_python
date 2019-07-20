import logging
import logtest

# formatter = '%(levelname)s:%(message)s'
formatter = '%(asctime)s:%(message)s'
logging.basicConfig(level=logging.INFO)


class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message


logging.info('info')
logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())

logger.info('from main')
logger.info('from main password="test"')
logger.info('from main passwod="test"')
# logger.setLevel(logging.DEBUG)
# logtest.do_something()
