#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 13:57:05 2021

@author: tauger
"""

class Vehiculo(object):  
    def __init__(self, mva, tipo):
        self.tipo = tipo
        self.mva = mva  
        self.fecha = []
        self.status = []
        self.active = True
        
    def add(self, fecha, status):
         self.fecha.append(fecha)
         self.status.append(status)
         
         
    def prints(self):
        print(self.mva, ' ', self.tipo)    
        for j in range(len(self.fecha)):  
            print(self.fecha[j], self.status[j])  
            
            
    def prints2(self):
        print(self.mva, ' ', self.tipo)    
        for j in range(len(self.fecha)):  
            print(self.fecha[j], self.status[j], end=' ')    
        print()    
            
    def setstatus(self, fecv, status): 
        iff = self.fecha.index(fecv) 
        if iff != -1: 
            self.status[iff] = status 
            
     
    def genmva(self):
        return self.mva       
     
        
    def contipos(self, tipos):
        cont = 0  
        cons = 0
        control = False
        cc = []
        info = []
        for j in range(len(self.fecha)): 
           for i in range(len(tipos)): 
               if self.status[j] == tipos[i]:
                   cont = cont + 1  
                   if control:
                       cons = cons + 1  
                   else :
                       control = True
                       cons = 1
               else :  
                   control = False
                   if len(cc)==0:
                       cc.append(cons) 
                   elif cons == 0 and cc.count(0) > 0:
                       pass
                   else :
                       cc.append(cons)                       
                   cons = 0
                   
        if cons == 0 and cc.count(0) > 0:
            pass
        else :
            cc.append(cons)   
            
#        print(self.mva, ' ', cont, ' ', cc)     
        
        info.append(cont)          
        info.append(max(cc))  
        info.append(round(sum(cc)/(len(self.fecha)),3) )
        info.append(cc)
                   
        return info           
        
        