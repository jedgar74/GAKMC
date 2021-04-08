#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:09:46 2021

@author: tauger
"""

import numpy as np 



class Solution(object): 
	
    
    
	def __init__(self, problem, init):
		"""  
		"""  
		self.fitness = None 
		self.nVar = problem.nVar	
		self.vars = np.zeros(self.nVar)  
		self.upperlimits  = problem.upperlimits
		self.lowerlimits  = problem.lowerlimits
		if init == "RANDOM"  :
			self.vars = self.initRandomizePerArray()  
				
		self.roundFitness = problem.roundFitness						
		
        
        
	def evaluate(self, problem):
		"""   
		""" 
		self.fitness = problem.evaluate()	
	 
		
    
		
	def initRandomizePerArray(self):
		"""   
		"""  
		u = np.zeros(self.nVar)
		
		for i in range(self.nVar): 
			u[i] = np.random.rand()*(self.upperlimits[i] - self.lowerlimits[i]) + self.lowerlimits[i]
				
		return u	 
	
    
	
	def getValue(self, u ):	
		return self.vars[u ]
	
    
    
	def setValue(self, i, u ):	
		self.vars[i] = u
	 
	 
		    
	def setFitness(self, fit):
		"""   
		""" 
		self.fitness = fit	
		
        
		
	def prints(self, name= ""):
		"""   
		"""
		print ( name + " ", end = "")
		for i in range(self.nVar):   
			print (  str(round(self.getValue(i), self.roundFitness)) + " ", end = "")
		try:
			print ( " ::: " +  str(round(self.fitness, self.roundFitness)) ) 
		except :    
			print ( " ::: None "  )  
		
		
        
	def isEquals(self, sol):	
		isEquals = True
		for i in range(self.nVar):
			if self.vars[i] != sol.getValue(i) :
				isEquals = False
				break 	
		return isEquals
 
