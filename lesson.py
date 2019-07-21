import loggin.config

logging.config.fileConfig('logging.oini')
logger = logging.getLogger(__name__)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.critival('critival message')
