import requests
from bs4 import BeautifulSoup

#r = requests.get('https://www.digmandarin.com/hsk-1-vocabulary-list.html')
#soup = BeautifulSoup(r.text, 'html.parser')

file = open("1.html", 'r', encoding="utf8")
text = file.read()
soup = BeautifulSoup(text, 'html.parser')

#print(soup.find('tr'))

file = open("2.html", 'w', encoding="utf8")

for link in soup.find('tr'):
	link = str(link)
	link = link.strip()
	if link != "":
		soup2 = BeautifulSoup(link, 'html.parser')
		a = soup2.th.contents
		a = str(a)
		file.write(a)

