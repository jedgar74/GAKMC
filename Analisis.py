#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 08:08:12 2021

@author: tauger
"""
from datetime import datetime, timedelta
from db.DBkm100 import *
from Empresa import *


class Analisis ( ): 
    
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
            stations = ["Aila"]
            company = ["Nelly"]
            nweeks = 5    
            self.parameters = {"stations": stations, "company": company, "nweeks": nweeks,  "finitest": finitest, "ffintest": ffintest, "prints": False }
   
    
    def setnweeks(self, nweeks):   
        self.parameters["nweeks" ] = nweeks
       
       
               
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
    
    def readStation2(self):   
        query = self.db.query("SELECT e.nombre, em.nombre, c.nombre_comercial, e.id_estacion, e.coord_google_maps FROM km100.estacion e JOIN km100.empresa em on em.id_empresa = e.id_empresa JOIN km100.cliente c on c.id = em.cliente_id") 
        
        self.labelestacion = []
        self.idestacion = []
        self.gpsestacion = []
        self.estacion = []
        self.empresa = []
        cliente = []
        
        self.clientes=[] 
        
        for t in query:
#            print(t)  
#            try:
            if len(self.clientes) == 0 :  
                emp = Empresa(t[1])
                emp.addEstacion(t[0], t[3], t[4]) 
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
                        emp.addEstacion(t[0], t[3], t[4]) 
                        self.clientes[j].addEmpresa(emp)
                        addcli = False
                        break 
                if addcli:
                    emp = Empresa(t[1])
                    emp.addEstacion(t[0], t[3], t[4]) 
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
                    self.idestacion.append(emp.getIDEstacion(k))
                    self.gpsestacion.append(emp.getGPSEstacion(k))
                    self.labelestacion.append(emp.getEstacion(k)+'('+emp.name+')')
                    # print(emp.getEstacion(k), '-',  emp.name, '-', self.clientes[t].name)
        # print("***********")             
        # print(len(self.estacion), len(self.empresa), len(cliente))   
        # print("-----------")  
        # print(self.estacion, self.empresa, cliente)
        # print("-----------")   
        
        
        
    def getidest(self, est, emp): 
        
        idest = ''
        
        # print("----12d----", emp)
        # print("----12f----", est)
        
        for j in range(len(self.empresa)):
            if self.empresa[j] == emp and self.estacion[j] == est: 
                idest = self.idestacion[j]
                # print("----123----", self.gpsestacion[j])
                
        return idest
    
    
   
    def getForecastdb(self, fini, ffin, stations, companies):
        # print("\n-------getForecastdb--------- ",  self.getidest( stations , companies ))
        print("\n------ Forecast ----- ")
        idp = [ ]
        nam = "SELECT i.clase, i.nveh FROM onefleet.forecast i WHERE i.id_estacion = %s AND i.fecha_inicio =%s AND i.fecha_final =%s"
        query = self.db.query(nam, (self.getidest( stations , companies ), fini.strftime(self.formato), ffin.strftime(self.formato), )) 
        
        for t in query: 
            print("------ Forecast ------ ", t )
            idp.append([ t[0], t[1], None])
            
        return idp 
    
    
    
    def getDatadb(self, fini, ffin, stations, companies):
        # print("-------getDatadb--------- ",  self.getidest( stations , companies ))
        print("\n-------- Data ------- ")
        idp = [ ]
        nam = "SELECT i.clase, i.maxrent, i.maxmant, i.mediamant FROM onefleet.inputdata i WHERE i.id_estacion = %s AND i.fecha_inicio =%s AND i.fecha_final =%s"
        query = self.db.query(nam, (self.getidest( stations , companies ), fini.strftime(self.formato), ffin.strftime(self.formato), )) 
        
        for t in query: 
            print("-------- Data ------- ", t )
            idp.append([ t[0], t[1], t[2] , t[3] ] )
            
        return idp 

        

    def analisis(self, forecast=True): 
        
        print("-------analisis--------- ") 
        finitest = datetime(self.parameters["finitest"][0], self.parameters["finitest"][1], self.parameters["finitest"][2], 0, 0, 0)
        ffintest = datetime(self.parameters["ffintest"][0], self.parameters["ffintest"][1], self.parameters["ffintest"][2], 0, 0, 0)
        feini = finitest - timedelta(days=(self.parameters["nweeks"])*7)
        fefin = ffintest - timedelta(days=(self.parameters["nweeks"])*7)  
       
        for d in range(self.parameters["nweeks"]):
            
            # Obtener información del pronóstico
            print("---------------- ", feini.strftime(self.formato), fefin.strftime(self.formato))     
            dta = [ ]
            for j in range(len(self.parameters["stations"])):
                # print("---------------- ", self.parameters["stations"][j], self.companies[j])  
                print("\n---------------- ", self.parameters["stations"][j], self.companies[j])     
        
                delta = self.getForecastdb(feini, fefin, self.parameters["stations"][j], self.companies[j])
                dta.append(delta)
                
                
            # Obtener información datos reales
             
            for k in range(len(self.parameters["stations"])):
                
                print("\n---------------- ", self.parameters["stations"][k], self.companies[k])    
                dts = self.getDatadb(feini, fefin, self.parameters["stations"][k], self.companies[k])
                delta = True
                
                for i in range(len(dts)): 
                    for j in range(len(dta[k])):
                        # print("--------3------- ", dta[k][j][0], dts[i][0])  
                        if dta[k][j][0] ==  dts[i][0] : 
                            dta[k][j][2]  = [dts[i][1], dts[i][2], dts[i][3]]
                            # print("--------4------- ", dta[k][j], dts[i])  
                            delta = False 
                        
                    if delta :        
                         dta[k].append([ dts[0], -1, [dts[1], dts[2], dts[3]] ])   
                   
            # realizar la comparativa 
            porc = 0 
            impr = 0
            sums = 0  
            sues = 0
            
            for k in range(len(dta)):
                print("\n---------------- ", self.parameters["stations"][k], self.companies[k])     
                # print("---------6------- ", dta[k]) 
                sues = sues + len(dta[k])
                for j in range(len(dta[k])):
                    # print("---------7------- ", dta[k][j][1]) 
                    if dta[k][j][1] != -1 :  
                        sums = sums  + dta[k][j][1]
                        dif = 1000000
                        # print("---------6------- ", dta[k][j][1]) 
                        # print("---------6------- ", dta[k][j][2] ) 
                        if dta[k][j][2] != None:
                            # covers peak demand
                            tmp = dta[k][j][1] - dta[k][j][2][0] 
                            if tmp > -1 : 
                                porc = porc + 0
                                if tmp < dif :
                                    dif = tmp
                            else :
                                dif = -1
                                porc = porc + 1
                            
                            # covers peak demand and average maintenance
                            tmp = dta[k][j][1] - (dta[k][j][2][0] + dta[k][j][2][2])
                            if tmp > -1 : 
                                porc = porc + 0
                                if tmp < dif :
                                    dif = tmp
                            else :
                                dif = -1
                                porc = porc + 1
                            
                            # covers peak demand and maintenance peak
                            tmp = dta[k][j][1] - (dta[k][j][2][0] + dta[k][j][2][1])
                            if tmp > -1 : 
                                porc = porc + 0
                                if tmp < dif :
                                    dif = tmp
                            else :
                                dif = -1
                                porc = porc + 1
                                
                                
                            if dif > -1 :     
                                impr = impr + dif
                print( )            
                print("---- Errores  / Mejora ---- ", porc, " / ",impr)        
             
            print( )   
            try:
                pporc=100*porc/(3*sues)   
            except:   
                pporc= 0
            print("-----% Error ------- ", pporc) 
            
            try:
                pimpr=100*impr/(sums)    
            except:    
                pimpr=0 
            print("-----% Mejora ------ ", pimpr )    
            print( )   
            print( )   
            
            feini = feini + timedelta(days=7)
            fefin = fefin + timedelta(days=7)
            pass        
    
    
        
    def run(self, forecast=True):  
        # print("-------run--------- ", self.parameters["stations"], self.parameters["company"]) 
        self.readStation2()
        
        if  len(self.parameters["stations"]) > -1: 
            self.companies = self.parameters["company"]*len(self.parameters["stations"])
            # print(self.companies) 
        else:
            self.companies = self.parameters["company"]
            
        # print("---------------- ", self.parameters["stations"], self.companies)     
            
        self.analisis() 
        
        pass
        
