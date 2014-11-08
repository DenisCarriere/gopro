import requests


class Camera(object):
    def __init__(self, password='Denis44C', ip='10.5.5.9'):
        self._password = password
        self._api_url = 'http://' + ip
        self._web_url = self._api_url + ':8080'

    def _camera_api(self, method, int_param=''):
        return self._api_call('camera', method, int_param)

    def _bacpac_api(self, method, int_param=''):
        return self._api_call('bacpac', method, int_param)

    def _api_call(self, api, method, int_param):
        url = self._api_url + '/gp/gpControl'
        
        r = requests.get(url)
        print r.content
        print r.url

    def delete_all(self):
        return self._camera_api('DA')

    def erase(self):
        return self.delete_all()

    def power_on(self):
        return self._bacpac_api('PW', 1)

    def power_off(self):
        return self._bacpac_api('PW', 0)

if __name__ == '__main__':
    camera = Camera()
    camera.power_off()

"""
&p=%0 + Int

Delete All : camera/DA

"""

"""
The cmd are dispatched against GoPro camera via HTTP request. 
The general query structure is  : http://<ip>/<device>/<app>?t=<password>&p=<command>
 Where:<device> can be bacpac or camera.
 From the page, we can extract the following queries;
 Turn on camera : http://<ip>/bacpac/PW?t=<password>&p=%01
Turn off camera : http://<ip>/bacpac/PW?t=<password>&p=
Change mode    : http://<ip>/bacpac/PW?t=<password>&p=%02
 Start capture : http://<ip>/bacpac/SH?t=<password>&p=%01
Stop capture : http://<ip>/bacpac/SH?t=<password>&p=
 Preview
On : http://<ip>/camera/PV?t=<password>&p=%02
Off : http://<ip>/camera/PV?t=<password>&p=
 Mode
Camera     : http://<ip>/camera/CM?t=<password>&p=
Photo        : http://<ip>/camera/CM?t=<password>&p=%01
Burst         : http://<ip>/camera/CM?t=<password>&p=%02
Timelapse : http://<ip>/camera/CM?t=<password>&p=%03
Timelapse : http://<ip>/camera/CM?t=<password>&p=%04
 Orientation
Head up     : http://<ip>/camera/UP?t=<password>&p=
Head down : http://<ip>/camera/UP?t=<password>&p=%01
 Video Resolution
WVGA-60  : http://<ip>/camera/VR?t=<password>&p=
WVGA-120  : http://<ip>/camera/VR?t=<password>&p=%01
720-30   : http://<ip>/camera/VR?t=<password>&p=%02
720-60   : http://<ip>/camera/VR?t=<password>&p=%03
960-30   : http://<ip>/camera/VR?t=<password>&p=%04
960-60   : http://<ip>/camera/VR?t=<password>&p=%05
1080-30 : http://<ip>/camera/VR?t=<password>&p=%06
 
FOV
wide : http://<ip>/camera/FV?t=<password>&p=
medium : http://<ip>/camera/FV?t=<password>&p=%01
narrow : http://<ip>/camera/FV?t=<password>&p=%02
 Photo Resolution
11mp wide     : http://<ip>/camera/PR?t=<password>&p=
8mp medium  : http://<ip>/camera/PR?t=<password>&p=%01
5mp wide       : http://<ip>/camera/PR?t=<password>&p=%02
5mp medium  : http://<ip>/camera/PR?t=<password>&p=%03
 Timer
0,5sec : http://<ip>/camera/TI?t=<password>&p=
1sec    : http://<ip>/camera/TI?t=<password>&p=%01
2sec    : http://<ip>/camera/TI?t=<password>&p=%02
5sec    : http://<ip>/camera/TI?t=<password>&p=%03
10sec  : http://<ip>/camera/TI?t=<password>&p=%04
30sec  : http://<ip>/camera/TI?t=<password>&p=%05
60sec  : http://<ip>/camera/TI?t=<password>&p=%06
 Localisation
On : http://<ip>/camera/LL?t=<password>&p=%01
Off : http://<ip>/camera/LL?t=<password>&p=
 Bip Volume
0%     : http://<ip>/camera/BS?t=<password>&p=
70%   : http://<ip>/camera/BS?t=<password>&p=%01
100% : http://<ip>/camera/BS?t=<password>&p=%02
"""