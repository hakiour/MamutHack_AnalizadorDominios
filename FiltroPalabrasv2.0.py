#!C:/Users/sergi/AppData/Local/Programs/Python/Python37-32/python.exe

import csv
import sys
import linkDownload as ld
import cgi

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

    #url = "https://www.lavanguardia.com/"
    #tema="racismo"

    DicOdio = csv2Dict(tema+".csv") #'/Dicts/'+'
    print(DicOdio)
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


        
CalculaScore()