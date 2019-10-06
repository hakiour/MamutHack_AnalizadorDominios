#!/usr/bin/env python3
print("Content-Type: text/html\n")
import mysql.connector
import json

MAXIMO_DOMINIOS_A_LISTAR = 4

mydb = mysql.connector.connect(
  host="localhost",
  user="terrassahash",
  passwd="HOMzOnzFaoBqvSk7",
  db="terrassahash",
  port=3306
)

def obtenerListadoDominios( maximoLineas):
    "Obtenemos los ultimos analisis realizados en nuestra bd"
    mycursor = mydb.cursor()
    mycursor.execute("SELECT nombreDominio FROM dominio ORDER BY fecha DESC LIMIT " + str(maximoLineas))

    resultado = []
    for item in mycursor:
        resultado.append(item);
    return resultado

resultado = {}

resultado["respuesta"] = obtenerListadoDominios(MAXIMO_DOMINIOS_A_LISTAR)

print(json.dumps(resultado))
