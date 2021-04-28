#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 08:19:50 2021

@author: tauger
"""

from datetime import datetime, timedelta
from db.DBkm100 import *
import numpy as np
from Estacion import * 
from IndAndVar import *
from problem.CarRentalFleetR3 import *
from algorithm.Entity import *
import sys
import matplotlib.pyplot as plt
from Empresa import * 



class Simulation ( ): 
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
            nsimulations = 1       
            weekstraining = 4
            fileconfigGA = "GARF2" 
            evalsGA = 5000 
            expGA = 10 
            self.parameters = {"stations": stations,  "company": company, "nsimulations": nsimulations, "weekstraining": weekstraining,   "finitest": finitest, "ffintest": ffintest,  "fileconfigGA": fileconfigGA,  "evalsGA": evalsGA,  "expGA": expGA,  "prints": False }
  
    
    def setprints(self, prints):   
        self.parameters["prints" ] = prints 
        

    
    def setevalsGA(self, evalsGA):   
        self.parameters["evalsGA" ] = evalsGA 
        
        
        
    def setfileconfigGA(self, fileconfigGA):   
        self.parameters["fileconfigGA" ] = fileconfigGA 
       
       
               
    def setexpGA(self, expGA):   
        self.parameters["expGA" ] = expGA 
        
        
        
    def setweekstraining(self, weekstraining):   
        self.parameters["weekstraining" ] = weekstraining 
        
        
        
    def setnsimulations(self, nsimulations):   
        self.parameters["nsimulations" ] = nsimulations
       
       
               
    def setcompany(self, company):   
        self.parameters["company" ] = company            
    
            
            
    def setstations(self, stations):   
        self.parameters["stations" ] = stations 
        
        
        
    def setfinitest(self, finitest):   
        self.parameters["finitest" ] = finitest 
       
       
               
    def setffintest(self, ffintest):   
        self.parameters["ffintest" ] = ffintest     



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
        
        
        
    def readparam(self, param):   
        self.parameters = param
        # print(self.parameters) 
       
        
            
    def readStation(self):   
        query = self.db.query("SELECT e.nombre, em.nombre, c.nombre_comercial FROM km100.estacion e JOIN km100.empresa em on em.id_empresa = e.id_empresa JOIN km100.cliente c on c.id = em.cliente_id") 
         
        self.estacion = []
        self.empresa = []
        cliente = []
        
        for t in query:
            # print(t)  
            try:
                r = self.estacion.index(t[0])
                if  r == -1:
                    self.estacion.append(t[0])
                    self.empresa.append(t[1])
                    cliente.append(t[2])  
            except:
                    self.estacion.append(t[0])
                    self.empresa.append(t[1])
                    cliente.append(t[2])    
        # print("***********")             
        # print(len(self.estacion), len(self.empresa), len(cliente))   
        # print("-----------")  
        # print(self.estacion, self.empresa, cliente)
        print("-----------")  
        print(len(self.estacion))  
    


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
        query = self.db.query("SELECT mva, clase, fecha_compra, km, id_modelo, id_categoria, anho, estatico, asignado, prestamo, contratado, cliente_prestamo, asignacion_estacion, alquilado, sin_movimiento, contrato_abierto, id_estacion, nombre, id_empresa FROM km100.vehiculo v JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion ") 

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
            nam = "SELECT mva, clase, e.nombre , em.nombre   FROM km100.vehiculo v  JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s" 
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
    


    def emptydata(self, data):
        rdata = data 
        if len(data) > 1:
            i = 0
            while i < len(rdata): 
                if len(rdata[i][0]) == 0 and len(rdata[i][1]) == 0 and len(rdata[i][2]) == 0:
                    rdata.pop(i)
                else:
                    i = i+1 
            
        return rdata
    
    
    
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
                    
#                if len(to_plot) == 1 :
#                    # ax2.plot(data[0][1], to_plot[0])
##                    print(stations[i])
##                    print(data[i][1])
##                    print(to_plot)
##                    print(data[i][0])
#                    ax2.plot(data[i][1], to_plot[0], label=data[i][0][0])	
#                    
#                elif len(to_plot) == 2 :
#                    # ax2.plot(data[0][1], to_plot[0], data[0][1], to_plot[1])	
#                    ax2.plot(data[i][1], to_plot[0], label=data[i][0][0])
#                    ax2.plot(data[i][1], to_plot[1], label=data[i][0][1])  
#                elif len(to_plot) == 3 :
#                    # ax2.plot(data[0][1], to_plot[0], data[0][1], to_plot[1], data[0][1], to_plot[2])	
#                    ax2.plot(data[i][1], to_plot[0], label=data[i][0][0])
#                    ax2.plot(data[i][1], to_plot[1], label=data[i][0][1])
#                    ax2.plot(data[i][1], to_plot[2], label=data[i][0][2])         
#                elif len(to_plot) == 4 :
#                    # ax2.plot(data[0][1], to_plot[0], data[0][1], to_plot[1], data[0][1], to_plot[2], data[0][1], to_plot[3])			
#                    ax2.plot(data[i][1], to_plot[0], label=data[i][0][0])
#                    ax2.plot(data[i][1], to_plot[1], label=data[i][0][1])
#                    ax2.plot(data[i][1], to_plot[2], label=data[i][0][2]) 
#                    ax2.plot(data[i][1], to_plot[3], label=data[i][0][3])		
#                
#                elif len(to_plot) == 5 :
#                    # ax2.plot(data[0][1], to_plot[0], data[0][1], to_plot[1], data[0][1], to_plot[2], data[0][1], to_plot[3], data[0][1], to_plot[4])
#                    ax2.plot(data[i][1], to_plot[0], label=data[i][0][0])
#                    ax2.plot(data[i][1], to_plot[1], label=data[i][0][1])
#                    ax2.plot(data[i][1], to_plot[2], label=data[i][0][2]) 
#                    ax2.plot(data[i][1], to_plot[3], label=data[i][0][3])	 
#                    ax2.plot(data[i][1], to_plot[4], label=data[i][0][4])        
#                elif len(to_plot) == 6 :
#                    # ax2.plot(data[0][1], to_plot[0], data[0][1], to_plot[1], data[0][1], to_plot[2], data[0][1], to_plot[3], data[0][1], to_plot[4], data[0][1], to_plot[5])
#                    print(data[i][1])
#                    ax2.plot(data[i][1], to_plot[0], label=data[i][0][0])
#                    ax2.plot(data[i][1], to_plot[1], label=data[i][0][1])
#                    ax2.plot(data[i][1], to_plot[2], label=data[i][0][2]) 
#                    ax2.plot(data[i][1], to_plot[3], label=data[i][0][3])
#                    ax2.plot(data[i][1], to_plot[4], label=data[i][0][4])
#                    ax2.plot(data[i][1], to_plot[5], label=data[i][0][5])  
#                elif len(to_plot) == 7 :
#                    # ax2.plot(data[0][1], to_plot[0], data[0][1], to_plot[1], data[0][1], to_plot[2], data[0][1], to_plot[3], data[0][1], to_plot[4], data[0][1], to_plot[5], data[0][1], to_plot[6])		
#                    ax2.plot(data[i][1], to_plot[0], label=data[i][0][0])
#                    ax2.plot(data[i][1], to_plot[1], label=data[i][0][1])
#                    ax2.plot(data[i][1], to_plot[2], label=data[i][0][2]) 
#                    ax2.plot(data[i][1], to_plot[3], label=data[i][0][3])
#                    ax2.plot(data[i][1], to_plot[4], label=data[i][0][4])
#                    ax2.plot(data[i][1], to_plot[5], label=data[i][0][5]) 
#                    ax2.plot(data[i][1], to_plot[6], label=data[i][0][6])
#    	               
#                elif len(to_plot) == 8 :
#                    # ax2.plot(data[0][1], to_plot[0], data[0][1], to_plot[1], data[0][1], to_plot[2], data[0][1], to_plot[3], data[0][1], to_plot[4], data[0][1], to_plot[5], data[0][1], to_plot[6], data[0][1], to_plot[7])		
#                    ax2.plot(data[i][1], to_plot[0], label=data[i][0][0])
#                    ax2.plot(data[i][1], to_plot[1], label=data[i][0][1])
#                    ax2.plot(data[i][1], to_plot[2], label=data[i][0][2]) 
#                    ax2.plot(data[i][1], to_plot[3], label=data[i][0][3])
#                    ax2.plot(data[i][1], to_plot[4], label=data[i][0][4])
#                    ax2.plot(data[i][1], to_plot[5], label=data[i][0][5]) 
#                    ax2.plot(data[i][1], to_plot[6], label=data[i][0][6])
#                    ax2.plot(data[i][1], to_plot[7], label=data[i][0][7])
#                elif len(to_plot) == 9 :
#                    # ax2.plot(data[0][1], to_plot[0], data[0][1], to_plot[1], data[0][1], to_plot[2], data[0][1], to_plot[3], data[0][1], to_plot[4], data[0][1], to_plot[5], data[0][1], to_plot[6], data[0][1], to_plot[7], data[0][1], to_plot[8])
#                    ax2.plot(data[i][1], to_plot[0], label=data[i][0][0])
#                    ax2.plot(data[i][1], to_plot[1], label=data[i][0][1])
#                    ax2.plot(data[i][1], to_plot[2], label=data[i][0][2]) 
#                    ax2.plot(data[i][1], to_plot[3], label=data[i][0][3])
#                    ax2.plot(data[i][1], to_plot[4], label=data[i][0][4])
#                    ax2.plot(data[i][1], to_plot[5], label=data[i][0][5]) 
#                    ax2.plot(data[i][1], to_plot[6], label=data[i][0][6]) 
#                    ax2.plot(data[i][1], to_plot[7], label=data[i][0][7])
#                    ax2.plot(data[i][1], to_plot[8], label=data[i][0][8]) 
#                elif len(to_plot) == 10 :
#                    # ax2.plot(data[0][1], to_plot[0], data[0][1], to_plot[1], data[0][1], to_plot[2], data[0][1], to_plot[3], data[0][1], to_plot[4], data[0][1], to_plot[5], data[0][1], to_plot[6], data[0][1], to_plot[7], data[0][1], to_plot[8], data[0][1], to_plot[9])	
#                    ax2.plot(data[i][1], to_plot[0], label=data[i][0][0])
#                    ax2.plot(data[i][1], to_plot[1], label=data[i][0][1])
#                    ax2.plot(data[i][1], to_plot[2], label=data[i][0][2]) 
#                    ax2.plot(data[i][1], to_plot[3], label=data[i][0][3])
#                    ax2.plot(data[i][1], to_plot[4], label=data[i][0][4])
#                    ax2.plot(data[i][1], to_plot[5], label=data[i][0][5]) 
#                    ax2.plot(data[i][1], to_plot[6], label=data[i][0][6])  
#                    ax2.plot(data[i][1], to_plot[7], label=data[i][0][7])
#                    ax2.plot(data[i][1], to_plot[8], label=data[i][0][8])
#                    ax2.plot(data[i][1], to_plot[9], label=data[i][0][9])
#                elif len(to_plot) == 11 :
#                    # ax2.plot(data[0][1], to_plot[0], data[0][1], to_plot[1], data[0][1], to_plot[2], data[0][1], to_plot[3], data[0][1], to_plot[4], data[0][1], to_plot[5], data[0][1], to_plot[6], data[0][1], to_plot[7], data[0][1], to_plot[8], data[0][1], to_plot[9], data[0][1], to_plot[10])
#                    ax2.plot(data[i][1], to_plot[0], label=data[i][0][0])
#                    ax2.plot(data[i][1], to_plot[1], label=data[i][0][1])
#                    ax2.plot(data[i][1], to_plot[2], label=data[i][0][2]) 
#                    ax2.plot(data[i][1], to_plot[3], label=data[i][0][3])
#                    ax2.plot(data[i][1], to_plot[4], label=data[i][0][4])
#                    ax2.plot(data[i][1], to_plot[5], label=data[i][0][5]) 
#                    ax2.plot(data[i][1], to_plot[6], label=data[i][0][6])
#                    ax2.plot(data[i][1], to_plot[7], label=data[i][0][7])
#                    ax2.plot(data[i][1], to_plot[8], label=data[i][0][8])
#                    ax2.plot(data[i][1], to_plot[9], label=data[i][0][9])
#                    ax2.plot(data[i][1], to_plot[10], label=data[i][0][10])
#                
                ax2.tick_params(labelrotation=-90)
                ax2.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')               
                # plt.show()            
                # plt.ioff()
                
                # Define la posibilidad de imprimir en línea las gráficas
                if self.parameters["stations"]: 
                    pass
                
                # plt.close(fig) 
                # plt.savefig('figures/'+stations[i]+' '+labl+".png", bbox_inches='tight')
                plt.savefig('figures/'+stations[i]+'('+companies[i]+') '+labl+".png", bbox_inches='tight')
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
        weeksimu = (self.parameters["nsimulations"]+self.parameters["weekstraining"])*7 
        finitest = datetime(self.parameters["finitest"][0], self.parameters["finitest"][1], self.parameters["finitest"][2], 0, 0, 0)
        ffintest = datetime(self.parameters["ffintest"][0], self.parameters["ffintest"][1], self.parameters["ffintest"][2], 0, 0, 0)
#        print(finitest.strftime(self.formato)) 
#        print(ffintest.strftime(self.formato)) 
        feini = finitest - timedelta(days=(self.parameters["nsimulations"]+self.parameters["weekstraining"]-1)*7)
        fefin = ffintest - timedelta(days=(self.parameters["nsimulations"])*7)  
#        print(feini.strftime(self.formato)) 
#        print(fefin.strftime(self.formato)) 

        
        mantenimiento = ['CHEQUEO', 'In Maintenance', 'STOP'] 
        disponibilidad = ['DISPONIBLE', 'AVAILABLE', '0', 'Non-Rev. Transfer'] 
            
        db2 = DBkm100() 
        
        # ejecutamos el número de simulaciones
        for k in range(self.parameters["nsimulations"]):
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
                nam = "SELECT kmbi.flota_historica_proveedor.mva, v.id  , descripcion_estado, fecha , clase FROM kmbi.flota_historica_proveedor JOIN km100.vehiculo v on v.mva= kmbi.flota_historica_proveedor.mva JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s AND kmbi.flota_historica_proveedor.fecha BETWEEN %s AND %s"  
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
                        # t[0] mva
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
                      
                        
                nam2 = "SELECT v.mva, fh.bandera_renta, fh.nombre_estado, fh.fecha FROM km100.vehiculo v JOIN kmbi.flota_historica fh on v.id = fh.id_vehiculo JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s AND  fh.fecha BETWEEN %s AND %s"
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
            
            
            # ---------------------------------------------
            # ---------------------------------------------
            # Ejecución del algoritmo genético con los parámetros previos
            # ---------------------------------------------
            # ---------------------------------------------
            
            print('\n', '\n', 'Algoritmo genético', '\n', '\n')    
        
            sol= []
        
            var = CarRentalFleetR3() 
            var.setInstance(infoTraining)
            print(var.stations.STATIONS, var.nVar)    
            entity = Entity(var, [self.parameters["fileconfigGA"], self.parameters["evalsGA"], self.parameters["expGA"] ])  
            entity.run()  
            
            # De las soluciones propuestas por el algoritmo obtener la mejor propuesta.
            # En este caso aquella que tenga menor valor de la función objetivo
            bfit = np.Inf
            vfit = np.ones(var.stations.STATIONS)
            print(typesOfVehicles)
            
            
            for j in range(entity.stats.nSolutions()):  
                print("\nChromosome")     
                tmp = entity.stats.getSolution(j) 
                tmp.prints( )
                print("\nProposal") 
                var.evaluate(tmp, "C") 
                # print("some", bfit, vfit, sol, var.proposal)   
                
                if j == 0 : 
                    # print(sol)
                    # print(var.proposal)
                    for i in range(var.stations.STATIONS): 
                        # print(var.proposal[i])
                        sol.append(var.proposal[i])
                    bfit = tmp.fitness     
                    vfit = var.valxstation
                    # print("s ", sol, var.proposal) 
                else :             
                    if tmp.fitness < bfit : 
                        bfit = tmp.fitness   
                        vfit = var.valxstation
                        for i in range(var.stations.STATIONS): 
                            # print(var.proposal[i])
                            sol[i] = var.proposal[i]
                    elif tmp.fitness == bfit :  
                        for i in range(var.stations.STATIONS): 
                            if var.valxstation[i] < vfit[i] : 
                                sol[i] = var.proposal[i]
                                vfit[i] = var.valxstation[i]
            print("\nResult")                         
            print(vfit)         
            print(sol)   
            
            
            # ---------------------------------------------
            # ---------------------------------------------
            # Evaluar la propuesta con la información propia de 
            # la siguiente semana
            # ---------------------------------------------
            # ---------------------------------------------
            
            
            # ---------------------------------------------
            # ---------------------------------------------
            # valores previos a la semana de prueba a los que se aplicará el pronóstico
            # ---------------------------------------------
            # ---------------------------------------------
         
            
            stations = []
            infoStations = []
            print('\n\n---Lastweek---', (fpini - timedelta(days=7)).strftime(self.formato), (fpfin - timedelta(days=7)).strftime(self.formato))    
            for w in range(len(self.parameters["stations"])): 
                nam = "SELECT kmbi.flota_historica_proveedor.mva, v.id, descripcion_estado, fecha, clase FROM kmbi.flota_historica_proveedor JOIN km100.vehiculo v on v.mva= kmbi.flota_historica_proveedor.mva JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s AND kmbi.flota_historica_proveedor.fecha BETWEEN %s AND %s"  
                # print(nam, self.parameters["stations"][w], self.companies[w], (fpini - timedelta(days=7)).strftime(self.formato), (fpfin - timedelta(days=7)).strftime(self.formato))
                query = self.db.query(nam, (self.parameters["stations"][w], self.companies[w], (fpini - timedelta(days=7)).strftime(self.formato), (fpfin - timedelta(days=7)).strftime(self.formato), )) 
                
                es = Estacion(self.parameters["stations"][w]+'('+self.companies[w]+')')
            
                his = []    
                estmp = []
                
                # ---------------------------------------------
                for t in query:
                    # print(t)  
                    # print('---2---', t[0], t[1], t[4], t[3], t[2]) 
                    if es.gets(t[0]):
                        es.addD(t[0], t[3], t[2].strip(" ")) 
                    else :        
                        es.add2(t[0], t[1], t[4], t[3], t[2].strip(" ")) 
                    his.append(t)     
                    
                        
                nam2 = "SELECT  v.mva, fh.bandera_renta, fh.nombre_estado, fh.fecha FROM km100.vehiculo v JOIN kmbi.flota_historica fh on v.id = fh.id_vehiculo JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s AND  fh.fecha BETWEEN %s AND %s"
                query2 = db2.query(nam2, (self.parameters["stations"][w], self.companies[w], (fpini - timedelta(days=7)).strftime(self.formato), (fpfin - timedelta(days=7)).strftime(self.formato), )) 
                 
        
                for tv in query2: 
                    # print(tv)  
                    # print('---3---', tv[0], tv[1], tv[3], tv[2]) 
                    mkstatus = self.makedecision( " ", tv[1], tv[2]) 
                    es.compare2(tv[0], tv[3], mkstatus)   
            
                    # print("---")    
                    # print("---")    
                # es.prints()   
                estmp.append(es.indtip())   
                estmp.append(es.indtipc())   
                estmp.append(es.indtipg(mantenimiento))  
                estmp.append(es.indtipg(disponibilidad))   
                estmp.append(es.indtipg(['On Rent', 'AVAILABLE']))   
                estmp.append(es.indtipg(['On Rent', 'AVAILABLE', 'In Maintenance' ])) 
                  
                stations.append(es) 
                
                # Verificamos Qué es la estación haya tenido datos si no tiene datos 
                # se asigna un conjunto vacío, asignado al grupo de vehículo none 
#                if len(estmp[0][0]) ==0:
#                    estmp = [[['None'], [0]],  [[0], [0.0], [0.0]],  [[0], [0.0], [0.0]],  [[0], [0.0], [0.0]],  [[0], [0.0], [0.0]],  [[0], [0.0], [0.0]]]
              
                infoStations.append(estmp)
                
            infoLastweek = IndAndVar()
            infoLastweek.setInstance((fpini - timedelta(days=7)).strftime(self.formato), (fpfin - timedelta(days=7)).strftime(self.formato), stations, typesOfVehicles, infoStations)
            
            if infoLastweek.verifydata() == True:
                print() 
                print('************************************') 
                print("You do not have data in the requested time interval, i.e.,", feini.strftime(self.formato), fefin.strftime(self.formato))
                print('************************************\n')
                sys.exit()
            infoLastweek.prints( )  
         
            
            # ---------------------------------------------
            # ---------------------------------------------      
            # Datos de la semana de pronósticos
            # ---------------------------------------------
            # ---------------------------------------------
            
            stations = []
            infoStations = []            
            self.onRentData = []
            
            if forecast==True:
            
                print('\n\n---Nextweek---', fpini.strftime(self.formato), fpfin.strftime(self.formato))
                
                
                for w in range(len(self.parameters["stations"])): 
                    nam = "SELECT kmbi.flota_historica_proveedor.mva, v.id  , descripcion_estado, fecha , clase FROM kmbi.flota_historica_proveedor JOIN km100.vehiculo v on v.mva= kmbi.flota_historica_proveedor.mva JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s AND kmbi.flota_historica_proveedor.fecha BETWEEN %s AND %s"  
                    query = self.db.query(nam, (self.parameters["stations"][w], self.companies[w], fpini.strftime(self.formato), fpfin.strftime(self.formato), )) 
                   
                    es = Estacion(self.parameters["stations"][w]+'('+self.companies[w]+')')
                
                    his = []    
                    estmp = [] 
     
        
                    for t in query:
                        # print(t)  
                        # print('---2---', t[0], t[1], t[4], t[3], t[2]) 
                        if es.gets(t[0]):
                            es.addD(t[0], t[3], t[2].strip(" ")) 
                        else :        
                            es.add2(t[0], t[1], t[4], t[3], t[2].strip(" ")) 
                        his.append(t)     
                        
                            
                    nam2 = "SELECT  v.mva, fh.bandera_renta, fh.nombre_estado, fh.fecha FROM km100.vehiculo v JOIN kmbi.flota_historica fh on v.id = fh.id_vehiculo JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s AND  fh.fecha BETWEEN %s AND %s"
                    query2 = db2.query(nam2, (self.parameters["stations"][w], self.companies[w], fpini.strftime(self.formato), fpfin.strftime(self.formato), )) 
                     
            
                    for tv in query2: 
                        # print(tv)  
                        # print('---3---', tv[0], tv[1], tv[3], tv[2]) 
                        mkstatus = self.makedecision( " ", tv[1], tv[2]) 
                        es.compare2(tv[0], tv[3], mkstatus)  
              
                        # print("---")    
                        # print("---")    
                    # es.prints()  
                    estmp.append(es.indtip())   
                    estmp.append(es.indtipc())   
                    estmp.append(es.indtipg(mantenimiento))  
                    estmp.append(es.indtipg(disponibilidad))  
                    estmp.append(es.indtipg(['On Rent', 'AVAILABLE']))   
                    estmp.append(es.indtipg(['On Rent', 'AVAILABLE', 'In Maintenance' ])) 
                    
                    stations.append(es) 
                    infoStations.append(estmp)
                    self.onRentData.append(es.onRentToGraph())
                
                infoNextweek = IndAndVar()
                infoNextweek.setInstance(fpini.strftime(self.formato), fpfin.strftime(self.formato), stations, typesOfVehicles, infoStations)
                
                if infoNextweek.verifydata() == True:
                    print() 
                    print('************************************') 
                    print("You do not have data in the requested time interval, i.e.,", feini.strftime(self.formato), fefin.strftime(self.formato))
                    print('************************************\n')
                    sys.exit()
                    
                infoNextweek.prints(sol)  
                self.graphs(self.onRentData, 'T ' +fpini.strftime(self.formato)+ ' '+ fpfin.strftime(self.formato), self.parameters["stations"], self.companies)   
                
                    
                fpinix = fpini 
                fe = []
                ie = 1
                while fpinix <= fpfin :  
                    fe.append(fpinix.strftime(self.formato))
                    fpinix = fpini + timedelta(days=ie) 
                    ie = ie + 1
                    
                if len(sol[0]) != len(infoLastweek.TYPES[0]):
                    valorf = self.vadapt(sol, infoLastweek, infoTraining)  
                else :
                    valorf = np.array(infoLastweek.TYPES) + np.array(sol)            
                print('********* :', sol,  infoLastweek.TYPES, infoNextweek.typesOfVehicles, valorf, fe )    
                print('********* :', es.ver(infoNextweek.typesOfVehicles, valorf, fe ) )
              
                self.analysis(forecast, feini, fefin, fpini, fpfin, sol, infoLastweek.typesOfVehicles,  infoLastweek.OPFLMAXIMA, infoTraining,  infoNextweek.OPFLMAXIMA,  infoNextweek.MAXIMA,  infoNextweek.MANMAXIMA,  infoNextweek.MANMEDIA, infoStations) 

            else :
				
                self.analysis(forecast, feini, fefin, fpini, fpfin, sol, infoLastweek.typesOfVehicles,  infoLastweek.OPFLMAXIMA, infoTraining) 

            # ------------
            # actualizar fechas
            # ------------     
            feini = feini + timedelta(days=7)
            fefin = fefin + timedelta(days=7)

        
      
    def vadapt (self, sol, infoLastweek, infoTraining):
        valorf = np.array(infoLastweek.TYPES)
        valors = np.array(sol)  
        # print('+2++', valorf) 
        # print('+2++', valors) 
        
        
        # print('+3++', infoLastweek.TYPES,  infoLastweek.typesOfVehicles)  
        # print('+3++', sol, infoTraining.TYPES,  infoTraining.typesOfVehicles)  
        
        for t in range(len(valors[0])):
            for j in range(len(valorf[0])):
                if infoLastweek.typesOfVehicles[j] == infoTraining.typesOfVehicles[t]:
                    valors[0][t] = valors[0][t] +valorf[0][j]
                    break
                
        # print('+4++', valors)          
        
        return valorf
    
    
        
       
    def analysis (self, flagfor, feini, fefin, fpini, fpfin, sol, typesvh, lastw, infoTraining, forew=None, MAXIMA=None, MANMAX=None, MANMEDIA=None, infoStations=None):   
        print('\n\n')
        
        print('****** analysis period ****** :', feini.strftime(self.formato), fefin.strftime(self.formato))    
        print('')
        forecast = [] 
        
        
        # print('----', sol)
        # print('----', typesvh)    
        # print('----', lastw)  
        # print('----', infoTraining.typesOfVehicles) 
        
        
        if len(sol[0]) != len(typesvh):
            for f in range(len(sol)):  
                cforecast = [] 
                for v in range(len(sol[f])):  
                    for d in range(len(typesvh)): 
                        if typesvh[d] == infoTraining.typesOfVehicles[v]:
                            cforecast.append(int(lastw[f][d]) + int(sol[f][v]))
                forecast.append(cforecast)    
        else :   
            # print('-e--', sol)
            for f in range(len(sol)):  
                cforecast = [] 
                for v in range(len(sol[f])):  
                    cforecast.append(int(lastw[f][v]) + int(sol[f][v]))
                forecast.append(cforecast) 
#            pass
#        for f in range(len(sol)):  
#                cforecast = [] 
#                for v in range(len(sol[f])):  
#                    cforecast.append(int(lastw[f][v]) + int(sol[f][v]))
#                forecast.append(cforecast)     
        # self.graphs(self.onRentData) 
        # print('----', forecast)
        
            
        print('******    proposal     ****** :', '\n', typesvh, '\n')
        print('')
        for f in range(len(sol)): 
            print(self.parameters["stations"][f],  sol[f])
        
        print('')    
        self.compareStations(sol, typesvh)   
        print('')    
        
        
        print('******    forecast     ****** :')     
        print('')
        for f in range(len(sol)): 
            print(self.parameters["stations"][f], forecast[f])
        print('')
        
        
        if flagfor==True:
            print('****** forecast period ****** :', fpini.strftime(self.formato), fpfin.strftime(self.formato))          
            print(' vehicles used in this period :', '\n', typesvh, '\n')
            for f in range(len(sol)): 
                print(self.parameters["stations"][f], forew[f])
            print('\n\n')
     
        
            print('* comparison of the proposal* :') 
            for f in range(len(sol)): 
                print('\n******    stations     ****** :', self.parameters["stations"][f])
     
                for v in range(len(sol[f])): 
                    
                    if self.nogroupin(f, v, typesvh, infoStations ):
                        continue
                    
                    print(typesvh[v])
                    print(forecast[f][v], 'covers peak demand', int(MAXIMA[f][v]), ' : ', end ='')
                    if forecast[f][v] >= int(MAXIMA[f][v]):
                        print('yes')
                    else :   
                        print('no')
                    
                    
                    print(forecast[f][v], 'covers peak demand and average maintenance', (int(MAXIMA[f][v])+int(MANMEDIA[f][v])), ' : ', end ='')
                    if forecast[f][v] >= (int(MAXIMA[f][v])+int(MANMEDIA[f][v])):
                        print('yes')
                    else :   
                        print('no')   
                    
                    
                    print(forecast[f][v], 'covers peak demand and maintenance peak', (int(MAXIMA[f][v])+int(MANMAX[f][v])), ' : ', end ='')
                    if forecast[f][v] >= (int(MAXIMA[f][v])+int(MANMAX[f][v])):
                        print('yes')
                    else :   
                        print('no')    
                    print() 
                    # forecast.append(int(lastw[f][v]) + int(sol[f][v]))
            pass
        
    
  
    def nogroupin(self, w, i, typesvh, infoStations):
        value = True
        try:
            ind = infoStations[w][0][0].index(typesvh[i]) 
            if ind != -1:
                value = False
            else :    
                pass
        except:  
            pass 
        
        
        return value 
     
        
        
    def compareStations(self, sol, typesvh): 
        
        for i in range(len(sol[0])):
            posc=[]
            negc=[]	
            spos=0
            sneg=0
            # print(i)
            for f in range(len(sol)): 
                # print(self.parameters["stations"][f],  sol[f])  
                if sol[f][i] > 0:  
                    posc.append( [self.parameters["stations"][f], sol[f][i]]) 
                    spos=spos+sol[f][i]
                    # print(self.parameters["stations"][f], sol[f][i], spos)
                elif sol[f][i] < 0: 
                    negc.append( [self.parameters["stations"][f], -1*sol[f][i]]) 
                    sneg=sneg-sol[f][i]
                    # print(self.parameters["stations"][f], sol[f][i], sneg)
      
            # print(posc)         
            # print(negc)    
            
            while True:
                if spos > 0 and sneg > 0:	
                    tmp=0
                    tm2=0
                    ind=0
                    in2=0
                    
                    for f in range(len(posc)):
                        if posc[f][1] > 0:
                            tmp = posc[f][1]
                            ind = f
                            break
                            
                    for f in range(len(negc)):
                        if negc[f][1] > 0:
                            tm2 = negc[f][1]
                            in2 = f    
                            break                   
                    
                    if tmp < tm2 :
                    	tm2 = tmp   
                    
                    posc[ind][1] = posc[ind][1] - tm2
                    negc[in2][1] = negc[in2][1] - tm2
                    spos = spos - tm2
                    sneg = sneg - tm2
                    print('move ', tm2, typesvh[i], 'from', negc[in2][0], 'to ', posc[ind][0])
                    
                else:
                    break		
        
        
        
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

 
