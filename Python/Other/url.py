import urllib.request

data = urllib.request.urlopen('https://www.facebook.com')

print(data.read())
