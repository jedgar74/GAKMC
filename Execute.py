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
# simulation.setstations(["Aila", "Bavaro", "Puerto Plata"])
    
simulation.setfinitest([2021, 2, 22])
simulation.setffintest([2021, 2, 28])
print(simulation.parameters) 
simulation.run()
