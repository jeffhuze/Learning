import urllib.request, urllib.parse 
import http, json, ssl 

serviceUrl = 'https://py4e-data.dr-chuck.net/opengeo?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break 

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceUrl + urllib.parse.urlencode(parms)  # adds the %2C for the space and coma for City, State

    print('Retrieving: ', url)
    uh = urllib.request.urlopen(url, context = ctx)
    data = uh.read().decode()           # data is in UTF8 on the web, decode will give back in Unicode Python string
    print('Retrieved: ', len(data), ' characters ', data[:20].replace('\n', ' ') )

    try:
        js = json.loads(data)
    except:
        js = None 

    if not js or 'features' not in js:
        print('==== Download Error ===')
        print(data)
        break  
    if len(js['features']) == 0:
        print('=== Object not found ===')
        print(data)
        break 

    lat = js['features'][0] ['properties']['lat']
    lon = js['features'][0] ['properties']['lon']
    county = js['features'][0] ['properties']['county']
    print('lat: ', lat, 'lon: ', lon)
    print('county: ', county)
    location = js['features'][0]['properties']['formatted']
    print(location)

    print(json.dumps(js, indent = 4) )
    print(json.dumps(js['features'][0]['properties'], indent = 7) )
