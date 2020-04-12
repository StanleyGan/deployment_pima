import os
import logging

from deployment_pima.config import config
from deployment_pima.config import logging_config

# Logger for this package
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_config.get_console_handler())
logger.propagate= False

with open(os.path.join(config.ROOT, 'VERSION')) as version_file:
    __version__ = version_file.read().strip()
