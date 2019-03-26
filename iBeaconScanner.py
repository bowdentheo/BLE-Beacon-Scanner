#This is a working prototype. DO NOT USE IT IN LIVE PROJECTS

import ScanUtility
import bluetooth._bluetooth as bluez

#Set bluetooth device. Default 0.
dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print ("\n *** Looking for iBeacons ***\n")
	print ("\n *** CTRL-C to Cancel ***\n")
except:
	print ("Error accessing bluetooth")

ScanUtility.hci_enable_le_scan(sock)

#Scans for iBeacons
try:
	while True:
		returnedList = ScanUtility.parse_events(sock, 10)
		for item in returnedList:
			print(item)
			print("UUID:", item["uuid"])
			print("Major:", item["major"])
			print("Minor:", item["minor"])
			print("RSSI:", item["rssi"])
			print("Mac Address:", item["macAddress"])
			print("")
except KeyboardInterrupt:
    pass
