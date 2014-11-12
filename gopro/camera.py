#!/usr/bin/env python
# coding: utf8

import requests
import time


class Camera(object):
    def __init__(self, ip='10.5.5.9'):
        self._api_url = 'http://' + ip
        
        # Connection Test
        self.connection = self._test()

    def __repr__(self):
        return '<GoPro Camera [{0}]>'.format(self.connection)

    def _command_api(self, method='', params=''):
        if params:
            params = {'p': params}
        url = self._api_url + '/gp/gpControl' + method
        return self._api_call(url, params)

    def _api_call(self, url, params):
        try:
            r = requests.get(url, timeout=5.0, params=params)
            self.connection = 'OK'
            return r.content.json()
        except:
            self.connection = 'Not Connected'
            return {}

    def _test(self):
        ok = self.ok
        if ok:
            return 'OK'
        else:
            return 'Not Connected'
            
    def _debug(self):
        content = self._command_api()
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
    def ok(self):
        if self.status:
            return True
        else:
            return False

    @property
    def status(self):
        return self._command_api().get('status')

    @property
    def commands(self):
        return self._command_api().get('commands')

    @property
    def info(self):
        return self._command_api().get('info')

    #def silence(self):
    #    return self._command_api()

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
