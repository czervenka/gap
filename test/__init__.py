import os
import sys

import src

# Enable included lib files.
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(src.__file__)), 'lib'))
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__))))
