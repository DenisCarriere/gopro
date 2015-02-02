from pymongo import MongoClient
import pexif
import os


client = MongoClient()

for item in client.gopro.process.find({}):
    path = item['path']
    lat = float(item['lat'])
    lng = float(item['lng'])
    bearing = (float(item['bearing']) + 90) % 360

    if lat > 0.0:
        lat_ref = 'N'
    else:
        lat_ref = 'S'
    if lng > 0.0:
        lng_ref = 'E'
    else:
        lng_ref = 'W'

    # Run Command for Bearing
    cmd = 'exiftool '
    cmd += '-gpsimgdirection={0} -gpsimgdirectionref=true '.format(bearing)
    cmd += '-gpsdestbearing={0} -gpsdestbearingref=true '.format(bearing)
    cmd += '-gpslatitude={0} -gpslatituderef={1} '.format(lat, lat_ref)
    cmd += '-gpslongitude={0} -gpslongituderef={1} '.format(lng, lng_ref)
    cmd += path
    print cmd

    os.system(cmd)