import traceback

try:
    raise Exception("This is an Error")
except Exception as err:
    with open('error.txt', 'w') as f:
        f.write(traceback.format_exc())

name  = 'harshith'
assert name == 'harshith'

try:
    assert name == 'one', 'oe'
except Exception as e:
    print(e)


import logging

logging.basicConfig(filename='log.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('This is a debug message')
logging.info('This is a info message')
logging.warning('This is a warning message')
logging.error('This is a error message')
logging.critical('This is a critical message')