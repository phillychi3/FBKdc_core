import logging
from .client import *


FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logging.getLogger(__name__).addHandler(logging.NullHandler())