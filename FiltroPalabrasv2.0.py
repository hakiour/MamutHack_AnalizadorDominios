#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import sys
import linkDownload as ld

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
        print('Error url')
        return 0

    tema = datosForm["tema"].value

    DicOdio = csv2Dict(tema+".csv") #'/Dicts/'+'
    busqueda = ld.readLinks(url, tema)
    ArrInter=[]
    for link in busqueda["LINKS"]:
        objLink = busqueda["LINKS"][link]
        ArrInter = list(DicOdio.keys() & objLink[link].keys())
        for palabraClave in ArrInter:
            objLink["PUNTUACION"] += objLink[link][palabraClave]
                
    return busqueda


print(CalculaScore())