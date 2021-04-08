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
            self.parameters = {"stations": stations,  "company": company, "nsimulations": nsimulations, "weekstraining": weekstraining,   "finitest": finitest, "ffintest": ffintest,  "fileconfigGA": fileconfigGA,  "evalsGA": evalsGA,  "expGA": expGA,  "printFile": False }
  
    
    
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
        # print("***********")         
        # print(len(self.cat)) 
        # print(self.cat) 
        
        
        
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
        
        if flagOnRent == 1 : 
            if kmCFleet == 'Taller' or kmCFleet == 'Operativo' :
                status = 'On Rent'
            else : 
                status = 'On Rent'   
        else :  
            if kmCFleet == 'Operativo' :
                status = 'AVAILABLE'
            elif kmCFleet == 'Taller' :
                status = 'In Maintenance'               
            else : 
                status = 'UNAVAILABLE'  
        # print('---4---', prov, ';', flag, ';', statusX, ';', status)        
                     
        return status 

     
        
    def sim(self): 
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
            
            print('\n\n---Training---', feini.strftime(self.formato), fefin.strftime(self.formato))   
            for w in range(len(self.parameters["stations"])): 
                
                # obtenemos Los indicadores de cada estación por grupo a partir de la
                # Data histórica
                nam = "SELECT kmbi.flota_historica_proveedor.mva, v.id  , descripcion_estado, fecha , clase FROM kmbi.flota_historica_proveedor JOIN km100.vehiculo v on v.mva= kmbi.flota_historica_proveedor.mva JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s AND kmbi.flota_historica_proveedor.fecha BETWEEN %s AND %s"  
                query = self.db.query(nam, (self.parameters["stations"][w], self.companies[w], feini.strftime(self.formato), fefin.strftime(self.formato), )) 
                print('---1---', feini.strftime(self.formato)) 
                
                # vehvma = []
                # veh_id = []
                his = []    
                estmp = []        
                es = Estacion(self.parameters["stations"][w])
                
                for t in query:
                    #  print(t)  
                    #  print('---2---', t[0], t[1], t[4], t[3], t[2]) 
                    if es.gets(t[0]):
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
                    es.compare(tv[0], tv[3], mkstatus) 
                         
                        
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
                infoStations.append(estmp)  
            
            
            typesOfVehicles   = [ ]
            infoTraining = IndAndVar()
            infoTraining.setInstance(feini.strftime(self.formato), fefin.strftime(self.formato), stations, typesOfVehicles, infoStations)
            infoTraining.prints( ) 
    
                
            # ------------
            # Ejecución del algoritmo genético con los parámetros previos
            # ------------  
            print('\n', '\n', 'algoritmo genético', '\n', '\n')    
        
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
            
            
            # ------------
            # Evaluar la propuesta con la información propia de 
            # la siguiente semana
            # ------------       
            
            # ------------      
            # valores previos a la semana de prueba a los que se aplicará el pronóstico
            # ------------   
         
            stations = []
            infoStations = []
            print('\n\n---Lastweek---', (fpini - timedelta(days=7)).strftime(self.formato), (fpfin - timedelta(days=7)).strftime(self.formato))    
            for w in range(len(self.parameters["stations"])): 
                nam = "SELECT kmbi.flota_historica_proveedor.mva, v.id, descripcion_estado, fecha, clase FROM kmbi.flota_historica_proveedor JOIN km100.vehiculo v on v.mva= kmbi.flota_historica_proveedor.mva JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s AND kmbi.flota_historica_proveedor.fecha BETWEEN %s AND %s"  
                # print(nam, self.parameters["stations"][w], self.companies[w], (fpini - timedelta(days=7)).strftime(self.formato), (fpfin - timedelta(days=7)).strftime(self.formato))
                query = self.db.query(nam, (self.parameters["stations"][w], self.companies[w], (fpini - timedelta(days=7)).strftime(self.formato), (fpfin - timedelta(days=7)).strftime(self.formato), )) 
                
                es = Estacion(self.parameters["stations"][w])
            
                his = []    
                estmp = []
                
                # ------------
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
                    es.compare(tv[0], tv[3], mkstatus)   
            
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
                
            infoLastweek = IndAndVar()
            infoLastweek.setInstance((fpini - timedelta(days=7)).strftime(self.formato), (fpfin - timedelta(days=7)).strftime(self.formato), stations, typesOfVehicles, infoStations)
            infoLastweek.prints( )  
         
            
            # ------------      
            # Datos de la semana de pronósticos
            # ------------       
            stations = []
            infoStations = []
            print('\n\n---Nextweek---', fpini.strftime(self.formato), fpfin.strftime(self.formato))
            for w in range(len(self.parameters["stations"])): 
                nam = "SELECT kmbi.flota_historica_proveedor.mva, v.id  , descripcion_estado, fecha , clase FROM kmbi.flota_historica_proveedor JOIN km100.vehiculo v on v.mva= kmbi.flota_historica_proveedor.mva JOIN km100.estacion e on e.id_estacion = v.asignacion_estacion JOIN km100.empresa em on em.id_empresa = e.id_empresa WHERE e.nombre = %s AND em.nombre = %s AND kmbi.flota_historica_proveedor.fecha BETWEEN %s AND %s"  
                query = self.db.query(nam, (self.parameters["stations"][w], self.companies[w], fpini.strftime(self.formato), fpfin.strftime(self.formato), )) 
               
                es = Estacion(self.parameters["stations"][w])
            
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
                    es.compare(tv[0], tv[3], mkstatus)  
          
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
            
            infoNextweek = IndAndVar()
            infoNextweek.setInstance(fpini.strftime(self.formato), fpfin.strftime(self.formato), stations, typesOfVehicles, infoStations)
            infoNextweek.prints(sol)  
            
                
            fpinix = fpini 
            fe = []
            ie = 1
            while fpinix <= fpfin :  
                fe.append(fpinix.strftime(self.formato))
                fpinix = fpini + timedelta(days=ie) 
                ie = ie + 1
                
                
            valorf = np.array(infoLastweek.TYPES) + np.array(sol)            
            print('********* :', sol,  infoLastweek.TYPES, infoNextweek.typesOfVehicles, valorf, fe )    
            print('********* :', es.ver(infoNextweek.typesOfVehicles, valorf, fe ) )
          
            
            self.analysis(feini, fefin, fpini, fpfin, sol, infoLastweek.typesOfVehicles,  infoLastweek.OPFLMAXIMA,  infoNextweek.OPFLMAXIMA,  infoNextweek.MAXIMA,  infoNextweek.MANMAXIMA,  infoNextweek.MANMEDIA) 



            # ------------
            # actualizar fechas
            # ------------     
            feini = feini + timedelta(days=7)
            fefin = fefin + timedelta(days=7)

        
       
       
    def analysis (self, feini, fefin, fpini, fpfin, sol, typesvh, lastw, forew, MAXIMA, MANMAX, MANMEDIA ):   
        print('\n\n')
        
        print('****** analysis period ****** :', feini.strftime(self.formato), fefin.strftime(self.formato))    
  
        forecast = [] 
        
        for f in range(len(sol)):  
            cforecast = [] 
            for v in range(len(sol[f])):  
                cforecast.append(int(lastw[f][v]) + int(sol[f][v]))
            forecast.append(cforecast)    
            
        print('******    proposal     ****** :', '\n', typesvh, '\n')
        for f in range(len(sol)): 
            print(self.parameters["stations"][f],  sol[f])
            
        self.compareStations(sol, typesvh)    
            
        print('')    
        print('******    forecast     ****** :', '\n', forecast)     
        print('')
        print('****** forecast period ****** :', fpini.strftime(self.formato), fpfin.strftime(self.formato))          
        print(' vehicles used in this period :', '\n', typesvh, '\n')
        for f in range(len(sol)): 
            print(self.parameters["stations"][f], forew[f])
        print('\n\n')
 
    
        print('* comparison of the proposal* :') 
        for f in range(len(sol)): 
            print('\n******    stations     ****** :', self.parameters["stations"][f])
 
            for v in range(len(sol[f])): 
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
        
    def run(self):   
        # ...............................
        # Paso 1. leer Data 
        # definimos la clase para conectarnos a la base de datos
        # ...............................
        
        self.readStation()
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
            
        self.sim()        

 
