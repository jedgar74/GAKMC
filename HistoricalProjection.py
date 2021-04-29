#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 10:11:20 2021

@author: tauger
"""

from db.DBkm100 import *
import numpy as np
from Empresa import * 
from Estacion import * 
from IndAndVar import *
from datetime import datetime, timedelta
import sys
import matplotlib.pyplot as plt

class HistoricalProjection( ): 
    def __init__(self, param=None):  
        self.formato = "%Y-%m-%d"  
        self.db = DBkm100()
        
        if (not param == None): 
            self.readparam(param) 
        else:
            finitest = [2020, 11, 30]
            ffintest = [2020, 12,  6]
            # print(finitest.strftime(self.formato)) 
            # print(ffintest.strftime(self.formato)) 
            stations = ["Independencia" ]
            company = ["Nelly"]  
            weekstraining = 4 
            self.parameters = {"stations": stations,  "company": company, "weekstraining": weekstraining,   "finitest": finitest, "ffintest": ffintest, "prints": False }
  
        
    
    def setprints(self, prints):   
        self.parameters["prints" ] = prints  
 
    
    
    def setweekstraining(self, weekstraining):   
        self.parameters["weekstraining" ] = weekstraining  
       
       
               
    def setcompany(self, company):   
        self.parameters["company" ] = company            
    
            
            
    def setstations(self, stations):   
        self.parameters["stations" ] = stations 
        
        
        
    def setfinitest(self, finitest):   
        self.parameters["finitest" ] = finitest 
       
       
               
    def setffintest(self, ffintest):   
        self.parameters["ffintest" ] = ffintest     


    def readCat(self):   
        query = self.db.query("SELECT clase FROM km100.vehiculo v JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion ") 

        self.cat = [] 
        for t in query:
            try:
                r = self.cat.index(t[0])
                if  r == -1:
                    self.cat.append(t[0])            
            except:
                self.cat.append(t[0])      
#        print("***********")         
#        print(len(self.cat)) 
#        print(self.cat) 
                
                
                
    def readVehReg(self):         
        #* query = self.db.query("SELECT mva, clase, fecha_compra, km, id_modelo, id_categoria, anho, estatico, asignado, prestamo, contratado, cliente_prestamo, asignacion_estacion, alquilado, sin_movimiento, contrato_abierto, id_estacion, nombre, id_empresa FROM km100.vehiculo v JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion ") 
        query = self.db.query("SELECT chasis, clase, fecha_compra, km, id_modelo, id_categoria, anho, estatico, asignado, prestamo, contratado, cliente_prestamo, asignacion_estacion, alquilado, sin_movimiento, contrato_abierto, id_estacion, nombre, id_empresa FROM km100.vehiculo v JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion ") 

        infovehist = []
        
        for t in query:
            infovehist.append(t) 
        # print("***********")         
        # print(len(infovehist))  



    def readVehTotal(self):        
        totvehxcat = []
        # print("***********")  
        # print(self.cat)
        for j in range(len(self.estacion)): 
            # nam = "SELECT mva, clase, nombre FROM km100.vehiculo v JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion WHERE nombre = %s" 
            #* nam = "SELECT mva, clase, e.nombre , em.nombre   FROM km100.vehiculo v  JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s" 
            nam = "SELECT chasis, clase, e.nombre , em.nombre   FROM km100.vehiculo v  JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s" 
            query = self.db.query(nam, (self.estacion[j], self.empresa[j])) 
         
            cattmp = np.zeros(len(self.cat))
            for t in query: 
                try: 
                    r = self.cat.index(t[1])
                    cattmp[r] = cattmp[r] + 1            
                except:
                    pass
            # print(self.estacion[j], "-", self.empresa[j], cattmp)
            totvehxcat.append(cattmp)  
              
        # print(len(totvehxcat)) 
        

            
    def setCompStatCase(self, companyd, stationsd): 
        
        # consultamos en la base de datos estación, empresa y cliente
        self.readStation2() 
        
        
        # Verificamos primero el nombre de la empresa
        tmp = True
        empo= None
        for t in range(len(self.clientes)):  
            for j in range(self.clientes[t].nEmpresas()): 
                emp = self.clientes[t].getEmpresa(j)
                if  emp.name.replace(" ", "").lower() == companyd[0].replace(" ", "").lower():
                    tmp = False
                    empo = emp
                    self.parameters["company"] = [emp.name]
                    break
                
        if tmp :
            print() 
            print('************************************') 
            print("The requested company was not found, i.e.,", companyd)
            print('************************************\n')
            sys.exit() 
            
        tmpstations = []  
        for t in range(len(stationsd)): 
            
            tmp = True 
            for j in range(empo.nEstaciones()): 
                if  empo.getEstacion(j).replace(" ", "").lower() == stationsd[t].replace(" ", "").lower():
                    tmp = False
                    tmpstations.append(empo.getEstacion(j)) 
                    break  
                
            if tmp :
                print() 
                print('************************************') 
                print("The requested station was not found, i.e.,", stationsd[t])
                print('************************************\n') 
                
        self.parameters["stations"] = tmpstations      
    
    
    
    def setCompCase(self, companyd): 
        
        # consultamos en la base de datos estación, empresa y cliente
        self.readStation2()  
        
        # Verificamos primero el nombre de la empresa
        tmp = True
        empo= None
        for t in range(len(self.clientes)):  
            for j in range(self.clientes[t].nEmpresas()): 
                emp = self.clientes[t].getEmpresa(j)
                if  emp.name.replace(" ", "").lower() == companyd[0].replace(" ", "").lower():
                    tmp = False
                    empo = emp
                    self.parameters["company"] = [emp.name]
                    break
                
        if tmp :
            print() 
            print('************************************') 
            print("The requested company was not found, i.e.,", companyd)
            print('************************************\n')
            sys.exit() 
             
        self.parameters["stations"] = empo.getEstaciones() 
        
        
        
    def readStation2(self):   
        query = self.db.query("SELECT e.nombre, em.nombre, c.nombre_comercial FROM km100.estacion e JOIN km100.empresa em on em.id_empresa = e.id_empresa JOIN km100.cliente c on c.id = em.cliente_id") 
        
        self.labelestacion = []
        self.estacion = []
        self.empresa = []
        cliente = []
        
        self.clientes=[] 
        
        for t in query:
#            print(t)  
#            try:
            if len(self.clientes) == 0 :  
                emp = Empresa(t[1])
                emp.addEstacion(t[0]) 
                cli = Cliente(t[2])
                cli.addEmpresa(emp) 
                self.clientes.append(cli)   
                
            else :    
                addcli = True
                for j in range(len(self.clientes)):
#                    print(self.clientes[j].name) 
#                    print(t[2])
                    if self.clientes[j].name == t[2]: 
                        emp = Empresa(t[1]) 
                        emp.addEstacion(t[0]) 
                        self.clientes[j].addEmpresa(emp)
                        addcli = False
                        break 
                if addcli:
                    emp = Empresa(t[1])
                    emp.addEstacion(t[0]) 
                    cli = Cliente(t[2])
                    cli.addEmpresa(emp) 
                    self.clientes.append(cli) 
         
                    
#        print(len(self.clientes))             
        for t in range(len(self.clientes)):  
            for j in range(self.clientes[t].nEmpresas()): 
                emp = self.clientes[t].getEmpresa(j)
                for k in range(emp.nEstaciones()): 
                    cliente.append(self.clientes[t].name) 
                    self.empresa.append(emp.name) 
                    self.estacion.append(emp.getEstacion(k))
                    self.labelestacion.append(emp.getEstacion(k)+'('+emp.name+')')
                    # print(emp.getEstacion(k), '-',  emp.name, '-', self.clientes[t].name)
        # print("***********")             
        # print(len(self.estacion), len(self.empresa), len(cliente))   
        # print("-----------")  
        # print(self.estacion, self.empresa, cliente)
        # print("-----------")      


    def makedecision(self, prov, flag, statusX): 
        flagOnRent = 0
        kmCFleet = "NO MATCH"
        
        status = prov 
        flagOnRent = flag
        kmCFleet = statusX
        
        # Se toman como válidas las entradas de renta de alquiler 
        # solamente lo proveniente del proveedor. Las demás banderas 
        # se varían con respecto a flota histórica local
         
        if kmCFleet == 'Operativo' :
            status = 'AVAILABLE'
        elif kmCFleet == 'Taller' :
            status = 'In Maintenance' 
        # --- Revisar    
        elif kmCFleet == 'Salvamento' :
            status = 'UNAVAILABLE'              
        else : 
            # --- incluye Remarketing
            status = 'UNAVAILABLE'        
        
        
#        if flagOnRent == 1 : 
#            if kmCFleet == 'Taller' or kmCFleet == 'Operativo' :
#                status = 'On Rent'
#            else : 
#                status = 'On Rent'   
#        else :  
#            if kmCFleet == 'Operativo' :
#                status = 'AVAILABLE'
#            elif kmCFleet == 'Taller' :
#                status = 'In Maintenance' 
#            # --- Revisar    
#            elif kmCFleet == 'Salvamento' :
#                status = 'UNAVAILABLE'              
#            else : 
#                # --- incluye Remarketing
#                status = 'UNAVAILABLE'  
        # print('---4---', prov, ';', flag, ';', statusX, ';', status)        
                     
        return status 
     
    
    
    def checkemptydata(self, data):
        empty = False
       
        if len(data[0]) == 0 and len(data[1]) == 0 and len(data[2]) == 0:
            empty = True  
            
        return empty 



    def sortfordate(self, fecha, valores): 
       
        for i in range(len(fecha)-1):
            for j in range(i+1, len(fecha)):
                if fecha[i] > fecha[j]:
                     tmpf = fecha[i] 
                     fecha[i] = fecha[j]
                     fecha[j] = tmpf
                     for k in range(len(valores)): 
                         tmpv = valores[k][i] 
                         valores[k][i] = valores[k][j]
                         valores[k][j] = tmpv 
    
    
    
    def graphs(self, data, labl, stations, companies):
        #data = self.emptydata(data)
        
        for i in range(len(data)):   
            
            if self.checkemptydata(data[i]):
                continue
            
            fig, axs = plt.subplots(1, 2, sharex=False)
            (ax1, ax2) = axs
    
            to_plot = []
            nv = []
            for k in range(len(data[i][0])):
                o = np.array(data[i][2][k])
                # print(o) 
                to_plot.append(o)
                nv.append(k+1) 
 
            ax1.boxplot(to_plot)
            ax1.tick_params(labelrotation=-90)
            ax1.set_xticklabels(data[i][0])
            # ax1.xticks(nv, data[i][0])
 
            try:
                self.sortfordate(data[i][1], to_plot) 
                if len(to_plot) > 10 :   
                    ax2.plot(data[i][1], to_plot[10], label=data[i][0][10])    
                         
                if len(to_plot) > 9 :       
                    ax2.plot(data[i][1], to_plot[9], label=data[i][0][9])   
                    
                if len(to_plot) > 8 :       
                    ax2.plot(data[i][1], to_plot[8], label=data[i][0][8])   
                                        
                if len(to_plot) > 7 :       
                    ax2.plot(data[i][1], to_plot[7], label=data[i][0][7])   
                                        
                if len(to_plot) > 6 :       
                    ax2.plot(data[i][1], to_plot[6], label=data[i][0][6])   
                    
                if len(to_plot) > 5 :       
                    ax2.plot(data[i][1], to_plot[5], label=data[i][0][5])   
                                        
                if len(to_plot) > 4 :        
                    ax2.plot(data[i][1], to_plot[4], label=data[i][0][4])   
                                        
                if len(to_plot) > 3 :       
                    ax2.plot(data[i][1], to_plot[3], label=data[i][0][3]) 
                                        
                if len(to_plot) > 2 :       
                    ax2.plot(data[i][1], to_plot[2], label=data[i][0][2])   
                                        
                if len(to_plot) > 1 :       
                    ax2.plot(data[i][1], to_plot[1], label=data[i][0][1]) 
                                        
                if len(to_plot) > 0 :       
                    ax2.plot(data[i][1], to_plot[0], label=data[i][0][0])                    
                    
               
                ax2.tick_params(labelrotation=-90)
                ax2.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')               
                # plt.show()            
                # plt.ioff()
                
                
                fig.set_size_inches(18.5*0.8, 10.5*0.8)
                ax2.set_title(' '+stations[i]+'('+companies[i]+')')
                # axs.set_title(stations[i]+'('+companies[i]+')', loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
                # plt.close(fig) 
                # plt.savefig('figures/'+stations[i]+' '+labl+".png", bbox_inches='tight')
                plt.savefig('figures/'+stations[i]+'('+companies[i]+') '+labl+".png", bbox_inches='tight')
                
                # Define la posibilidad de imprimir en línea las gráficas
                # print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,", self.parameters["prints"])
                if self.parameters["prints"] == True: 
                    # print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
                    plt.show()
                
                plt.close(fig)
                
            except:  
                print("**********************") 
                print('printing error ')   
                print("**********************")
                print(stations[i])
                print(data[i][1])
                print(to_plot)
                print(data[i][0])
                pass    


    def sim(self, forecast=True): 
        
        print(self.parameters)  
        self.nsimulations  = 1             
        weeksimu = (self.nsimulations+self.parameters["weekstraining"])*7 
        finitest = datetime(self.parameters["finitest"][0], self.parameters["finitest"][1], self.parameters["finitest"][2], 0, 0, 0)
        ffintest = datetime(self.parameters["ffintest"][0], self.parameters["ffintest"][1], self.parameters["ffintest"][2], 0, 0, 0)
#        print(finitest.strftime(self.formato)) 
#        print(ffintest.strftime(self.formato)) 
        feini = finitest - timedelta(days=(self.nsimulations+self.parameters["weekstraining"]-1)*7)
        fefin = ffintest - timedelta(days=(self.nsimulations)*7)  
#        print(feini.strftime(self.formato)) 
#        print(fefin.strftime(self.formato)) 

        
        mantenimiento = ['CHEQUEO', 'In Maintenance', 'STOP'] 
        disponibilidad = ['DISPONIBLE', 'AVAILABLE', '0', 'Non-Rev. Transfer'] 
            
        db2 = DBkm100() 
        self.nsimulations = 1
        
        # ejecutamos el número de simulaciones
        for k in range(self.nsimulations):
            print("**********************")   
            print("**********************") 
            print('simulation: ', k)   
            print("**********************") 
            print("**********************")   
            fpini = fefin + timedelta(days=1)
            fpfin = fefin + timedelta(days=7)
            print(feini.strftime(self.formato)) 
            print(fefin.strftime(self.formato))    
            print(fpini.strftime(self.formato)) 
            print(fpfin.strftime(self.formato))
            
            
            stations = []
            infoStations = []   
            self.onRentData = []  
            
            
            print('\n\n---Training---', feini.strftime(self.formato), fefin.strftime(self.formato))   
            
            for w in range(len(self.parameters["stations"])): 
                
                # obtenemos Los indicadores de cada estación por grupo a partir de la
                # Data histórica
                #* nam = "SELECT kmbi.flota_historica_proveedor.mva, v.id  , descripcion_estado, fecha , clase FROM kmbi.flota_historica_proveedor JOIN km100.vehiculo v on v.mva= kmbi.flota_historica_proveedor.mva JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s AND kmbi.flota_historica_proveedor.fecha BETWEEN %s AND %s"  
                nam = "SELECT kmbi.flota_historica_proveedor.chasis, v.id  , descripcion_estado, fecha , clase FROM kmbi.flota_historica_proveedor JOIN km100.vehiculo v on v.chasis= kmbi.flota_historica_proveedor.chasis JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s AND kmbi.flota_historica_proveedor.fecha BETWEEN %s AND %s"  
                query = self.db.query(nam, (self.parameters["stations"][w], self.companies[w], feini.strftime(self.formato), fefin.strftime(self.formato), )) 
                print('---1---', self.parameters["stations"][w]+'('+self.companies[w]+')', feini.strftime(self.formato)) 
                
                # vehvma = []
                # veh_id = []
                his = []    
                estmp = []        
                es = Estacion(self.parameters["stations"][w]+'('+self.companies[w]+')')
                
                for t in query:
                    #  print(t)  
                    #  print('---2---', t[0], t[1], t[4], t[3], t[2]) 
                    if es.gets(t[0]):
                        # t[0] chasis
                        # t[3] fecha
                        # t[2] estado
                        if t[2] == None: 
                            print(t[0], t[3], 'UNKNOWN')
                            es.addD(t[0], t[3], 'UNKNOWN')
                        else:    
                            es.addD(t[0], t[3], t[2].strip(" ")) 
                    else :        
                        es.add2(t[0], t[1], t[4], t[3], t[2].strip(" ")) 
                    his.append(t)    
                      
                        
                #* nam2 = "SELECT v.mva, fh.bandera_renta, fh.nombre_estado, fh.fecha FROM km100.vehiculo v JOIN kmbi.flota_historica fh on v.id = fh.id_vehiculo JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s AND  fh.fecha BETWEEN %s AND %s"
                nam2 = "SELECT v.chasis, fh.bandera_renta, fh.nombre_estado, fh.fecha FROM km100.vehiculo v JOIN kmbi.flota_historica fh on v.id = fh.id_vehiculo JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s AND  fh.fecha BETWEEN %s AND %s"
                query2 = db2.query(nam2, (self.parameters["stations"][w], self.companies[w], feini.strftime(self.formato), fefin.strftime(self.formato), )) 
               
        
                for tv in query2: 
                    # print(tv)  
                    # print('---3---', tv[0], tv[1], tv[3], tv[2]) 
                    mkstatus = self.makedecision(" ", tv[1], tv[2]) 
                    es.compare2(tv[0], tv[3], mkstatus) 
                         
                        
                # es.prints2()  
                # print("000000 ", es.idveh) 
                estmp.append(es.indtip())   
                estmp.append(es.indtipc())   
                estmp.append(es.indtipg(mantenimiento))  
                estmp.append(es.indtipg(disponibilidad))  
                estmp.append(es.indtipg(['On Rent', 'AVAILABLE']))   
                estmp.append(es.indtipg(['On Rent', 'AVAILABLE', 'In Maintenance' ]))  
                estmp.append(es.indtiplap(['On Rent']))   
                
                stations.append(es) 
                # Verificamos Qué es la estación haya tenido datos si no tiene datos 
                # se asigna un conjunto vacío, asignado al grupo de vehículo none 
#                if len(estmp[0][0]) ==0:
#                    estmp = [[['None'], [1]],  [[0], [0.0], [0.0]],  [[0], [0.0], [0.0]],  [[0], [0.0], [0.0]],  [[0], [0.0], [0.0]],  [[0], [0.0], [0.0]],  [0, [[0]], [[0]], [[0]], [[0.0]], [[0]]]  ]
                infoStations.append(estmp)  
                self.onRentData.append(es.onRentToGraph()) 
            
            typesOfVehicles   = [ ]
            infoTraining = IndAndVar()
            infoTraining.setInstance(feini.strftime(self.formato), fefin.strftime(self.formato), stations, typesOfVehicles, infoStations)
            
            if infoTraining.verifydata() == True:
                print() 
                print('************************************') 
                print("You do not have data in the requested time interval, i.e.,", feini.strftime(self.formato), fefin.strftime(self.formato))
                print('************************************\n')
                sys.exit()
                 
            infoTraining.prints( )   
             
            self.graphs(self.onRentData, 'T ' +feini.strftime(self.formato)+ ' '+ fefin.strftime(self.formato), self.parameters["stations"], self.companies)   
             
            
             
            # ------------
            # actualizar fechas
            # ------------     
            feini = feini + timedelta(days=7)
            fefin = fefin + timedelta(days=7)




    def run(self, forecast=True):   
        # ...............................
        # Paso 1. leer Data 
        # definimos la clase para conectarnos a la base de datos
        # ...............................
        
        self.readStation2()
        self.readCat()
        self.readVehReg()
        self.readVehTotal()
        
        
        # ...............................
        # Paso 2: definimos el grupo de estaciones sobre las que se va 
        # aplicar el algoritmo, el número de simulaciones, lapso de 
        # entrenamiento y lapso de  prueba
        # ...............................
        
        if  len(self.parameters["stations"]) > -1: 
            self.companies = self.parameters["company"]*len(self.parameters["stations"])
            # print(self.companies) 
        else:
            self.companies = self.parameters["company"]
            
        self.sim(forecast)        
       
