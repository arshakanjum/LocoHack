import re
import os
import Image
import pytesseract
import threading
import requests ; from bs4 import BeautifulSoup
from collections import Counter
import datetime


#os.system('adb exec-out screencap -p > screen.png')
#os.rename('screen.png', 'screen.jpg')
#n=datetime.datetime.now().time().second
#os.system('cp screen.jpg '+str(n)+'.jpg')
#os.system('mv '+str(n)+'.jpg Backup/')
#os.system('python desc.py')
#os.system('python process.py ans1.jpg ans1text.jpg & python process.py ans2.jpg ans2text.jpg & python process.py ans3.jpg ans3text.jpg &')
#os.system('python process.py test.jpg text.jpg') 



#q= str(pytesseract.image_to_string(Image.open('text.jpg'), config="letters -psm 6"))
#a1= str(pytesseract.image_to_string(Image.open('ans1text.jpg'), config="letters -psm 6"))
#a2= str(pytesseract.image_to_string(Image.open('ans2text.jpg'), config="letters -psm 6"))
#a3= str(pytesseract.image_to_string(Image.open('ans3text.jpg'), config="letters -psm 6"))

q='Who is the father of the nation india'
a1='the'
a2='is'
a3='Mahatma Gandhi'

if len(a1)>len(q):
    a1,q=q,a1
if len(a2)>len(q):   
    a2,q=q,a2
if len(a3)>len(q):
    a3,q=q,a3
os.system('rm -rf *.jpg')
c1=Counter({1:0, 2:0, 3:0})

q=q.replace("= ","B")
q=q.replace(": ","B")
q=q.replace("=","B")
q=q.replace(":","B")
q=' '.join(q.split())
a1=a1.replace("= ", "B")
a2=a2.replace("= ", "B")
a3=a3.replace("= ", "B")
a1=a1.replace(": ", "B")
a2=a2.replace(": ", "B")
a3=a3.replace(": ", "B")
#d=['The','the','and', 'of','in','is','Indians','indians','Warriors','warrior']
d=['The','the','and', 'of','in','is','as']


print q
print a1
print a2
print a3
print ""


headers = {
    "User-Agent":
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"
        }
def fetch_links(url):
        

    
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text,"lxml")
    elems = soup.select('#resultStats')
    print(elems[0].getText())


base = "http://www.google.com"
url = "http://www.google.com/search?q="+ q 

response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
for result in soup.select('#ires .g'):
    footer = result.select_one('.s .st')

    if not footer:
        # means we're in a div for query images, skipping
        continue

    headline = result.select_one('.r a').text.encode(encoding='UTF-8')
    print headline
    description = footer.text.encode(encoding='UTF-8')
    #print(headline.encode(encoding='UTF-8'), description.encode(encoding='UTF-8'))
    for i in set(a1.split())-set(d):
        if i in headline or i in description or i.upper() in headline or i.upper() in description or i.lower() in headline or i.lower() in description:
            c1.update([1])
    for i in set(a2.split())-set(d):
        if i in headline or i in description or i.upper() in headline or i.upper() in description or i.lower() in headline or i.lower() in description:
            c1.update([2])
    for i in set(a3.split())-set(d): 
       if i in headline or i in description or i.upper() in headline or i.upper() in description or i.lower() in headline or i.lower() in description:
            c1.update([3])

print ""

print a1 +" : "+ str(c1[1])
print a2 +" : " +str(c1[2])
print a3 +" : " +str(c1[3])


websites=["http://www.google.com/search?q="+q+" "+a1,"http://www.google.com/search?q="+q+" "+a2,"http://www.google.com/search?q="+q+" "+a3]

threads = [threading.Thread(target=fetch_links, args=(url,))
           for url in websites]

for t in threads:
    t.start()



        