#!C:/Users/sergi/AppData/Local/Programs/Python/Python37-32/python.exe
print("Content-Type: text/html\n")
from urllib.request import Request, urlopen
import re
import cgi
from bs4 import BeautifulSoup
import json
import sys
from lxml import html
import requests


#Abrir pagina web i adquirir texto
url = "https://www.freecodecamp.org/news/my-first-python-project-converting-a-disorganized-text-file-into-a-neatly-structured-csv-file-21f4c6af502d"
file = 'test'


def urlToList(url, fileName):
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
	text = '/n'.join(chunk for chunk in chunks if chunk)	# drop blank lines
	
	#trabajaremos siempre con las palabras en minúsculas para evitar possibles errores de búsqueda
	text = text.lower()
	x={
		"lista" : text.split()
	}

	#Passamos el texto como lista de palabras en un fichero
	with open(fileName+'.json', 'w') as filehandle:
	    json.dump(x, filehandle, ensure_ascii = False)

	return True

print("test.com")