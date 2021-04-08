#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:09:46 2021

@author: tauger
"""

from algorithm.Solution import *



class Population(object):  
	
    
    
	def __init__(self, popSize, problem, init="RANDOM" ): 
		self.popSize = popSize 
		self.generateRandom(problem, init) 
		
        
		
	def generateRandom(self, problem, init):	
		self.popul = []
		
		for i in range(self.popSize):
			f = Solution(problem, init) 
			problem.evaluate(f) 
			self.popul.append(f)
		
		
        
	def sort(self):	
		size = self.popSize

		for i in range(1, size) :  
			for j in range(size - 1) : 
				if (self.popul[j].fitness > self.popul[j+1].fitness) :
					aux = self.popul[j]
					self.popul[j] = self.popul[j+1]
					self.popul[j+1] = aux 
 
		
		
	def getBetterSort(self): 
		return self.popul[0]   
		 
				
 		
	def addSort(self, insolution, expansion = False ) :
		isBetter = False  
		lenpop = len(self.popul)
		
		for t in range(self.popSize): 
			if ( insolution.fitness < self.popul[t].fitness )  :
				self.add(t, insolution);  
				isBetter = True;
				break  
				
		if expansion == True :		
			if isBetter == False :
				self.popul.append(insolution); 
		else :
			if isBetter == True :
				self.popul.pop(lenpop)
 
		self.popSize = len(self.popul)  



	def add(self, index, insolution) :
		self.popul.insert(index, insolution);
		self.popSize = len(self.popul)



	def printFitness(self, label) : 
		print("--> " + label + " ", end="")
		
		for i in range(self.popSize): 
			print( str(round(self.popul[i].fitness, 3)) + " ", end = "") 
		
		print("\n") 



	def getIndividual(self, l):  
		return self.popul[l]  
  
	 
        
	def contains(self, insolution ) : 
		isContains = False
		
		for t in range(self.popSize): 
			if self.popul[t].isEquals(insolution) : 
				isContains = True 
				break  
				
		return isContains
		
    
 
