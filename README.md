# GoPro

### A complete Python GoPro module made easy.

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
>>> camera.status
{'connection': 'OK',
 'datetime': '2014-11-12T23:53:59',
 'ip': '10.5.5.9',
 'ok': True,
 'screen': 'video',
 'storage': '31.3 GB',
 'time_offset': 'now'}
...
```

## Take a Photo or Video

With very simple commands you can tell your GoPro to start recording or take a photo.

The screen will automaticly change to the approriate page.

```python
>>> camera.photo()
>>> camera.video()
>>> camera.timelapse()
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

## Settings

You can explore the different types of settings & status by getting the raw JSON response or selecting a specific pre-parsed attribute

### Processed attributes

**Status - Screen**

This will let you know which page your GP is currently active.

There are only 4 available outcomes.

```python
>>> camera.status
'settings'
'video'
'photo'
'timelapse'
...
```

### Raw JSON Responses

The original response from the GoPro device.

```python
>>> camera.settings_raw
>>> camera.status_raw
...
```

## Date & Time

It is a good idea to sync your GoPro with the same clock as your computer.

An easy way to do this is use the `datetime` &  `time_offset` attribute.

Try to aim your GoPro to have less than 1 second offset.

The `time_offset` is measured in (+/-) seconds.

```python
>>> camera.datetime
2014-11-12 21:53:09
>>> camera.datetime_offset
-0.320142
...
```

## File Storage

Here is how you can retrieve the total file storage in (KB) or pretty human readeable format.

```python
>>> camera.status_storage
31330144
>>> camera.status['storage']
'31.3 GB'
```

## Debug

Want to explore & troubleshoot the device a bit, you can retrieve the following properties from your device.

```python
>>> camera.debug
>>> camera.info
>>> camera.commands
...
```

## Contributors

A big thanks to all the people who have helped contribute!

To be a contributor, please message me with requests on [Twitter](https://twitter.com/DenisCarriere)/[Github issues](https://github.com/DenisCarriere/gopro/issues)

- @[Denis Carriere](https://github.com/DenisCarriere)
- @[Konrad Iturbe](https://github.com/KonradIT)
- @[Jason Moiron](https://github.com/jmoiron)

## License

The MIT License (MIT)

Copyright (c) 2014-2015 Denis Carriere
