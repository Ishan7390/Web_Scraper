import requests
import bs4
link_list=[]
res = requests.get('https://www.apple.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')

for link in soup.find_all('a', href=True):
	'''link_list.append(link)
	# if link[0]=='#':
 	# 	link_list.remove(link)
 	if link[0]=='/':
		link_list.remove(link)

 link_list
'''
	# if link['href']!="#":
	# 	print(link["href"])
	if link['href'][0]=='#':
		pass
	elif link['href'][0]=='/':
		pass
	else:
		print(link['href'])