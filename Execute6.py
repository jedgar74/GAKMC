#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 10:18:47 2021

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

simulation = Simulation()
#simulation = Simulation(parameters)

simulation.setfinitest([2020, 1, 1])
simulation.setffintest([2020, 1, 7])
simulation.setnsimulations(1)
simulation.setweekstraining(52)
#simulation.setCompCase(["Nelly"])
simulation.setCompStatCase(["Nelly"], ["Independencia" ])
simulation.setexpGA(1)
simulation.run()
    