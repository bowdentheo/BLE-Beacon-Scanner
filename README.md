# iBeacon Scanner

A simple project that scans for iBeacon devices using your Raspberry Pi and Python.

It shows: UUID, Major, Minor, Mac Address and RSSI.

Let me know if there are any issues.

Here is a demo:

![](scannerDemo.gif)

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
So it lookes like this: ```ExecStart=/usr/local/libexec/bluetooth/bluetoothd --experimental```

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
cd Desktop/iBeacon-Scanner
```
Run
```
python iBeaconScanner.py
```

## Running the tests

Once the app is running you should see any iBeacon devices in the viinity around you - The RSSI will update if a beacon moves.


## Deployment

I DON'T recommend that you use this in a live project - it is merely a proof of concept.

## Future Development

- Eddystone support
- UriBeacon support

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
