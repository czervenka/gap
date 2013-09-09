import os
import sys

import src

# Include test sources
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
# Include src sources
sys.path.insert(0, os.path.abspath(os.path.dirname(src.__file__)))
# Include lib sources
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(src.__file__)), 'lib'))
