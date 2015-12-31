from tld import get_tld

# get the mid level domain.
# Ex: print get_domain_name("http://www.google.com") prints google.com
def get_domain_name(url):
    print "Getting the mid level domain name..."
    domain_name = get_tld(url)
    return domain_name
