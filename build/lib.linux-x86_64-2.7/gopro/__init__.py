#!/usr/bin/env python
# coding: utf8

"""
geocoder library
~~~~~~~~~~~~~~~~
GoPro Camera Python module made easy.

>>> import gopro
>>> camera = gopro.camera()
>>> camera.photo()
"""

__title__ = 'gopro'
__author__ = 'Denis Carriere'
__author_email__ = 'carriere.denis@gmail.com'
__version__ = '0.0.1'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2014-2015 Denis Carriere'

from .api import camera