# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from pip_services3_commons.config.ConfigParams import ConfigParams
from pip_services3_commons.refer.Descriptor import Descriptor
from pip_services3_components.build.CompositeFactory import CompositeFactory
from pip_services3_container.refer.ManagedReferences import ManagedReferences
from pip_services3_rpc.build import DefaultRpcFactory

from src.build.ClientFacadeFactory import ClientFacadeFactory
from src.build.ServiceFacadeFactory import ServiceFacadeFactory
from src.services.version1.FacadeServiceV1 import FacadeServiceV1


class ReferencesTest(ManagedReferences):
    _factory = CompositeFactory()

    def __init__(self):
        super(ReferencesTest, self).__init__()

        self._setup_factoriest()
        self._append_dependencies()
        self._configure_service()
        self.create_user_and_sessions()

    def _setup_factoriest(self):
        self._factory.add(ClientFacadeFactory())
        self._factory.add(ServiceFacadeFactory())
        self._factory.add(DefaultRpcFactory())

    def append(self, descriptor):
        component = self._factory.create(descriptor)
        self.put(descriptor, component)

    def _append_dependencies(self):
        # Add factories
        self.put(None, self._factory)

        # Add service
        self.put(None, FacadeServiceV1())

        # Add services
        self.append(Descriptor('beacons', 'client', 'direct', '*', '1.0'))

    def _configure_service(self):
        # Configure Facade service
        service = self.get_one_required(Descriptor('pip-services', 'endpoint', 'http', 'default', '*'))

        service.configure(ConfigParams.from_tuples(
            'root_path', '/api/1.0',
            'connection.protocol', 'http',
            'connection.host', '0.0.0.0',
            'connection.port', 3000
        ))

    def create_user_and_sessions(self):
        # TODO
        pass
