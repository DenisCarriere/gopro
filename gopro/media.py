#!/usr/bin/env python
# coding: utf8
import os
import requests
import humanize
from PIL import Image #http://stackoverflow.com/questions/32772596/pip-install-pil-fails
from StringIO import StringIO


class Media(object):
    def __init__(self, url):
        self.url = url
        self.basename = os.path.basename(self.url)
        self.name, self.extension = os.path.splitext(self.basename)
        self.media_type = self._get_media_type(self.extension)

    def _get_media_type(self, extension):
        extension = extension.lower()
        media_type_lookup = {
            '.jpg': 'Photo',
            '.mp4': 'Video',
        }
        return media_type_lookup[extension]
    
    def download(self):
        r = requests.get(self.url)
        self.content = r.content

    def save(self, location):
        # Create Folder
        folder, filename = os.path.split(location)
        if not os.path.exists(folder):
            os.mkdir(folder)
        # Save file
        if filename:
            return self.img.save(location)

    @property
    def img(self):
        self.download()
        return Image.open(StringIO(self.content))

    @property
    def size(self):
        self.download()
        size_bytes = len(r.content)
        return humanize.naturalsize(size_bytes)

    def __repr__(self):
        return '<Media - {0} [{1}]>'.format(self.basename, self.media_type)


if __name__ == '__main__':
    media = Media('http://hello.com/DC1111.jpg')
    print(media)
