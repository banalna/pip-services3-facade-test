# -*- coding: utf-8 -*-

import sys

from pip_services3_facade.container.FacadeProcess import FacadeProcess

try:
    FacadeProcess().run()
except Exception as ex:
    sys.stderr.write(str(ex))
