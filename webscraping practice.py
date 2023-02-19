import urllib.request,urllib.parse,urllib.error
file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
dict = dict()
for lines in file :
                  words = lines.decode().split()
                  print(words)
                  for w in words :
                                    if w in dict :
                                                      dict[w] = dict[w] + 1
                  
                                    else :
                                                      dict[w] = 1
                  print(dict)
                                          

lis = list()
for key,value in dict.items():
                  print(key,value)
                  newtuple = value,key
                  lis.append(newtuple)
                  newtuple = sorted(lis,reverse=True)
print(newtuple)



import requests
from bs4 import BeautifulSoup

url =  'https://www.codewithharry.com'

r = requests.get(url)
htmlcontent = r.content
print(htmlcontent)

soup = BeautifulSoup(htmlcontent,'html.parser')
print(soup.prettify)

title = soup.title
print(title)

paras= soup.find_all('p')
print(paras)

text = soup .get_text()
print(text)


anchors = soup.find_all('a')
all_links = set()
print(anchors)
for links in anchors :
                  links =  'https://www.codewithharry.com'+links.get('href')
                  print(links)