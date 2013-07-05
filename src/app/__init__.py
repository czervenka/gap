__all__ = ['prepare_environment']
import sys
from os.path import dirname, join

def prepare_environment():
    sys.path.insert(0, join(dirname(dirname(__file__)), 'lib'))

prepare_environment()
