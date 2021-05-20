import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup

url = input("Enter URL")
count = input("Enter count")
position = input("Enter position")
count = int(count)
position = int(position)

i = 0
while i < count :
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    aTags = soup("a")
    tagList = list()
    for tag in aTags : 
        tagList.append(tag.get("href", None))
    url = tagList[position-1]
    print(url)
    i = i + 1