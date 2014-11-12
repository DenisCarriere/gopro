#!/usr/bin/env python
# coding: utf8

import requests
import time


class Camera(object):
    def __init__(self, ip='10.5.5.9'):
        self._api_url = 'http://' + ip

    def _command_api(self, method, params=''):
        if params:
            params = {'p': params}
        url = self._api_url + '/gp/gpControl' + method
        return self._api_call(url, params)

    def _api_call(self, url, params):
        r = requests.get(url, params=params)
        return r.content

    def _debug(self):
        r = requests.get('http://10.5.5.9/gp/gpControl')
        content = r.json()
        sections = [
            'status',
            'info',
            'commands',
            'modes',
            'display_hints',
            'version',
            'filters',
            'services',
        ]
        return content

    @property
    def commands(self):
        return _debug()['commands']

    @property
    def info(self):
        return _debug()['info']

    def silence(self):
        return self._command_api()

    def capture(self):
        return self._command_api('/command/shutter', '1')

    def mode(self, method):
        xmode = {
            'video': '0',
            'photo': '1',
            'burst': '2',
            'timelapse': '3',
        }
        method = method.lower()
        if method in xmode:
            method = xmode[method]
        return self._command_api('/command/xmode', method)

    def burst(self):
        self.mode('burst')
        self.capture()

    def photo(self):
        self.mode('photo')
        self.capture()

    def video(self):
        self.mode('video')
        self.capture()

    def timelapse(self):
        self.mode('timelapse')
        self.capture()

    def delete_all(self):
        return self._command_api('/command/storage/delete/all')

    def delete_last(self):
        return self._command_api('/command/storage/delete/last')

    def sleep(self):
        return self._command_api('/command/system/sleep')

    def locate(self, method='on'):
        status = {
            'on': '1',
            'off': '0',
        }
        method = method.lower()
        if method in status:
            method = status[method]
        return self._command_api('/command/system/locate', method)

    def factory_reset(self):
        return self._command_api('/command/system/factory/reset')

if __name__ == '__main__':
    camera = Camera()
    camera.photo()

    #camera._debug()
    #camera.sleep()
    #camera.mode('photo')