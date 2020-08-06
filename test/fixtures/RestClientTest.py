# -*- coding: utf-8 -*-

import http.client
import requests


class RestClientTest:
    _rest = None
    headers = {'Content-type': 'application/json'}
    url = 'http://localhost:3000'

    def __init__(self):
        self._rest = requests.Session()

    def get(self, path):
        response = self._rest.request('GET', self.url + path, headers=self.headers)
        return response

    def head(self, path):
        response = self._rest.request('HEAD', self.url + path, headers=self.headers)
        return response

    def post(self, path, params):
        response = self._rest.request('POST', self.url + path, json=params, headers=self.headers)
        return response

    def put(self, path, params):
        response = self._rest.request('PUT', self.url + path, json=params, headers=self.headers)
        return response

    def delete(self, path, params):
        response = self._rest.request('DELETE', self.url + path, json=params, headers=self.headers)
        return response

    # TODO
    # def get_as_user(self, session_id, path):
    #     self.headers.update({'x-session-id': session_id})
    #     self._rest.request('GET', path, headers=self.headers)
    #     return self._rest.getresponse()
    #
    # def head_as_user(self, session_id, path):
    #     self.headers.update({'x-session-id': session_id})
    #     self._rest.request('HEAD', path, headers=self.headers)
    #     return self._rest.getresponse()
    #
    # def post_as_user(self, session_id, path, params):
    #     self.headers.update({'x-session-id': session_id})
    #     self._rest.request('POST', path, body=params, headers=self.headers)
    #     return self._rest.getresponse()
    #
    # def put_as_user(self, session_id, path, params):
    #     self.headers.update({'x-session-id': session_id})
    #     self._rest.request('PUT', path, body=params, headers=self.headers)
    #     return self._rest.getresponse()
    #
    # def delete_as_user(self, session_id, path, params):
    #     self.headers.update({'x-session-id': session_id})
    #     self._rest.request('DELETE', path, body=params, headers=self.headers)
    #     return self._rest.getresponse()
