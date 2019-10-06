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
        busqueda = ld.readLinks(url)
        ArrInter=[]
        for url in busqueda["LINKS"]:
            ArrInter = list(DiccMalas.keys() & busqueda["LINKS"][url]["palabras"].keys())
            for palabraClave in ArrInter:
                if palabraClave in busqueda["LINKS"][url]["palabras"].keys():
                    busqueda["LINKS"][url]["puntuacion"] += busqueda["LINKS"][url]["palabras"][palabraClave]

        return busqueda
    else:
        print("Input error")
        return None

CalculaScore()