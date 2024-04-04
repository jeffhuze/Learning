import socket 

# mysock = socket.socket(socket.AF_INET, socket.sock_stream)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() # encdoing in UTF-8
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if ( len(data) < 1):
#         break
#     mystring = data.decode()
#     print(mystring)
# mysock.close()

#####

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print( line.decode().strip() )

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print( line.decode().strip() )

## Parsing web pages or web scraping
# beautiful soup from crummy.com
# install at https://pypi.python.org/pypi/beautifulsoup4
        