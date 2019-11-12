import bs4
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen as ureq

uClient = ureq("https://uwaterloo.ca/")
thepage = uClient.read()
uClient.close()
soupdata = BS(thepage, 'lxml')


soup = BS("https://uwaterloo.ca/", 'lxml')
for img in soup.findAll("img"):
	temp = img.get("src")
	if temp[:1]=="/":
		image = "https://uwaterloo.ca/" + temp
	else:
		image = temp

	nametemp = img.get("alt")
	if len(nametemp)==0:
		filename = str(i)
		i+=1
	else:
		filename=nametemp	

	imagefile = open(filename + ".jpeg", "wb")
	imagefile.write(ureq(image).read())
	imagefile.close()		