# yaglib

## Intro

yaglib (Yet Another Gatt LIBrary) provide peripheral server side support based on bluez and the related dbus API.
It is based on examples from bluez-5.44 source distributions: bluez/test/example-get-server.

Note: This library was tested on Ubuntu. It will not work on systems that don't support bluez,
such as Mac OSX or Windows.

## Requirements

* Python 3.4+
* Python packages - see requirements.txt
* python3-dbus installed via apt-get

```bash
apt-get install python3-dbus
```
yaglib has been tested on Ubuntu 16.04 and Raspberry PI Raspian kernel update from May 2017.

## Examples 

Examples directory contains one server example that simulates heart rate service:

See

```
./examples/hrserver.py
./examples/hrservice.py
./examples/testservice.py
```

## Installation


Normal installation via pip:

```bash
pip3 install git+git://github.com/manylabs/yaglib.git
```

Development - use local source tree

```bash
ls yaglib
# __init__.py	yaglib.py yaglibadv.py
export PYTHONPATH=`pwd`:$PYTHONPATH
```

Install python library from local source tree

```bash
ls yaglib
# __init__.py	yaglib.py yaglibadv.py
python3 setup.py install
```


### Running and Testing Examples 

* Run sample gatt advertise server and heartrate server that simulates heart rate and battery service

```bash
# advertise can run in the background
./examples/hradvertise.py &
./examples/hrserver.py
```

* Test heartrate via Web Bluetooth testapp from Web Bluetooth Community Group (WebBluetoothCG):

https://webbluetoothcg.github.io/demos/heart-rate-sensor/


## TODO

* Add example for custom service
* Add unit tests




