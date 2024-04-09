import urllib.request, urllib.parse 
import http, json, ssl 

sample = 'http://py4e-data.dr-chuck.net/comments_42.json'
actual = 'http://py4e-data.dr-chuck.net/comments_2002963.json'

url = actual    # change between sample and actual URLs here !!!!

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retrieving: ', url)
uh = urllib.request.urlopen(url, context = ctx)
data = uh.read().decode()           # data is in UTF8 on the web, decode will give back in Unicode Python string
print('Retrieved', len(data), 'characters ')

try:
    js = json.loads(data)
except:
    js = None 

if not js or 'comments' not in js:
    print('==== Download Error ===')
    print(data)
    # break  
if len(js['comments']) == 0:
    print('=== Object not found ===')
    print(data)
    # break 

# print(json.dumps(js, indent = 4) )

myCounter = 0
mySummer = 0

counter1 = js['comments'][0] ['count']
counter2 = js['comments'][1] ['count']
counter3 = js['comments'][2] ['count']
# print(counter1)
# print(counter2)
# print(counter3)

for item in js['comments']:
    # print(item)
    myCounter = myCounter + 1
    # print(item['count'])
    itemCount = int( item['count'] )
    mySummer = mySummer + itemCount

print('Count:', myCounter)
print('Sum:', mySummer)
