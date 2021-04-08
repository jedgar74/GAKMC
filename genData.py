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
query = ("SELECT kmbi.flota_historica_proveedor.mva, id_estado, descripcion_estado, fecha ,   id_ubicacion_actual ,   id_ubicacion_traslado, categoria, clase, exactus, id_modelo,   asignado,   contratado,   asignacion_estacion,   alquilado,   sin_movimiento ,  contrato_abierto,   id_estacion,   e.nombre,   e.id_empresa FROM kmbi.flota_historica_proveedor JOIN km100.vehiculo v on v.mva= kmbi.flota_historica_proveedor.mva JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa  WHERE kmbi.flota_historica_proveedor.fecha BETWEEN '2020-11-02' AND '2020-11-29'") 
# conn2.execute(query, ('independencia', 'Independencia',))  
conn2.execute(query) 

 
file = open("./filename.csv", "w")
file.write("mva, id_estado, descripcion_estado, fecha ,   id_ubicacion_actual ,   id_ubicacion_traslado, categoria, clase, exactus, id_modelo,   asignado,   contratado,   asignacion_estacion,   alquilado,   sin_movimiento ,  contrato_abierto,   id_estacion,   e.nombre,  id_empresa" ) 
file.write('\n') 
for tabla in conn2:
    print(tabla)
    for t in range(len(tabla)):   
        txt = str(tabla[t])
        file.write(", " + txt.replace(',', '-') ) 
    file.write('\n')  
    
file. close()
conexion2.close()   