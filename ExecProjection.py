#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 10:16:51 2021

@author: tauger
"""


from Projection import *

# ...............................
# ejecutar la simulación
# ...............................

simulation = Projection()
#simulation = Simulation(parameters)

simulation.setfinitest([2020, 1, 1])
simulation.setffintest([2020, 1, 7]) 
simulation.setweekstraining(52)
simulation.setprints(True)
#simulation.setCompCase(["Nelly"])
simulation.setCompStatCase(["Nelly"], ["Independencia" ]) 
print(simulation.parameters)
simulation.run()