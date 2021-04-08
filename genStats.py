#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:32:28 2021
Genera estadísticas de los grupos de vehículos por lapsos de fecha 
determinados para una determinada Estación
@author: tauger

"""

import mysql.connector
import pandas as pd
import numpy as np
from Estacion import * 

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="090509", 
                                  database="km100")
conn=conexion1.cursor()
conn.execute("show tables")
for tabla in conn:
    print(tabla)
    
#query = ("SELECT first_name, last_name, hire_date FROM employees "
#         "WHERE hire_date BETWEEN %s AND %s")
#
#hire_start = datetime.date(1999, 1, 1)
#hire_end = datetime.date(1999, 12, 31)
#
#cursor.execute(query, (hire_start, hire_end))
#
#for (first_name, last_name, hire_date) in cursor:
#  print("{}, {} was hired on {:%d %b %Y}".format(
#    last_name, first_name, hire_date))
#query = ("SELECT * FROM km100.user") 
#conn.execute(query)    
#for tabla in conn:
#    print(tabla)
#    
    

conexion2=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="090509", 
                                  database="kmbi")   

# Número de estaciones y nombres 
conn2=conexion1.cursor()
query = ("SELECT estacion.nombre FROM estacion") 
conn2.execute(query)  

estacion = []

# Calculamos las estaciones
for tabla in conn2:
    print(tabla)  
    try:
        r = estacion.index(tabla[0])
        if  r == -1:
            estacion.append(tabla[0])
            print(estacion)        
    except:
            estacion.append(tabla[0])
            print(estacion)
print(len(estacion))  

# clase registrada vehículos
query = ("SELECT clase FROM km100.vehiculo v JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion ") 
conn2.execute(query) 
cat = [] 
for tabla in conn2:
    try:
        r = cat.index(tabla[0])
        if  r == -1:
            cat.append(tabla[0])            
    except:
        cat.append(tabla[0])          
print(len(cat)) 
print(cat) 


# vehículos registrados
query = ("SELECT mva, clase, fecha_compra, km, id_modelo, id_categoria, anho, estatico, asignado, prestamo, contratado, cliente_prestamo, asignacion_estacion, alquilado, sin_movimiento, contrato_abierto, id_estacion, nombre, id_empresa FROM km100.vehiculo v JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion ") 
conn2.execute(query)  

dvsol = []

for tabla in conn2:
    # print(tabla)  
    dvsol.append(tabla)  
    # print("---")    
print(len(dvsol))  


dvest = []

for t in range(len(estacion)):
    # print("---")
    nam = "SELECT mva, clase, nombre FROM km100.vehiculo v JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion WHERE nombre = %s" 
    query = (nam) 
    conn2.execute(query, (estacion[t],))  
    dft= np.zeros(len(cat))
    for tabla in conn2: 
        try:
            # print("---")
            r = cat.index(tabla[1])
            dft[r] = dft[r] + 1            
        except:
            pass
    # print(dft)
    dvest.append(dft) 
# print(dvest)            
      
print(len(dvest)) 


fi=['2020-08-31', '2020-09-07', '2020-09-14', '2020-09-21', '2020-09-28', '2020-10-05', '2020-10-12', '2020-10-19', '2020-10-26', '2020-11-02', '2020-11-09', '2020-11-16', '2020-11-23', '2020-11-30', '2020-11-07', '2020-12-14', '2020-12-21'] 
ff=['2020-09-06', '2020-09-13', '2020-09-20', '2020-09-27', '2020-10-04', '2020-10-11', '2020-10-18', '2020-10-25', '2020-11-01', '2020-11-08', '2020-11-15', '2020-11-22', '2020-11-29', '2020-12-06', '2020-12-13', '2020-12-20', '2020-12-27'] 
#fi=['2020-08-10', '2020-08-17', '2020-08-24', '2020-08-31', '2020-09-07', '2020-09-14', '2020-09-21', '2020-09-28', '2020-10-05', '2020-10-12', '2020-10-19', '2020-10-26', '2020-11-02', '2020-11-09', '2020-11-16', '2020-11-23', '2020-11-30'] 
#ff=['2020-08-30', '2020-09-06', '2020-09-13', '2020-09-20', '2020-09-27', '2020-10-04', '2020-10-11', '2020-10-18', '2020-10-25', '2020-11-01', '2020-11-08', '2020-11-15', '2020-11-22', '2020-11-29', '2020-12-06', '2020-12-13', '2020-12-20'] 

df = []
for v in range(len(fi)):   
    dr = []
    # Incluir  datos históricos
    # query = ("SELECT kmbi.flota_historica_proveedor.mva, id_estado ,  descripcion_estado, fecha ,   id_ubicacion_actual ,   id_ubicacion_traslado,      categoria,   clase exactus,   id_modelo,   asignado,   contratado,   asignacion_estacion,   alquilado,   sin_movimiento ,  contrato_abierto,   id_estacion,   nombre,   id_empresa FROM kmbi.flota_historica_proveedor JOIN km100.vehiculo v on v.mva= kmbi.flota_historica_proveedor.mva JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion WHERE (nombre = %s  OR nombre = %s ) AND kmbi.flota_historica_proveedor.fecha BETWEEN '2020-11-02' AND '2020-11-29'") 
    query = ("SELECT kmbi.flota_historica_proveedor.mva, id_estado ,  descripcion_estado, fecha ,   id_ubicacion_actual ,   id_ubicacion_traslado,      categoria,   clase, exactus,   id_modelo,   asignado,   contratado,   asignacion_estacion,   alquilado,   sin_movimiento ,  contrato_abierto,   id_estacion,   nombre,   id_empresa FROM kmbi.flota_historica_proveedor JOIN km100.vehiculo v on v.mva= kmbi.flota_historica_proveedor.mva JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion WHERE nombre = %s AND kmbi.flota_historica_proveedor.fecha BETWEEN %s AND %s") 
    # conn2.execute(query, ('independencia', 'Independencia',))  
    conn2.execute(query, ('Independencia', fi[v], ff[v], )) 

    es = Estacion('Independencia')
    his = []
    for tabla in conn2:
        # print(tabla)  
        if es.gets(tabla[0]):
            es.addD(tabla[0], tabla[3], tabla[2].strip(" ")) 
        else :        
            es.add(tabla[0], tabla[7], tabla[3], tabla[2].strip(" ")) 
        his.append(tabla)
        # print("---")    
    # es.prints()  
    print('Nombre de estación  ', es.name)
    print('Número de vehículos ', len(es.a)) 
    print("---", fi[v], ff[v])
    
    es.indtip() 
    dr.append(es.name) 
    dr.append(fi[v]) 
    dr.append(ff[v]) 
    dr.append(es.ntip) 
    dr.append(es.tip) 
    print("---ON RENT")
    es.indtipc() 
    dr.append("---ON RENT")
    dr.append(es.tipc)
    dr.append(es.tipd)
    dr.append(es.tipe)
    # print("*** ", es.tipe)
    print("---CHEQUEO")
    es.indtipg( ['CHEQUEO', 'In Maintenance'])
    dr.append("---CHEQUEO")
    dr.append(es.tipc)
    dr.append(es.tipd)
    dr.append(es.tipe)
    print("---DISPONIBLE") 
    es.indtipg( ['DISPONIBLE', 'AVAILABLE', '0', 'Non-Rev. Transfer'])
    dr.append("---DISPO")
    dr.append(es.tipc)
    dr.append(es.tipd)
    dr.append(es.tipe)
    df.append(dr)    
# estmp.append(es.tipc) 
# estmp.append(es.tipd)   

#df = pd.DataFrame(conn2, columns = [])  
#df.to_excel('example.xlsx', sheet_name='example')    +++
#
##Definir la Data de comprobación
#query = ("SELECT kmbi.flota_historica_proveedor.mva, id_estado ,  descripcion_estado, fecha ,   id_ubicacion_actual ,   id_ubicacion_traslado,      categoria,   clase exactus,   id_modelo,   asignado,   contratado,   asignacion_estacion,   alquilado,   sin_movimiento ,  contrato_abierto,   id_estacion,   nombre,   id_empresa   FROM kmbi.flota_historica_proveedor JOIN km100.vehiculo v on v.mva= kmbi.flota_historica_proveedor.mva JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion WHERE kmbi.flota_historica_proveedor.fecha  BETWEEN '2020-11-30' AND '2020-12-06'") 
#conn2.execute(query)  
#
#ver = []
#for tabla in conn2:
#    print(tabla)  
#    ver.append(tabla)
#    print("---")    
#print(len(ver))  
#
# 
#ivn = [] 
#ivc = []
#for a in his:
#    for t in estacion:
#        try:
#            print(a[0]) 
#            r = ivn.index(a[0]) 
#            if  r == -1:
#                ivn.append(a[0]) 
#                ivc.append(1)
#            else: 
#                ivc[r] == ivc[r] +1   
#        except:
#            pass
#print(ivn)             
#print(ivc)       

#Calcular el número de vehículos por estación
    
for v in range(len(df)):  
    dr = df[v]
    for i in range(len(dr)):   
        print(dr[i], end =" ")
    print('\n')    
    print('\n') 
conexion2.close()     
    
conexion1.close()  



  