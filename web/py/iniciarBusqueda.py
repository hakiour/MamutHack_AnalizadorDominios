#!C:\Users\localadmin\Anaconda3\python.exe
print("Content-Type: text/html\n")
import csv
import linkDownload as ld
import cgi
import conexion as conexion

def csv2Dict(fichero):
    with open(fichero) as f:
        rd = csv.DictReader(f)
    
        for row in rd:
            nuevo=dict(row)
    f.close()
    return nuevo


def CalculaScore():
    datosForm = cgi.FieldStorage()

    if datosForm:
        url = datosForm["url"].value
        arrayUrl = (url.split("//"))
        if len(arrayUrl) == 2: 
            url = arrayUrl[1]
        else: 
            return 'Error url'

        tema = datosForm["tema"].value

    url = "https://www.lavanguardia.com/"
    tema="racismo"

    DicOdio = csv2Dict(tema+".csv") #'/Dicts/'+'

    busqueda = ld.readLinks(url, tema)

    ArrInter=[]
  
    for link in busqueda["LINKS"]:
        objLink = busqueda["LINKS"][link]
        ArrInter = list(DicOdio.keys() & objLink[link].keys())
        for palabraClave in ArrInter:
            objLink["PUNTUACION"] += objLink[link][palabraClave]  
        #paraulesOrd = sorted(objLink[link].items(), key=lambda kv: kv[1])
        #objLink[link] = collections.OrderedDict(paraulesOrd)       
    return busqueda

resultado = CalculaScore()

#conectamos la BDD
mydb = conexion.iniciarBD()
mycursor = mydb.cursor()
sql="INSERT INTO dominio (nombreDominio, tematica) VALUES (%s,%s);"
val = (resultado["DOMINI"],resultado["TEMATICA"])

mycursor.execute(sql,val)
mydb.commit()


#sql = "INSERT INTO LINK (nombreLink,indice) VALUES (%s,%d)"
#val = resultado["LINKS"]
print("Valores de Dominio y Tematica insertados")
