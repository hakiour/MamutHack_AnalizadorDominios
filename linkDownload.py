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



def urlToList(url, dominio):
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
	text = re.sub('[!@#$1234567890"]', '', text)
	text = re.sub('[-_]', ' ', text)

	
	#trabajaremos siempre con las palabras en minúsculas para evitar possibles errores de búsqueda
	text = text.lower()
	counts = Counter(text.split())		#calculamos frecuencia de las palabras

	for word in list(counts.keys()):					#utilizamos list() para evitar runtime error al iterar sobre keys()
		if(len(word)<4 or len(word)>10):
			del counts[word]

	#creamos un diccionario con el link como llave y la lista (otro dic en vd) de palabras y su freq
	DicLink={
		url : counts,
		"SCORE" : 0
	}


	return DicLink


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
		

		busqueda = {
			"DOMINI" : urlSrc,
			"TEMATICA" : tema,
			"LINKS" : {}
		}

		for link in arrayUrls[:-1]:
			print("reading link: "+ link)
			dicPalabrasLink = urlToList(link, urlSrc)
			busqueda["LINKS"][link]=dicPalabrasLink[link]				#añadimos entrada de url: palabras.

		return busqueda

	else:
		print('Error input')
		return None

#print(readLinks())

