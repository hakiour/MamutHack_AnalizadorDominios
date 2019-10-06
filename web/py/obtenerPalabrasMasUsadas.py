#!C:\Users\localadmin\Anaconda3\python.exe
print("Content-Type: text/html\n")
import json
import conexion

MAXIMOS_PALABRAS_A_LISTAR = 12

mydb = conexion.iniciarBD()

def obtenerPalabrasMasUsadas( maximoLineas):
    "Obtenemos las palabras con más iteraciones"
    mycursor = mydb.cursor()
    mycursor.execute("SELECT palabra FROM palabras GROUP BY palabra HAVING SUM(numeroVeces) ORDER BY numeroVeces DESC LIMIT " + str(maximoLineas))

    resultado = []
    for item in mycursor:
        resultado.append(item);
    return resultado

resultado = {}

resultado["respuesta"] = obtenerPalabrasMasUsadas(MAXIMOS_PALABRAS_A_LISTAR)

print(json.dumps(resultado))
