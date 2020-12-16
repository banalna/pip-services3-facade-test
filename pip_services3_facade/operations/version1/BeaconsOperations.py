# -*- coding: utf-8 -*-

from pip_services3_commons.refer import Descriptor
from pip_services3_rpc.services import RestOperations

from pip_services3_facade.pip_services3_beacons.clients.version1.BeaconsHttpClientV1 import BeaconsHttpClientV1


class BeaconsOperations(RestOperations):
    _beacons_client: BeaconsHttpClientV1
    _number_of_calls = 0

    def __init__(self):
        super(BeaconsOperations, self).__init__()
        self._dependency_resolver.put('beacons',
                                      Descriptor('beacons', 'client', '*', '*', '1.0'))

    def get_number_of_calls(self):
        return self._number_of_calls

    def increment_number_of_calls(self, req=None, res=None):
        self._number_of_calls += 1

    def set_references(self, references):
        super(BeaconsOperations, self).set_references(references)
        self._beacons_client = self._dependency_resolver.get_one_required('beacons')

    def get_page_by_filter(self):
        correlation_id = self._get_correlation_id()
        filters = self._get_filter_params()
        paging = self._get_paging_params()
        self._send_result(self._beacons_client.get_beacons_by_filter(correlation_id, filters, paging))

    def get_one_by_id(self, id):
        correlation_id = self._get_correlation_id()
        self._send_result(self._beacons_client.get_beacon_by_id(correlation_id, id))

    def create(self):
        correlation_id = self._get_correlation_id()
        entity = self._get_data()
        self._send_created_result(self._beacons_client.create_beacon(correlation_id, entity))

    def update(self, id):
        correlation_id = self._get_correlation_id()
        entity = self._get_data()
        self._send_result(self._beacons_client.update_beacon(correlation_id, entity))

    def delete_by_id(self, id):
        correlation_id = self._get_correlation_id()
        self._beacons_client.delete_beacon_by_id(correlation_id, id)
        self._send_deleted_result()

    def handled_error(self):
        raise Exception('NotSupported', 'Test handled error')

    def unhandled_error(self):
        raise TypeError('Test unhandled error')

    def send_bad_request(self, req, message):
        self._send_bad_request(req, message)
