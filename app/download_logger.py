import logging

logger = logging.getLogger("uvicorn.error")

class DownloadLogger(object):

    def debug(self, msg):
        logger.debug(msg)

    def warning(self, msg):
        logger.warning(msg)

    def error(self, msg):
        logger.warning(msg)