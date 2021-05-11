#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:14:48 2021

@author: tauger
"""

import json 
from Simulation import *


def readParameters( nameFile ): 
    """  Read the algorithm parameters  
    """
    with open('./files/scenario/'+nameFile+'.json') as file: 
        data = json.load(file)
		 
    return  data 


# ...............................
# leer el archivo de configuración de la simulación  
# ...............................
namefile = 'scenario'

parameters = readParameters(namefile)
# print(parameters['stations']) 
 

# ...............................
# ejecutar la simulación
# ...............................

# simulation = Simulation()
simulation = Simulation(parameters)
# simulation.setcompany(["Budget"])
# simulation.setstations(["Santo Domingo","Santiago"])
simulation.setexpGA(1)    
simulation.setnsimulations(1)  
simulation.setfinitest([2020, 11, 24])
simulation.setffintest([2020, 11, 30])

# simulation.setCompCase(["AVIS"])
#simulation.setCompCase(["Alimentos y Entregas"])
#simulation.setCompCase(["Dollar"])
#simulation.setCompCase(["Budget"])
#simulation.setCompCase(["Europcar"])
#simulation.setCompCase(["Firefly"])
#simulation.setCompCase(["Hertz"])
#simulation.setCompCase(["InterRent"])
simulation.setCompCase(["Nelly"])
#simulation.setCompCase(["Inversiones Forteza"])
#simulation.setCompCase(["KM100 Fleet"])
#simulation.setCompCase(["LAC"])
#simulation.setCompCase(["Leasing Corporativo Europcar"])
#simulation.setCompCase(["Nelly"])
#simulation.setCompCase(["Payless"])
#simulation.setCompCase(["Thrifty"]) 
#simulation.setCompStatCase(["Thrifty"], ["Santiago" ])
#simulation.setCompStatCase(["Alimentos y Entregas"], ["Alimentos y Entregas" , "Alimentos y Entrega santo domingo" , "Remarketing"])
# print(simulation.parameters) 
#simulation.setCompStatCase(["Nelly"], ["Independencia" ])
#simulation.setstations(["Remarketing"])
#simulation.setstations(["Aila"])
#simulation.setcompany(["Nelly"])

simulation.run()
