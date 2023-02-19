import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithharry.com'

# step 1 , get the html !

r = requests.get(url)
htmlcontent = r.content
#print(htmlcontent)

#parse the html !
soup =  BeautifulSoup(htmlcontent,'html.parser')
#print(soup.prettify)

#get the title of a website !
title = soup.title
#print('------------' ,title, '---------------')

#get all the paragraphs from this page !
paras = soup.find('p2')
#print('************',paras,'***************')

#print(soup.find('p')['class'])
print(soup.get_text())


#get all anchortags or links from the wesbite !
anchors = soup.find_all('a')
all_links = set()
print(anchors)
for link in anchors :
    link = "https://www.codewithharry.com" + link.get('href')
    all_links.add(link)
    print(link)

