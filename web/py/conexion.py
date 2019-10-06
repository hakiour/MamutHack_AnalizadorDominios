# -*- coding: utf-8 -*-

import mysql.connector
def iniciarBD():
    mydb = mysql.connector.connect(
      host="localhost",
      user="terrassahash",
      passwd="HOMzOnzFaoBqvSk7",
      db="terrassahash",
      port=3306
    )
    return mydb