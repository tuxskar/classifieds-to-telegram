from __future__ import absolute_import, print_function

import sys

from .common import *

try:
    print("Trying import local.py settings...", file=sys.stderr)
    from .local import *
except ImportError:
    pass
