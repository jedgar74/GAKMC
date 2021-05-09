#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 16:08:15 2021

@author: tauger
""" 


class Cliente(object):
    
    def __init__(self, name): 
        self.name = name 
        self.empresas = []
        
        
    def addEmpresa(self, empresa):   
        
        if len(self.empresas) == 0: 
            self.empresas.append(empresa)
        else :
            addemp = True
            for t in range(len(self.empresas)):
                if self.empresas[t].name == empresa.name: 
                    self.empresas[t].addEstacion(empresa.estaciones[0], empresa.idestaciones[0], empresa.gpsestaciones[0])
                    addemp = False
                    break 
            if addemp:
                self.empresas.append(empresa)     
                
                
                
    def getEmpresas(self):     
        return self.empresas
    
                 
                
    def nEmpresas(self):     
        return len(self.empresas)
    
    
    
    def getEmpresa(self, i):     
        return self.empresas[i]
       
            
 