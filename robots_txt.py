from urllib2 import urlopen
import io

# scans and prints the robots.txt of a webpage
# if the url provided by the user does not have a '/', the function adds it
# print get_robots_txt('http://www.reddit.com')
# Since this was built using python 2.7, urllib2 is used instead of
# importing requests from urllib (used in python 3)
def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    request = urlopen(path + 'robots.txt', data=None)
    #data = io.TextIOWrapper(req, encoding='utf-8')
    return request.read()
