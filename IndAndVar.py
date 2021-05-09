#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:37:38 2021

@author: tauger
"""

import numpy as np

class IndAndVar(object):   
    
    def __init__(self):
        pass
    
    
    def setInstance(self, finit, ffins, stations, typesOfVehicles, infoStations): 
        self.finit = finit
        self.ffins = ffins
        self.STATIONS = len(stations)    
        self.TOTALV = 0 
        self.typesOfVehicles   = [ ] 
        
        for w in range(len(stations)):   
            self.TOTALV = self.TOTALV + len(stations[w].mvaveh)  
            for c in range(len(infoStations[w][0][0])):  
                try:
                    ind = self.typesOfVehicles.index(infoStations[w][0][0][c]) 
                    if ind != -1:
                        pass
                    else :    
                        self.typesOfVehicles.append(infoStations[w][0][0][c])  
                except:  
                        self.typesOfVehicles.append(infoStations[w][0][0][c])     
        
        
        self.typesOfVehicles.sort()
        # print(typesOfVehicles)    
        self.SETV = len(self.typesOfVehicles)   
        self.TYPES = [ ]   
        self.MAXIMA = [ ]  
        self.MEDIA = [ ]  
        self.MANMAXIMA = [ ]
        self.MANMEDIA = [ ]
        self.DISPMAXIMA = [ ]
        self.DISPMEDIA = [ ]
        self.VFEC = [ ] 
        self.OPERMAXIMA = [ ]
        self.OPERMEDIA = [ ]
        self.OPFLMAXIMA = [ ]
        self.OPFLMEDIA = [ ]
        
        for w in range(len(stations)):  
            tTYPES = np.zeros(len(self.typesOfVehicles))
            tMAXIMA= np.zeros(len(self.typesOfVehicles))
            tMEDIA = np.zeros(len(self.typesOfVehicles))
            tMANMAXIMA= np.zeros(len(self.typesOfVehicles))
            tMANMEDIA = np.zeros(len(self.typesOfVehicles)) 
            tDISPMAXIMA= np.zeros(len(self.typesOfVehicles))
            tDISPMEDIA = np.zeros(len(self.typesOfVehicles)) 
            
            tOPERMAXIMA= np.zeros(len(self.typesOfVehicles))
            tOPERMEDIA = np.zeros(len(self.typesOfVehicles)) 
            tOPFLMAXIMA= np.zeros(len(self.typesOfVehicles))
            tOPFLMEDIA = np.zeros(len(self.typesOfVehicles)) 
            
            tVFEC = [ ]  
            for j in range(len(self.typesOfVehicles)): 
                tVFEC.append([0])
    #        print("--d-",len(infoStations[w][0][0]))   
    #        print("--d-",tVFEC)             
            for j in range(len(infoStations[w][0][0])):        
                ind = self.typesOfVehicles.index(infoStations[w][0][0][j])
                tTYPES[ind] = int(infoStations[w][0][1][j])
                tMAXIMA[ind] = int(infoStations[w][1][0][j])
                tMEDIA[ind] = float(infoStations[w][1][1][j])
                tMANMAXIMA[ind] = int(infoStations[w][2][0][j])
                tMANMEDIA[ind] = float(infoStations[w][2][1][j])   
                tDISPMAXIMA[ind] = int(infoStations[w][3][0][j])    
                tDISPMEDIA[ind] = float(infoStations[w][3][1][j])  
                #print("--d-",ind, len(self.typesOfVehicles),j,len(infoStations[w][0][0]),infoStations[w][4])
                tOPERMAXIMA[ind] = int(infoStations[w][4][0][j])    
                tOPERMEDIA[ind] = float(infoStations[w][4][1][j])  
                tOPFLMAXIMA[ind] = int(infoStations[w][5][0][j])    
                tOPFLMEDIA[ind] = float(infoStations[w][5][1][j])                 
                
                if len(infoStations[w]) > 6:      
#            print("--e-", infoStations[w][6][1]) 
                    if j < len(infoStations[w][6][1]):
                        tVFEC[ind] = infoStations[w][6][1][j]
                    
            self.TYPES.append(tTYPES.tolist())    
            self.MAXIMA.append(tMAXIMA.tolist())  
            self.MEDIA.append(tMEDIA.tolist())           
            self.MANMAXIMA.append(tMANMAXIMA.tolist())  
            self.MANMEDIA.append(tMANMEDIA.tolist())           
            self.DISPMAXIMA.append(tDISPMAXIMA.tolist())  
            self.DISPMEDIA.append(tDISPMEDIA.tolist())     
            self.VFEC.append(tVFEC)    
            
            self.OPERMAXIMA.append(tOPERMAXIMA.tolist())  
            self.OPERMEDIA.append(tOPERMEDIA.tolist())             
            self.OPFLMAXIMA.append(tOPFLMAXIMA.tolist())  
            self.OPFLMEDIA.append(tOPFLMEDIA.tolist())     
        
        
        # print("\n--e-", infoStations[0])  
        # print("\n--e-", infoStations[0][4]) 
        # self.NumeroDias = 1e10
        if len(infoStations[w]) > 6:      
            self.NumeroDias = infoStations[0][6][0]
        
        
        
    def prints(self, sol=None):   
        print("---")   
        print('DATES     :', self.finit, self.ffins)
        print('TYPESOFVEHICLES:',  self.typesOfVehicles) 
        print('STATIONS  :', self.STATIONS)   
        print('SETV      :', self.SETV)  
        print('TOTALV    :', self.TOTALV)    
        print('TYPES     :', self.TYPES )  
        print('MAXIMA    :', self.MAXIMA)     
        print('MEDIA     :', self.MEDIA)      
        print('MANMAXIMA :', self.MANMAXIMA)  
        print('MANMEDIA  :', self.MANMEDIA)  
        print('DISPMAXIMA:', self.DISPMAXIMA)     
        print('DISPMEDIA :', self.DISPMEDIA)      
        
        print('OPERMEDIA :', self.OPERMEDIA)    
        print('OPERMAXIMA:', self.OPERMAXIMA)        
        print('OPFLMEDIA :', self.OPFLMEDIA)    
        print('OPFLMAXIMA:', self.OPFLMAXIMA)        
        
        if sol != None : 
#            valor1 = np.array(MEDIAb) + np.array(MANMEDIAb) + np.array(DISPMEDIAb)  
#            valor2 = np.array(MAXIMAb) + np.array(DISPMAXIMAb)
#            valorf = np.array(TYPESb) + np.array(sol)
#            print('valor EE ME DE :', '\n', valor1)   
#            print('valor MM DM    :', '\n', valor2) 
            print('valor PROPOSAL :', sol)
#            print('valor T PROPOS :', '\n', valorf)
                
            valor3 = np.array(self.MEDIA) + np.array(self.MANMEDIA) + np.array(self.DISPMEDIA) 
            valor4 = np.array(self.MAXIMA) + np.array(self.DISPMAXIMA)
            print('valor MAXIMA   :', self.MAXIMA)   
            print('valor MM DM    :', valor4) 
     

    def verifydata(self):
        ou = False
        if self.SETV==0 and len(self.typesOfVehicles)==0 :
            ou = True
            # sys.exit()
            # sys.exit("You do not have data in the requested time interval, i.e.,", ran1, ran2)
     
        return ou


