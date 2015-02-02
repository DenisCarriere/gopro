import os
import csv
import time
from datetime import datetime
from datetime import timedelta
from dateutil import parser
import exifread
from pymongo import MongoClient


client = MongoClient()
root = '/home/ubuntu/Pictures/GoPro/'
client.gopro.gpx.remove({})
client.gopro.photos.remove({})


with open(root + 'Gopro2.csv') as f:
    first_line = f.readline().strip()
    if first_line == '"Name","Activity type","Description"':
        # Skip 2nd & 3rd line also
        f.readline()
        f.readline()
    else:
        pass

    # Read CSV
    reader = csv.DictReader(f)
    for line in reader:
        delta = timedelta(0, 60*60*5)
        dt = parser.parse(line['Time']) - delta
        store = {
            'lat': line['Latitude (deg)'],
            'lng': line['Longitude (deg)'],
            'dt': dt,
            'bearing': line['Bearing (deg)'],
            'altitude': line['Altitude (m)'],
            'accuracy': line['Accuracy (m)'] 
        }
        client.gopro.gpx.save(store)

# Read Photos
for filename in os.listdir(root):
    if '.JPG' in filename:
        path = root + filename
        with open(path) as f:
            tags = exifread.process_file(f)
            dt = parser.parse(str(tags['EXIF DateTimeOriginal']))
            store = {
                'dt': dt,
                'filename': filename,
                'path': path,
            }
            client.gopro.photos.save(store)