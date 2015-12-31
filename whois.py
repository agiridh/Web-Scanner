import os

# Gives all kinds of information about a domain name
# print get_whois('google.com')
def get_whois(domain_name):
    print "Getting the whois info..."
    command = 'whois ' + domain_name
    process = os.popen(command)
    results = str(process.read())
    return results
