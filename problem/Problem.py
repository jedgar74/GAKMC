#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 09:03:25 2021

@author: tauger
"""


from problem.Counter import * 
from algorithm.Operators import * 
import numpy as np  



class Problem(object):  
	
	
	
	def __init__(self): 
		self.nVar = 0   
		self.counter = Counter(0)  
		self.roundFitness = 1	   
		self.upperlimits = None 
		self.lowerlimits = None
