# Thomas Kerley
# INF 601 - Advanced Python
# Fall 2022
# Final Project

import nmap

# My defined functions and classes
import kerleyFunctions.py as kF
import device.py

def Main():

    # checks permission to scan
    if not kF.permission():
        exit
    
    # nmap scans for local network
    # id gateway
    # id network mask
    # scan ips in mask
    # pull info on active ips
    # check port XXXX for any active client noise
    # id devices that are mobile
    # id devices that are missing client file
    # create network map
    # load local host web app
    # show network and device information



    nm = nmap.Nmap()
    # variable for IPv6 status
    targetIPv6 = False
    # assign target IP and host if different
    print("Please enter target IP address: ")
    targetIP = input()
    #TODO sanitize imput for IPv4 & IPv6 formats

    if targetIP == regexforIPv6:
        targetIPv6 = True
    else:
        targetIPv6 = False
    
    # scan devices and get results.
    if kF.permissionReminder():
        scanResults = nmap()
    else:
        exit
    
    # filtered list of device objects
    devices = kF.parseScanResults(scanResults)