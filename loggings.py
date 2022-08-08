import logging

logger = logging.getLogger(__name__)
logger = logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(created)f:%(filename)s')
file_handler = logging.FileHandler('test.log')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)