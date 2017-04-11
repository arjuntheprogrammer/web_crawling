from bs4 import BeautifulSoup

import requests
#import urllib.request
import urllib

def titles():
	url="http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=moto+g4"
	source_code=requests.get(url)
	plain_text=source_code.text

	soup=BeautifulSoup(plain_text, "html.parser")
	
	for k in soup.findAll('a', {'class':'a-link-normal s-access-detail-page  a-text-normal'} ):
		title=k.get('title')
		#print (title)


	#http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=moto+g4
	#class="s-access-image cfMarker"	
	var=1
	for k in soup.findAll('img', {'class':'s-access-image cfMarker'} ):
		src=k.get('src')
		download_image_from_url(src, var)
		var+=1
		print (src)

def download_image_from_url(url, var):
	filename=str(var)+".jpeg"
	#urllib.request.urlretrieve(url, filename)
	urllib.urlretrieve(url, filename)


titles()		