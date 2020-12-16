# -*- coding: utf-8 -*-
from pip_services3_container import ProcessContainer
from pip_services3_rpc.build.DefaultRpcFactory import DefaultRpcFactory

from pip_services3_facade.build.ClientFacadeFactory import ClientFacadeFactory
from pip_services3_facade.build.FacadeFactory import FacadeFactory
from pip_services3_facade.build.ServiceFacadeFactory import ServiceFacadeFactory

from pip_services3_mongodb.build.DefaultMongoDbFactory import DefaultMongoDbFactory


class FacadeProcess(ProcessContainer):

    def __init__(self):
        super(FacadeProcess, self).__init__("pip-facades-vault", "Public facade for pip-vault 3.0")

        self._factories.add(ClientFacadeFactory)
        self._factories.add(ServiceFacadeFactory)
        self._factories.add(FacadeFactory)
        self._factories.add(DefaultRpcFactory)
        self._factories.add(DefaultMongoDbFactory)
