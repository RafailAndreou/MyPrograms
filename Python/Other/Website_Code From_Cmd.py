import sys

try:
    import urllib.request
except ImportError:
    import urllib2

script,URL = sys.argv

try:
    url = urllib.request.urlopen(sys.argv[1])
except NameError:
    url = urllib2.urlopen(sys.argv[1])
    
print(str(url.read()))
          
