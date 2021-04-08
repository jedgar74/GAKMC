#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:09:46 2021

@author: tauger
"""


import numpy as np
import math
import copy 



class Operators():
	"""
	"""



	def __init__(self):
		"""  
		""" 

		self.defPrecision('None')
		# self.typeProblem = typeProblem

		
	# 	def randVar(self, i):
	# 		v = np.random.rand()*(u.upperlimits[i]-u.lowerlimits[i])+u.lowerlimits[i]
	# 		return v
 
 
	def defPrecision(self, x):
		if not x == 'None':
			self.precision = x     
		else:
			self.precision = 'None' 
            
            
	def rounds(self, x):    
		if not self.precision == 'None':
		    return round(x, self.precision) 
		else:
		    return x

				
	def mutationSimple(self, sol):
	# 		u=sol
	# 		i=randint(sol.nVar)
	# 		u[i]=self.randVar(i)
	# 		
		return sol



	def mutationSimple2(self, sol):
		u = copy.deepcopy(sol) 
		sigma = 0.01 
		i = np.random.randint(sol.nVar)
		u.vars[i] = u.vars[i]+ 2*(np.random.rand()-0.5)*sigma 
		
		if u.vars[i] > u.upperlimits[i]:
			u.vars[i] = u.upperlimits[i]
		elif u.vars[i] < u.lowerlimits[i]:
			u.vars[i] = u.lowerlimits[i]	 
		return u
	
    
	def mutation(self, name, sols):
		if name == 'BASIC':
			solx = self.mutationSimple(sols[0])
		elif name == 'BASIC2':
			solx = self.mutationSimple2(sols[0])	
		else: 
			# this instruction allows throwing an exception
			raise ValueError("This mutation method is not defined: "+name)
		return solx


	def crossoverSimple(self, s1, s2):
		i1 = copy.deepcopy(s1)
		i2 = copy.deepcopy(s2) 
		alpha = np.random.randint(i2.nVar)
		beta = np.random.rand()
		# print (  str(alpha) + " "+  str(beta))
		i1.setValue(alpha, s1.getValue(alpha) - beta*(s1.getValue(alpha) - s2.getValue(alpha) )) 
		i2.setValue(alpha, s2.getValue(alpha) + beta*(s1.getValue(alpha) - s2.getValue(alpha) )) 
		
		for g in range(alpha+1, i2.nVar):  
			i2.setValue(g, s1.getValue(g)) 
			i1.setValue(g, s2.getValue(g))
		
		# s1.prints("s1") 
		# s2.prints("s2") 	
		# i1.prints("i1") 
		# i2.prints("i2")
		return [ i1, i2 ] 


	def crossover(self, name, sols):
		if name == 'BASIC':
			solx = self.crossoverSimple(sols[0], sols[1])
		else: 
			raise ValueError("This crossover method is not defined: "+name)
		return solx		  




		
				 
		
	def selection(self, name, psols):
		"""This method allows choosing a specific selection method
		""" 
		if  name =='ROULETTE':
			solx = self.roulette(psols)	 
		else:  
			raise ValueError("This method is not defined: "+name)						
		return solx			
  
		 
		 
	def roulette(self, psols): 
		solx = []
	 
		x = 0
		maxx = -1e100
		minx =  1e100 
		for g in range(psols.popSize): 
			t = psols.getIndividual(g).fitness
			x = x + t 
	 		
			if t > maxx:
				maxx = t 
			elif t < minx:
				minx = t 	
		sumx = x 						
		x = (maxx+1)*psols.popSize - sumx 
			 
		for s in range(2): 
			y = np.random.rand() * x 
			i = 0
			z = 0
		 
			while (z < y):
				z = z + (maxx - psols.getIndividual(i).fitness) + 1  					
				i = i + 1 
				
			q = psols.popSize 
			if i == 0:
				solx.append(psols.getIndividual(0) )
			elif i == q:
				solx.append(psols.getIndividual(q-1))
			else:
				solx.append(psols.getIndividual(i)) 
 
		return solx  		



	def isBetter(self, sols): 
		if sols[0].fitness < sols[1].fitness:
			return True
		else:
			return False
 
