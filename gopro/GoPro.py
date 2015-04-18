#!/usr/bin/env python
# coding: utf8

import requests
import humanize
import datetime
import json
import re
from media import Media


class GoPro(object):
    _status = {}
    _media = []
    _settings = {}

    def __init__(self, ip='10.5.5.9'):
        self._status['ip'] = ip
        self._api_url = 'http://' + ip
        self._media_url = self._api_url + '/videos/DCIM/100GOPRO/'
        
        # Connection Test
        self.status_connection

    def __repr__(self):
        return '<GoPro Camera [{0}]>'.format(self.connection)

    def __iter__(self):
        for item in self.media:
            yield item

    def __getitem__(self, item):
        return self.media[item]


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

    @property
    def settings(self):
        return self._settings

    @property
    def status(self):
        self.datetime
        self.time_offset
        self.status_screen
        self.status_storage
        return self._status
     
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
        for section in sections:
            print section
            print '-------'
            print '======='
            print content[section]

    @property
    def photos(self):
        pass

    @property
    def media(self):
        r = requests.get(self._media_url)
        expression = r'"(\w+.JPG)"'
        pattern = re.compile(expression)
        self._media = []
        for item in re.findall(pattern, r.content):
            item_url = self._media_url + item
            self._media.append(Media(item_url))
        return self._media

    @property
    def ok(self):
        if self.connection == 'OK':
            self._status['ok'] = True
            return True
        else:
            self._status['ok'] = False
            return False

    @property
    def status_raw(self):
        return self._command_api('/status').get('status')

    @property
    def settings_raw(self):
        return self._command_api('/status').get('settings')

    @property
    def status_connection(self):
        # Connecting is retrieved from making an API call
        self._command_api('/status')
        self.status['connection'] = self.connection
        return self.connection

    @property
    def status_screen(self):
        if self.ok:
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
    def status_storage(self):
        # Filesize in KB
        if self.ok:
            storage = self.status_raw.get('54')
	    if storage is not None:
	            self._status['storage'] = humanize.naturalsize(storage * 1000)
            return storage

    """
    @property
    def status_current_photo(self):
        # The Current photo status, +1 for the next
        return self.status_raw.get('38')


    @property
    def status_current_video(self):
        return self.status_raw.get('38')


    @property
    def status_busy(self):
        status = self.status_raw
        status.get('8') # 0 is Free, 1 Busy
        status.get('10') # 0 is Free, 1 Busy
        status.get('55') # 1 is Free, 0 Busy
        return 
    """

    @property
    def commands(self):
        return self._command_api().get('commands')

    @property
    def info(self):
        return self._command_api().get('info')

    @property
    def datetime(self):
        if self.ok:
            d = []
            for item in self.status_raw.get('40')[1:].split('%'):
                d.append(int(item, 16))
            d = datetime.datetime(d[0] + 2000, d[1], d[2], d[3], d[4], d[5]) 
            self._status['datetime'] = d.isoformat()
            return d

    @property
    def time_offset(self):
        if self.ok:
            now = datetime.datetime.today()
            gp_time = self.datetime
            if now > gp_time:
                multiplier = 1
                time_offset = now - gp_time
            else:
                multiplier = -1
                time_offset = gp_time - now
            time_offset = time_offset.total_seconds() * multiplier
            self._status['time_offset'] = humanize.naturaltime(time_offset)
            return time_offset

    def capture(self):
        return self._command_api('/command/shutter', '1')

    def stop(self):
        return self._command_api('/command/shutter', '0')

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
    for photo in camera[0:3]:
        location = '/home/denis/GoPro/' + photo.basename 
        photo.save(location)
