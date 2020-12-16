# -*- coding: utf-8 -*-

from pip_services3_facade.container.FacadeProcess import FacadeProcess


try:
    FacadeProcess().run()
except Exception as ex:
    raise ex
