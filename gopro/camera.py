#!/usr/bin/env python
# coding: utf8

import requests
import datetime
import json


class Camera(object):
    _status = {}
    _settings = {}

    def __init__(self, ip='10.5.5.9'):
        self._api_url = 'http://' + ip
        
        # Connection Test
        self._test_connection()

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
            return r.json()
        except:
            self.connection = 'Not Connected'
            return {}

    def _test_connection(self):
        if self.ok:
            self.status['connection'] = 'OK'
        else:
            self.status['connection'] = 'Not Connected'

    @property
    def settings(self):
        return self._settings

    @property
    def status(self):
        self.datetime
        self.time_offset
        self.status_screen
        return self._status

    @property        
    def debug(self):
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
    def status_raw(self):
        return self._command_api('/status').get('status')

    @property
    def settings_raw(self):
        return self._command_api('/status').get('settings')

    @property
    def status_screen(self):
        status_screen = {
            -1: 'settings' ,
            0: 'video',
            1: 'photo',
            3: 'timelapse', 
        }
        status_screen = status_screen[self.status_raw.get('12')] 
        self._status['screen'] = status_screen
        return status_screen

    @property
    def commands(self):
        return self._command_api().get('commands')

    @property
    def info(self):
        return self._command_api().get('info')

    @property
    def datetime(self):
        d = []
        for item in self.status_raw.get('40')[1:].split('%'):
            d.append(int(item, 16))
        d = datetime.datetime(d[0] + 2000, d[1], d[2], d[3], d[4], d[5]) 
        self._status['datetime'] = d.isoformat()
        return d

    @property
    def time_offset(self):
        now = datetime.datetime.today()
        gp_time = self.datetime
        if now > gp_time:
            multiplier = 1
            time_offset = now - gp_time
        else:
            multiplier = -1
            time_offset = gp_time - now
        time_offset = time_offset.total_seconds() * multiplier
        self._status['time_offset'] = time_offset
        return time_offset

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
        if not self.status_screen == 'photo':
            self.mode('photo')
        self.capture()

    def video(self):
        if not self.status_screen == 'video':
            self.mode('video')
        self.capture()

    def timelapse(self):
        if not self.status_screen == 'timelapse':
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
    print camera.status_screen