#https://www.codechef.com/contests


from bs4 import BeautifulSoup

import requests

def titles():
	url="https://www.codechef.com/contests"
	source_code=requests.get(url)
	plain_text=source_code.text

	soup=BeautifulSoup(plain_text, "html.parser")
	for k in soup.findAll('a'):#, {'href':'<a href="/IOIPRAC">INOI Practice 2015</a>'} ):
		title=k.get('href')
		print (title)


titles()		