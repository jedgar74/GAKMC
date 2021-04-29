#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:02:10 2021

@author: tauger
"""
from HistoricalProjection import *
import sys

# ...............................
# ejecutar la simulación
# ...............................

historicalProj = HistoricalProjection() 
a = int(sys.argv[2]) +1
historicalProj.setfinitest([a, 1, 1])
historicalProj.setffintest([a, 1, 7]) 
historicalProj.setweekstraining(52)
historicalProj.setCompCase([sys.argv[1]])
#historicalProj.setCompStatCase(["Nelly"], ["Independencia" ]) 
print(historicalProj.parameters)
historicalProj.run()
