#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 10:16:51 2021

@author: tauger
"""


from HistoricalProjection import *

# ...............................
# ejecutar la simulación
# ...............................

historicalProj = HistoricalProjection()
#historicalProj = Simulation(parameters)

historicalProj.setfinitest([2020, 1, 1])
historicalProj.setffintest([2020, 1, 7]) 
historicalProj.setweekstraining(52)
historicalProj.setprints(True)
#historicalProj.setCompCase(["Nelly"])
historicalProj.setCompStatCase(["Nelly"], ["Independencia" ]) 
print(historicalProj.parameters)
historicalProj.run()
