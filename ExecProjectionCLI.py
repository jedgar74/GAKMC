#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:02:10 2021

@author: tauger
"""
from Projection import *
import sys

# ...............................
# ejecutar la simulación
# ...............................

simulation = Projection()
#simulation = Simulation(parameters)
a = int(sys.argv[2]) +1
simulation.setfinitest([a, 1, 1])
simulation.setffintest([a, 1, 7]) 
simulation.setweekstraining(52)
simulation.setCompCase([sys.argv[1]])
#simulation.setCompStatCase(["Nelly"], ["Independencia" ]) 
print(simulation.parameters)
simulation.run()
