#!C:\Users\localadmin\Anaconda3\python.exe
print("Content-Type: text/html\n")
import conexion
import json

mydb = conexion.iniciarBD()

def obtenerListadoDominios( maximoLineas):
    "Obtenemos los ultimos analisis realizados en nuestra bd"
    mycursor = mydb.cursor()
    mycursor.execute("SELECT nombreDominio FROM dominio ORDER BY fecha DESC LIMIT " + str(maximoLineas))

    resultado = []
    for item in mycursor:
        resultado.append(item);
    return resultado

resultado = {}

resultado["respuesta"] = obtenerListadoDominios(4)

print(json.dumps(resultado))
