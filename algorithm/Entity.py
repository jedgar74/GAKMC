#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:27:41 2021

@author: tauger
"""

from problem.Problem import *
from algorithm.Report import Report 
from algorithm.GeneticAlgorithm import *  
from datetime import datetime, date, time, timedelta
import calendar



class Entity(object): 
	"""
	The class encapsulates the operation of the algorithm and the parameters associated with the problem
	"""


	""" ATTRIBUTES   
	"""


	def __init__(self, problem, args):
		"""  
		"""
		self.problem = problem  
		self.parameters = args[0]
		self.nEvals = args[1]
		self.nExperim = args[2]
		self.stats = Report() 
		self.allsolutions = [] 
 
 

	def run(self):
		""" Run the Genetic Algorithm
		"""
     
		self.problem.counter = Counter(self.nEvals) 
		self.stats.setLabel("GA---"+self.parameters+"["+str(self.nEvals)+"]");

		print("\n Experiments to GA" )
		for e in range(self.nExperim):
			 
			print(" "+str(e), self.problem.nVar)
			GA = GeneticAlgorithm(self.problem, self.parameters) 
			self.stats.add(GA.stateFinal)    
    										
			self.problem.counter = Counter(self.nEvals)  
		
		print("\n") 
		self.stats.prints();
		print("") 
		self.stats.printAllSolutions();  
        
 
        
        
	def getSolution(self, i = None):
		""" returns the solution or solutions stored in Report
		""" 
     
		if (i == None) :
			return self.stats.getSolutionComplete()
            
		else :
			return self.stats.getSolutionComplete(i)
