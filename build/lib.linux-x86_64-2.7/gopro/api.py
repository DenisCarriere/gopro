#!/usr/bin/env python
# coding: utf8

from .camera import Camera

def camera(ip='10.5.5.9'):
	return Camera(ip)