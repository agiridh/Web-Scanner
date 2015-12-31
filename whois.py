import os

# Gives all kinds of information about a domain name
# print get_whois('google.com')
def get_whois(url):
    command = 'whois ' + url
    process = os.popen(command)
    results = str(process.read())
    return results
