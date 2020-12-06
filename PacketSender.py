import binascii
import socket
import netifaces as ni

# defining functions

def getInterfaceInfo(iface_name):
    """This function will read actual NIC configuration as source MAC and source IP.
    Input parameters: interface name, from which we send packets.
    Return: current MAC, current IP """
    ip = ni.ifaddresses(iface)[ni.AF_INET][0]['addr']
    netmask = ni.ifaddresses(iface)[ni.AF_INET][0]['netmask']
    iface_mac=ni.ifaddresses(iface)[ni.AF_LINK][0]['addr']
#    print(ip, netmask, iface_mac) # debug only
    return(iface_mac, ip)


def send_packet(dest_ip,dest_port,payload):
    """" This function will generate packet from a specified interface, basing on next input parameters:
        Input: dest_ip,dest_port,payload
        Output: status of sending if successful
    """
    pass


# reading the input parameters:
# source interface, destination IP, dest port, payload

iface=str(input("Enter your source interface:"))
#dest_ip=str(input("Enter your destination interface:"))
#dest_port=str(input("Enter your destination port:"))
#payload=str(input("Enter UDP payload of your packet in HEX format:"))

