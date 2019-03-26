# BLE iBeacon Scanner - iBeacon and Eddystone Beacons

A simple project that scans for iBeacon and Eddystone BLE beacons using your Raspberry Pi and Python.

## iBeacon
UUID, Major, Minor, Mac Address and RSSI

## Eddystone
UID - Finds: Namespace ID and Instance ID.

URL - Finds: URL and URL Prefix.

EID - Finds (Details comming soon).

TLM - Finds (Details comming soon).


Let me know if there are any issues.

Here is a demo:

![](BLEBeaconDemo.gif)

## Getting Started

You will need to download ```bluez``` to get bluetooth data.

```
sudo apt-get update
sudo apt-get install python-pip python-dev ipython
```
```
sudo apt-get install bluetooth libbluetooth-dev
sudo pip install pybluez
```

Additionally to detect BLE devices you need to enable the experimental features. To do this:

1. Go to directory

```
cd /lib/systemd/system
```
2. Edit a file
```
sudo vim bluetooth.service
```
Add ```--experimental``` after  ```ExecStart=/usr/local/libexec/bluetooth/bluetoothd```
So it lookes like this: 
```
ExecStart=/usr/local/libexec/bluetooth/bluetoothd --experimental
```

3. Save and exit vim
Shift + Colon, then type ```wq!``` - to write and quit.

4. Restart daemon
```
sudo systemctl daemon-reload
```
5. Restart bluetooth
```
sudo systemctl restart bluetooth
```

## Quick Start

Download files.

Go to directory
```
cd Desktop/BLE-Beacon-Scanner
```
Run
```
python BeaconScanner.py
```
Note that this does not work with Python 3 yet... we are working on it!

## Running the tests

Once the app is running you should see any iBeacon and Eddystone devices in the vicinity - The RSSI will update if an iBeacon moves.

## Deployment

I DON'T recommend that you use this in a live project - it is merely a proof of concept.

## Future Development

- UriBeacon support
- Versatility
- Beacon type selection

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE
