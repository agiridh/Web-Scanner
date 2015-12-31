'''
author: Aditya Giridhar
To run this file type: python main.py website_name http://www.website_url.com
'''
from sys import argv
from domain_name import *
from general import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

# Creating root directory where scans of all the websites can be stored
ROOT_DIR = 'websites'
create_dir(ROOT_DIR)

script, name, url = argv

# Scanning the website mentioned by the user
def get_information(name, url):
    domain_name = get_domain_name(url)
    ip_addr = get_ip_address(domain_name)
    nmap = get_nmap('-F', ip_addr)
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, ip_addr, nmap, robots_txt, whois)

# Each website's scanned information is stored in a seperate folder
# Each scan's result is stored in a seperate file
def create_report(name, full_url, domain_name, ip_addr, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/ip_addr.txt', ip_addr)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots_txt.txt', robots_txt)
    write_file(project_dir + '/whois.txt', whois)

get_information(name, url)
