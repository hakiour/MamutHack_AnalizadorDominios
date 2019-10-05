#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 23:54:38 2019

@author: danielortega
"""
import csv

def csv2Dict(fichero):
    with open(fichero) as f:
        rd = csv.DictReader(f)
        for row in rd:
            nuevo=dict(row)
    f.close()
    return nuevo

def readLinks():
    busq = {"DOM": "https://www.lavanguardia.com/",
            "LINK": {"https://www.lavanguardia.com/home":{"palabras":{"negro":2,"matar":4,"suicidio":8},"puntuacion":0},
                     "https://www.lavanguardia.com/index":{"palabras":{"dispara":2,"paliza":4,"nazi":8},"puntuacion":0}},
            "TEMATICA":"racismo"}
    return busq

fichero = "/Users/danielortega/Documents/Proyectos/MamutHack/MamutHack_AnalizadorDominios/diccionario2.csv"
fichero2 = "/Users/danielortega/Documents/Proyectos/MamutHack/MamutHack_AnalizadorDominios/test.json"

DiccMalas = csv2Dict(fichero)
busqueda = readLinks() #funcion que nos retornara un diccionario de busquedas
#for palabrasMalas in DiccMalas:
    #if palabrasMalas in busqueda["LINK"]["https://www.lavanguardia.com/home"]["palabras"]:
        #print(palabrasMalas)#busqueda["LINK"]["https://www.lavanguardia.com/home"]["puntuacion"].value()+=busqueda["LINK"]["https://www.lavanguardia.com/home"]["palabras"].value()
    #print (busqueda["LINK"]["https://www.lavanguardia.com/home"]["puntuacion"])
#print(busqueda["LINK"]["https://www.lavanguardia.com/home"]["palabras"].items())
ArrInter=[]
valores = 0
for url in busqueda["LINK"]:
    ArrInter = list(DiccMalas.keys() & busqueda["LINK"][url]["palabras"].keys())
    for palabraClave in ArrInter:
        if palabraClave in busqueda["LINK"][url]["palabras"].keys():
            busqueda["LINK"][url]["puntuacion"] += busqueda["LINK"][url]["palabras"][palabraClave]
    print(busqueda)