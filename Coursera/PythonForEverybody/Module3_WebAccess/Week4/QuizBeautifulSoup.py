import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl 

myString = 'http://py4e-data.dr-chuck.net/comments_2002960.html'
myCounter = 0
mySummer = 0
# url = input('Enter - For Quiz')
html = urllib.request.urlopen(myString).read() #Use myString rather than url
soup = BeautifulSoup(html, 'html.parser')
spans = soup('span')
for span in spans:
    # print( 'Span:', span)
    # print('URL:', span.get('href',None) )
    # print('Contents:', span.contents[0])
    myCounter = myCounter + int( span.contents[0] )
    mySummer = mySummer + 1
print('Count ', mySummer)    
print('Sum ', myCounter)
