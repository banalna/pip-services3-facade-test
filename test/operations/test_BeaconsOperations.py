# -*- coding: utf-8 -*-
from pip_services3_commons.run import Parameters

from pip_services3_facade.pip_services3_beacons.data.version1 import BeaconV1, BeaconTypeV1

from test.fixtures.TestRefernces import ReferencesTest
from test.fixtures.RestClientTest import RestClientTest

BEACON1 = BeaconV1("1", "1", BeaconTypeV1.AltBeacon, "00001", "TestBeacon1",
                   {"type": 'Point', "coordinates": [0, 0]}, 50)

BEACON2 = BeaconV1("2", "1", BeaconTypeV1.iBeacon, "00002", "TestBeacon2",
                   {"type": 'Point', "coordinates": [2, 2]}, 70)

BEACON3 = BeaconV1("3", "2", BeaconTypeV1.AltBeacon, "00003", "TestBeacon3",
                   {"type": 'Point', "coordinates": [10, 10]}, 50)


class TestBeaconsOperationsV1:

    references = None
    rest = None

    @classmethod
    def setup_class(cls):
        cls.rest = RestClientTest()
        cls.references = ReferencesTest()
        cls.references.open(None)

    @classmethod
    def teardown_class(cls):
        cls.references.close(None)

    def test_beacons_operations(self):
        # create one beacon
        beacon1 = self.rest.post('/api/1.0/beacons/create_beacon', Parameters.from_tuples("beacon", BEACON1))
        assert beacon1 is not None
        # TODO
