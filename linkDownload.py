#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import Request, urlopen
import re
import cgi
from bs4 import BeautifulSoup
import json
import sys
from lxml import html
import requests
from collections import Counter

#Abrir pagina web i adquirir texto
url = "https://www.freecodecamp.org/news/my-first-python-project-converting-a-disorganized-text-file-into-a-neatly-structured-csv-file-21f4c6af502d"
file = 'test'



def urlToList(url, fileName, dominio):
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	soup = BeautifulSoup(webpage, features="lxml")

	# elimina elementos script y style
	for script in soup(["script", "style"]):
	    script.extract()    # rip

	# sacar solo texto
	text = soup.body.get_text()

	# El siguiente proceso es para separar en lineas y unirlo en un solo string
	lines = (line.strip() for line in text.splitlines())
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))	# break multi-headlines into a line each
	text = '\n'.join(chunk for chunk in chunks if chunk)	# drop blank lines
	
	#trabajaremos siempre con las palabras en minúsculas para evitar possibles errores de búsqueda
	text = text.lower()
	counts = Counter(text.split())
	x={
		"Dominio" : dominio,
		"Link": url,
		"Palabras": counts
	}

	#Passamos el texto como lista de palabras en un fichero
	#with open(fileName+'.json', 'w') as filehandle:
	#    json.dump(x, filehandle, ensure_ascii = False)

	return True


def readLinks():

	rutaGoogle = 'http://www.google.com/search?btnG=1&q=site%3A'
	datosForm = cgi.FieldStorage()

	if datosForm:
		url = datosForm["url"]
		arrayUrl = (url.split("//"))
		if len(arrayUrl) == 2: 
			url = arrayUrl[1]
		else: 
			print('Error url')
			return 0

		tema = datosForm["tema"]
		
		pagina = requests.get(rutaGoogle + url)
		tree = html.fromstring(pagina.content)
		arrayUrls = []

		for elementos in tree.xpath("//a"):
			ruta = elementos.get("href")
			if "/url?q" in ruta:
				arrayUrls.append(elementos.get("href").replace("/url?q=",""))#"http://www.google.com"+elementos.get("href"))
		
		i=0

		for link in arrayUrls[:-1]:
			print("reading link: "+ link)
			urlToList(link, "test"+str(i), urlSrc)
			i+=1
	else:
		print('Error input')



#url = "https://www.elmundo.es/pais-vasco/2019/07/10/5d25f9af21efa0c0578b456f.html"
#urlToList(url,file)

readLinks()



#map reduce para contar palabras
