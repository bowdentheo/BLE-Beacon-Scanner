#This is a working prototype. DO NOT USE IT IN LIVE PROJECTS

import sys
import struct
import bluetooth._bluetooth as bluez

def hci_enable_le_scan(sock):
    hci_toggle_le_scan(sock, 0x01)

def hci_toggle_le_scan(sock, enable):
    cmd_pkt = struct.pack("<BB", enable, 0x00)

def packetToString(packet):
    """
    Returns the string representation of a raw HCI packet.
    """
    if sys.version_info > (3, 0):
        return ''.join('%02x' % struct.unpack("B", bytes([x]))[0] for x in packet)
    else:
        return ''.join('%02x' % struct.unpack("B", x)[0] for x in packet)

def parse_events(sock, loop_count=100):
    old_filter = sock.getsockopt( bluez.SOL_HCI, bluez.HCI_FILTER, 14)
    flt = bluez.hci_filter_new()
    bluez.hci_filter_all_events(flt)
    bluez.hci_filter_set_ptype(flt, bluez.HCI_EVENT_PKT)
    sock.setsockopt( bluez.SOL_HCI, bluez.HCI_FILTER, flt )
    results = []
    for i in range(0, loop_count):
        packet = sock.recv(255)
        ptype, event, plen = struct.unpack("BBB", packet[:3])
        packetOffset = 0
        dataString = packetToString(packet)
        """
        If the bluetooth device is an iBeacon then show the beacon.
        """
        if dataString[38:46] == '4c000215':
            """
            Selects parts of the bluetooth packets.
            """
            #print (dataString)
            uuid = dataString[46:54] + "-" + dataString[54:58] + "-" + dataString[58:62] + "-" + dataString[62:66] + "-" + dataString[66:78]
            major = dataString[78:82]
            minor = dataString[82:86]
            majorVal = int("".join(major.split()[::-1]), 16)
            minorVal = int("".join(minor.split()[::-1]), 16)
            """
            Organises Mac Address to display properly
            """
            scrambledAddress = dataString[14:26]
            fixStructure = iter("".join(reversed([scrambledAddress[i:i+2] for i in range(0, len(scrambledAddress), 2)])))
            macAddress = ':'.join(a+b for a,b in zip(fixStructure, fixStructure))
            rssi, = struct.unpack("b", packet[packetOffset -1])

            #print("UUID",uuid)
            #print("Major",majorVal)
            #print("Minor",minorVal)
            #print("Mac Address",macAddress)
            #print ("RSSI:", rssi)
            #print ("----------")

            resultsArray = [{"uuid": uuid, "major": majorVal, "minor": minorVal, "rssi": rssi, "macAddress": macAddress}]

            return resultsArray

    return results
