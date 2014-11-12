# GoPro - Python API

At the moment this module only works with the newest GoPro Hero 4.

The earlier versions of GoPro are not backwards/forwards compatible.

## Install

Easy install with Github or PyPi

Installing the **latest version from GitHub**.

```bash
$ git clone https://github.com/DenisCarriere/gopro.git
$ cd gopro
$ python setup.py install
```

Installing the **tested version from PyPi**.

```bash
$ sudo pip install gopro
```

## Quickstart

Once the installation is complete you are ready to start! :)

The default `IP` address for the GoPro is using `10.5.5.9`.

You must first be connected to the GoProApp Wifi connection.

Launch your favorite `ipython` or standard `python`

```python
>>> import gopro
>>> camera = gopro.camera()
>>> camera.photo()
...
```

## Camera modes

Makes it easy to cycle threw each available modes.

```python
>>> camera.mode('burst')
>>> camera.mode('photo')
>>> camera.mode('timelapse')
>>> camera.mode('video')
...
```

## Locate (Beep! Beep!)

Can't find your device?? Call the locate function and it will Beep endlessly until there is no more battery.

To turn off the beeps, simply press the `mode` button on the device or use the `off` as a parameter.

```python
>>> camera.locate('on')
>>> camera.locate('off')
...
```

## Sleep

The camera will turn itself off, the Wi-Fi will still be active.

At the moment there is no working commands to turn the device back on.

To reactivate the device, press the `mode` button.

```python
>>> camera.sleep()
...
```

## Delete Photos

Might be useful to dump all those photos from your GoPro.

**Warning** once you delete photos/videos you cannot retrieve them back.

The `erase` function does the same as the delete all.

```python
>>> camera.erase()
>>> camera.delete_all()
>>> camera.delete_last()
...
```

## Debug

Want to explore & troubleshoot the device a bit, you can retrieve the following properties from your device.

```
>>> camera.info
>>> camera.commands
...
```

## Contributors

A big thanks to all the people who have helped contribute!

To be a contributor, please message me with requests on [Twitter](https://twitter.com/DenisCarriere)/[Github issues](https://github.com/DenisCarriere/gopro/issues)

- @[DenisCarriere](https://github.com/DenisCarriere)
- @[KonradIT](https://github.com/KonradIT)

## License

The MIT License (MIT)

Copyright (c) 2014-2015 Denis Carriere
