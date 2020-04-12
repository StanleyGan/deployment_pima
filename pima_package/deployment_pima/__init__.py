import os
from deployment_pima.config import config

with open(os.path.join(config.ROOT, 'VERSION')) as version_file:
    __version__ = version_file.read().strip()
