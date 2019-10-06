#!C:\Users\localadmin\Anaconda3\python.exe
print("Content-Type: text/html\n")

import mysql.connector
import json
import cgi

MAXIMO_DOMINIOS_A_LISTAR = 4

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
mycursor.execute("SELECT trim(nombreLink) as nombreLink, indice FROM link WHERE idDominio = " + idDominio + " LIMIT 7")

resultado = []

for item in mycursor:
    resultado.append(item)

jsonString = {}

jsonString["respuestaLinks"] = resultado

print(json.dumps(jsonString))