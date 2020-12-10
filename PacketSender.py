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
    """ This function will generate packet from a specified interface, basing on next input parameters:
        Input: dest_ip,dest_port,payload
        Output: status of sending if successful
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)    # creating a socket

                      					       # Let's send data through UDP protocol
   # while True:
    s.sendto(payload.encode('utf-8'), (dest_ip, dest_port))
    print("\n\n Packet sent : ", payload, "\n\n")
    s.close()

    pass


# reading the input parameters:
# source interface, destination IP, dest port, payload

#iface=str(input("Enter your source interface:"))
dest_ip=str(input("Enter your destination ip address:"))
dest_port=int(input("Enter your destination port:"))
payload=str(input("Enter UDP payload of your packet in HEX format:"))

#dest_ip="172.1.1.1"
#dest_port=4000
#payload="1234567890"


send_packet(dest_ip,dest_port,payload)
