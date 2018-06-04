import re
import os
import Image
import pytesseract
import threading
import requests ; from bs4 import BeautifulSoup
from collections import Counter
import datetime


#os.system('adb exec-out screencap -p > screen.png')
os.rename('screen.png', 'screen.jpg')
n=datetime.datetime.now().time().second
os.system('cp "screen.jpg" '+str(n))
os.system('python crop2.py & python crop3.py & python crop4.py & python crop.py ')
os.system('python process.py ans1.jpg ans1text.jpg & python process.py ans2.jpg ans2text.jpg & python process.py ans3.jpg ans3text.jpg &')
os.system('python process.py test.jpg text.jpg') 
#os.system('python process.py test.jpg text.jpg' )


q= str(pytesseract.image_to_string(Image.open('text.jpg')))
a1= str(pytesseract.image_to_string(Image.open('ans1text.jpg')))
a2= str(pytesseract.image_to_string(Image.open('ans2text.jpg')))
a3= str(pytesseract.image_to_string(Image.open('ans3text.jpg')))

os.system('rm -rf *.jpg')
c1=Counter({1:0, 2:0, 3:0})


a1='Brazil'
a2='Italy'
a3='India'
q='Which country has had the most FIFA World Cup wins?'
q=q.replace("= ","B")
q=q.replace(": ","B")
q=' '.join(q.split())
a1=a1.replace("= ", "B")
a2=a2.replace("= ", "B")
a3=a3.replace("= ", "B")
a1=a1.replace(": ", "B")
a2=a2.replace(": ", "B")
a3=a3.replace(": ", "B")
print q
print a1
print a2
print a3
print ""

def fetch_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    elems = soup.select('#resultStats')
    print(elems[0].getText())


base = "http://www.google.com"
url = "http://www.google.com/search?q="+ q 

response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
for item in soup.select(".r a"):
    print item.text
    for i in a1.split():
        if i in item.text:
            c1.update([1])
    for i in a2.split():
        if i in item.text:
            c1.update([2])
    for i in a3.split():
        if i in item.text:
            c1.update([3])
for item in soup.select(".st"):
    for i in a1.split():
        if i in item.text:
            c1.update([1])
    for i in a2.split():
        if i in item.text:
            c1.update([2])
    for i in a3.split():
        if i in item.text:
            c1.update([3])
print ""
for i in (1,2,3):
    print str(c1[i])
print ""

websites=["http://www.google.com/search?q="+q+" "+a1,"http://www.google.com/search?q="+q+" "+a2,"http://www.google.com/search?q="+q+" "+a3]

threads = [threading.Thread(target=fetch_links, args=(url,))
           for url in websites]

for t in threads:
    t.start()



        