import logging
import time
from functools import wraps # to preserve the original function's metadata when decorating


logger = logging.getLogger(__name__)

def log_step(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        started_at = time.time()
        logger.info("Starting %s", function.__name__)
        result = function(*args, **kwargs)
        ended_at = time.time()
        logger.info(
            "Finished %s in %.2f seconds",
            function.__name__,
            ended_at - started_at,
        )
        return result
    return wrapper