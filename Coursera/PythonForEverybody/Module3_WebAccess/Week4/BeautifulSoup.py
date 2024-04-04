import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl 

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print( tag.get('href', None) )
# http://www.dr-chuck.com/page1.htm

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - but just an example')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# quiz
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl 

myString = 'http://py4e-data.dr-chuck.net/comments_42.html'
myString = 'http://py4e-data.dr-chuck.net/comments_2002960.html'
myCounter = 0
# url = input('Enter - For Quiz')
html = urllib.request.urlopen(myString).read() #Use myString rather than url
soup = BeautifulSoup(html, 'html.parser')
spans = soup('span')
for span in spans:
    print( 'Span:', span)
    print('URL:', span.get('href',None) )
    print('Contents:', span.contents[0])
    myCounter = myCounter + int( span.contents[0] )
print('Counter: ', myCounter)


