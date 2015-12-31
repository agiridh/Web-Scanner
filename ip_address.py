import os
import socket # This module provides access to the BSD socket interface

# get_ip_address takes in a mid level domain name as its only argument
# returns ip address of a website. (print get_ip_address('google.com'))
# Another way to do this:
# def get_ip_address(url):
#   command = 'host' + url
#   process = popen(command)
#   results = str(process.read())
#   marker = results.find('has address') + 12
#   return results[marker:].splitlines()[0]
def get_ip_address(domain_name):
    print "Obtaining the ip address of the website..."
    ip_addr = socket.gethostbyname(domain_name)
    return ip_addr
