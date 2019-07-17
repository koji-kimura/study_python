import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)

logging.critical('critical')
logging.error('error')
logging.debug('debug')
logging.info('info')
logging.debug('debug')

logging.info('info{}'.format('test'))
logging.info('info %s %s', 'test1', 'test2')
