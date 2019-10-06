#!C:\Users\localadmin\Anaconda3\python.exe
print("Content-Type: text/html\n")

import mysql.connector
import json
import cgi

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  db="terrassahash",
  port=3306
)

datosForm = cgi.FieldStorage()
idDominio = datosForm["dominio"].value

mycursor = mydb.cursor()
mycursor.execute("SELECT Palabra, FORMAT(FLOOR(SUM(numeroVeces)),0) as numeroVeces FROM dominio JOIN link ON dominio.idDominio = link.idDominio" +
" JOIN palabras ON link.idLink = palabras.idLink WHERE dominio.idDominio = " + idDominio + " GROUP BY Palabra LIMIT 6")

resultado = []

for item in mycursor:
    resultado.append(item)

jsonString = {}

jsonString["respuestaPalabras"] = resultado

print(json.dumps(jsonString))