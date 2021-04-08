#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 17:15:33 2021
genera un archivo .csv para ser introducido en los mecanismos de 
aprendizaje automático
@author: tauger
"""
import os
import mysql.connector

conexion2=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="090509", 
                                  database="kmbi")   
conn2=conexion2.cursor()
query = ("SELECT fh.id  , fh.id_estado , id_vehiculo,  fh.nombre_estado ,fh.id_estacion, fh.id_empresa,  fh.fecha,  fhp.mva, fhp.id_estado, fhp.descripcion_estado, fhp.fecha, v.categoria, v.clase FROM kmbi.flota_historica fh JOIN km100.vehiculo v on v.id =fh.id_vehiculo  JOIN kmbi.flota_historica_proveedor fhp on v.mva= fhp.mva  JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion  JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE v.mva='18SP1012'  AND  e.nombre = 'Independencia' AND em.nombre = 'Nelly'  AND fh.fecha BETWEEN '2020-11-30' AND '2020-12-06' ") 
 
conn2.execute(query) 

 
file = open("./filenamee.csv", "w")
file.write("fh.id  , fh.id_estado , id_vehiculo,  fh.nombre_estado ,fh.id_estacion, fh.id_empresa,  fh.fecha,  fhp.mva, fhp.id_estado, fhp.descripcion_estado, fhp.fecha, v.categoria, v.clase" ) 
file.write('\n') 
for tabla in conn2:
    print(tabla)
    for t in range(len(tabla)):   
        txt = str(tabla[t])
        file.write(", " + txt.replace(',', '-') ) 
    file.write('\n')  
    
file. close()
conexion2.close()   