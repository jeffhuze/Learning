import urllib.request, urllib.parse, urllib.error
from urllib import request 
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'


sample = 'http://py4e-data.dr-chuck.net/comments_42.xml'
actual = 'http://py4e-data.dr-chuck.net/comments_2002962.xml'
myURL = sample

## change here! ##
## change either sample or actual
html = urllib.request.urlopen(actual)  # this needed to be prefixed with urllib.request instead of request...... without the urllib


data = html.read()
# print("Retrieved",len(data),"characters")

stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment/count')
lst = stuff.findall('comments/comment')
# print('comments/comment/count count: ', len(lst))

lst2 = stuff.findall('count')
# print('comment/count count: ', len(lst2))

counts = stuff.findall('.//count')
# print('counts: ', counts)

myCounter = 0
summed = 0
for item in lst:
    # print('myCounter =', myCounter)
    # print(item)
    myCounter = 1 + myCounter
    # if item.find('count').text is not None:
    #     print('count value: ',  item.find('count').text )
    s = float(item.find('count').text )
    summed = s + summed
print('Count: ',myCounter)    
print('Sum: ', int(summed) ) 
  

'''
while True:
    address = input('Enter location: ')
    address = sample
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)
'''




'''
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)
'''    