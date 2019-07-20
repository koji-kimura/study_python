import logging
import logtest

# formatter = '%(levelname)s:%(message)s'
formatter = '%(asctime)s:%(message)s'
logging.basicConfig(level=logging.INFO)
logging.info('info')
logger = logging.getLogger(__name__)
logger.info('from main')
# logger.setLevel(logging.DEBUG)
logtest.do_something()
