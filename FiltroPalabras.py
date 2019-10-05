# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''

'''
import csv
import numpy as np
import json
##leemos el fichero y transformamos en un array
"""dataArr = []
def csvToArray(fichero):
    
    with open(fichero) as csvFichero:
        data = csv.reader(csvfichero)

    for palabra in data:
        dataArr.append(palabra)
    
    
    
     array = []
    with open(fichero2, "r") as json:
        array = json.load(fichero2)
        
        for i in range(len(array)):
            print(array[i])
    
    print(dataArr)
    return dataArr
    print(data)

##
    """
def csv2Dict(fichero):
    with open(fichero) as f:
        rd = csv.DictReader(f)
        """if "bonito" in row.keys():
                print("encontrado")
            else: print("no sta")
        
        """
        for row in rd:
            nuevo=dict(row)
        print(nuevo)
    f.close()
    return nuevo


           
def json2Array(fichero2):
    array = []
    with open(fichero2, "r") as read_file:
        objeto = json.load(read_file)
        array = objeto["lista"]
    return array


fichero = "/Users/danielortega/Documents/Proyectos/MamutHack/MamutHack_AnalizadorDominios/diccionario2.csv"
fichero2 = "/Users/danielortega/Documents/Proyectos/MamutHack/MamutHack_AnalizadorDominios/test.json"
#csv2Dict(fichero)
palabrasPagina = []
DiccEnArr = []
palabrasPaginas = json2Array(fichero2)
DiccEnArr = csv2Dict(fichero)
index = 0
for palabra in palabrasPaginas:
    if palabra in DiccEnArr:
        #index+=int(DiccEnArr.get(palabra))
        print(palabra)
        #intersection




