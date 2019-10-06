#!C:\Users\localadmin\Anaconda3\python.exe

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
	text = re.sub('[!@#$1234567890?¿¡."]', '', text)
	text = re.sub('[-_]', ' ', text)

	
	#trabajaremos siempre con las palabras en minúsculas para evitar possibles errores de búsqueda
	text = text.lower()
	palabras = dict(Counter(text.split()))		#calculamos frecuencia de las palabras

	for word in list(palabras.keys()):					#utilizamos list() para evitar runtime error al iterar sobre keys()
		if(len(word)<4 or len(word)>10 or palabras[word] <= 2):
			del palabras[word]

	#creamos un diccionario con el link como llave y la lista (otro dic en vd) de palabras y su freq
	DicLink={
		url : palabras,
		"PUNTUACION" : 0
	}


	return DicLink


def readLinks(url, tema):
	rutaGoogle = 'http://www.google.com/search?btnG=1&q=site%3A'
	pagina = requests.get(rutaGoogle + url)
	tree = html.fromstring(pagina.content)
	arrayUrls = []

	for elementos in tree.xpath("//a"):
		ruta = elementos.get("href")
		if "/url?q" in ruta:
			arrayUrls.append(elementos.get("href").replace("/url?q=",""))#"http://www.google.com"+elementos.get("href"))
	
	busqueda = {
		"DOMINI" : url,
		"TEMATICA" : tema,
		"LINKS" : {}
	}

	for link in arrayUrls[:-1]:

		#print("reading link: "+ link)
		dicPalabrasLink = urlToList(link, url)
		busqueda["LINKS"][link]=dicPalabrasLink				#añadimos entrada de url: palabras.


	return busqueda
	


