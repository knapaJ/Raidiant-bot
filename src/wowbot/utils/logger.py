import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("wowbot")
logger.setLevel(logging.DEBUG)  # Logger for the app to use

logging.getLogger("discord").setLevel(logging.WARNING)

