import sys
from logging import Logger, getLogger, StreamHandler, Formatter, INFO

class LoggerFactory:
    @staticmethod
    def get_logger(name: str) -> Logger:
        logger: Logger = getLogger(name)

        if not logger.handlers:
            logger.setLevel(INFO)
            handler: StreamHandler = StreamHandler(sys.stdout)
            handler.setLevel(INFO)
            formatter: Formatter = Formatter(
                "[%(asctime)s][%(name)s][%(filename)s:%(lineno)d][%(funcName)s][%(levelname)s]: %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        return logger