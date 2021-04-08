#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:09:46 2021

@author: tauger
"""

from problem.Problem import *
from algorithm.Population import *
import json
import math 
import copy



class GeneticAlgorithm ():   
    
    
	def __init__(self, problem, fileConfig, run=True): 
		super().__init__() 
		self.objProblem = problem  
		self.setParameters(fileConfig)
		self.popul = Population(self.parameters.get('individuals'), self.objProblem, self.parameters.get('initialTypeSolution'))
		self.popul.sort()
		self.objProblem.counter.incCount(self.parameters.get('individuals')) 
		print(self.objProblem.nVar)
		self.stateFinal = copy.deepcopy(self.popul.getBetterSort())
		if  run==True :
			self.geneticAlgorithm(self.stateFinal)
 


	def readParameters(self, nameFile ): 
		"""  Read the algorithm parameters  
		"""
		with open('./files/config/'+nameFile+'.json') as file:
			data = json.load(file)
		 
		return  data 



	def isStopCriteria (self):
		"""   
		"""
		if (self.objProblem.counter.getCount() <= self.objProblem.counter.getLimit()):
			return True  
		else :
			return False 



	def run(self, sol=None):  
		"""   
		"""
		if sol==None :
			self.geneticAlgorithm()
		else :
			self.geneticAlgorithm(sol)

            

	def setParameters(self, fileConfig): 
		"""   Set the algorithm parameters
		"""
		self.parameters = self.readParameters(fileConfig)
 
		for i in range(7):  

			if not 'individuals' in self.parameters :
				self.parameters.update(dict(individuals=10))
				
			if not 'probcrossover' in self.parameters :
				self.parameters.update(dict(probcrossover=1))
					
			if not 'probmutation' in self.parameters :
				self.parameters.update(dict(probmutation=0.15))  
				
			if not 'mutationoper' in self.parameters : 
				self.parameters.update(dict(mutationoper="BASIC2"))	
				 
			if not 'crossoveroper' in self.parameters : 
				self.parameters.update(dict(crossoveroper="BASIC"))	
				
			if not 'selectionoper' in self.parameters : 
				self.parameters.update(dict(selectionoper="ROULETTE"))	 
					
			if not 'initialTypeSolution' in self.parameters : 
				self.parameters.update(dict(initialTypeSolution="RANDOM"))		 	 
 
		
		
	def geneticAlgorithm(self, solution=None): 
		if solution!=None :
			self.popul.addSort(solution)  
            
		self.popul.printFitness("POP(INI)")  
		samples = 1  
		
		while self.isStopCriteria():  
			i = 0    
			while  i < samples  : 
				notCrossover = 0
				par = self.objProblem.op.selection(self.parameters.get('selectionoper'), self.popul) 
				tempSol = par[0] 

				if  np.random.rand() < self.parameters.get('probcrossover'): 
					temp = self.objProblem.op.crossover(self.parameters.get('crossoveroper'), par) 
					tempSol = temp[0]
				else :
					notCrossover = 1 
					
				if  notCrossover == 0 and np.random.rand() < self.parameters.get('probmutation'):	 
					tempSol = self.objProblem.op.mutation(self.parameters.get('mutationoper'), [tempSol]) 
		   
				if  notCrossover == 0 and not self.popul.contains(tempSol) : 
					self.objProblem.evaluate(tempSol)
					self.objProblem.counter.incCount()  
					self.popul.addSort(tempSol)  
					i = i + 1 
					
		self.stateFinal = self.popul.getIndividual(0)  
		self.popul.printFitness("POP(FIN)")   
