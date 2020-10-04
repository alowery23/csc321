"""Home configuration
192.168.1.79
255.255.255.0
192.168.1.253
"""
"""The output is to see configurations of host and to get IPv4 and IPv6 (TCP/IP) configurations"""
"""The function for netifaces is "import netifaces
netifaces.interfaces()""""
def get_mac(interface: str):
    """For the given interface string, return the MAC address as a string

    Args:
      interface (str): String representation of the interfaces

    Returns: (str) MAC address
    """
   """ addrs[netifaces.AF_LINK] can be used for MAC addresses""" 
   def get_ips(interface: str):


     addrs = netifaces.ifaddresses('en0')  