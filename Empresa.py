#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 16:11:18 2021

@author: tauger
"""

from Cliente import * 


class Empresa(object):
    
    def __init__(self, name): 
        self.name = name  
        self.estaciones = []
        
        
        
    def addEstacion(self, estacion):    
        if len(self.estaciones) == 0: 
            self.estaciones.append(estacion)
        else :
            try:
                if  self.estaciones.index(estacion) == -1: 
                    self.estaciones.append(estacion)
            except:    
                self.estaciones.append(estacion)
                
                
    def getEstaciones(self):     
        return self.estaciones
    
                 
                
    def nEstaciones(self):     
        return len(self.estaciones)
    
    
    
    def getEstacion(self, i):     
        return self.estaciones[i]
       
    