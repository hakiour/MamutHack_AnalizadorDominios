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

    #if datosForm:
    #    url = datosForm["url"].value
    #    arrayUrl = (url.split("//"))
    #    if len(arrayUrl) == 2: 
    #        url = arrayUrl[1]
    #    else: 
    #        return 'Error url'

    #    tema = datosForm["tema"].value

    tema = 'racismo'
    url = "https://www.lavanguardia.com"

    DicOdio = csv2Dict(tema+".csv") #'/Dicts/'+'
    busqueda = ld.readLinks(url, tema)
    ArrInter=[]

    for url in busqueda["LINKS"]:
        ArrInter = list(DicOdio.keys() & busqueda["LINKS"][url]["PALABRAS"].keys())
        print(ArrInter)
        for palabraClave in ArrInter:
            if palabraClave in busqueda["LINKS"][url]["PALABRAS"].keys():
                busqueda["LINKS"][url]["PUNTUACION"] += busqueda["LINKS"][url]["PALABRAS"][palabraClave]
    return busqueda


        
CalculaScore()