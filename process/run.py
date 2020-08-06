# -*- coding: utf-8 -*-

import sys

from src.container.FacadeProcess import FacadeProcess

try:
    FacadeProcess().run()
except Exception as ex:
    sys.stderr.write(str(ex))
