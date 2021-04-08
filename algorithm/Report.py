#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:09:46 2021

@author: tauger
"""

import math 



class Report(object): 
	"""  
	""" 
 


	def __init__(self):
		"""  
		"""
		self.solutions = []
		self.label = None 
 


	def getSolution(self, i):
		""" 
		"""
		return self.solutions[i]
 
             

	def nSolutions(self):
		"""  
		"""
		return len(self.solutions)

	
	
	def getLabel(self):
		"""   
		"""
		return self.label 

	
	
	def setLabel(self, label):
		"""  
		"""
		self.label  = label 

	
	
	def add(self, s):
		"""  
		"""
		self.solutions.append(s)

	
	
	def getBetter(self):
		"""  
		"""
		b = self.better()
		return self.solutions[b].fitness
 


	def prints(self):
		"""   
		""" 
		print("Experiments    : " + str(len(self.solutions)) + "  " + self.label) 
		print("-----------------------------------") 
		q = self.better()
		print("Better fitness : "+ str(round(self.solutions[q].fitness, 3))  ) 
		ave = self.average()
		print("Average        : "+ str(round(ave, 3)) ) 
		print("St. Deviation  : "+ str(round(self.stDeviat(ave), 3)) ) 
		print("Better Solution: "+str(q+1)) 
		print("-----------------------------------")  

		self.solutions[q].prints() 
		print("-----------------------------------")  		
  

	def printAllSolutions(self):
		""" 
		"""
		for i in range(len(self.solutions)):  
			self.solutions[i].prints() 
 


	def better(self):
		"""  
		"""
		q = self.solutions[0].fitness  
		k = 0 
		for i in range(1, len(self.solutions)):   
			if self.solutions[i].fitness < q :
				k = i 
				q = self.solutions[i].fitness  
	 
		return k



	def average(self):
		"""  
		"""
		q=0
		for i in range(len(self.solutions)):  
			q = q + self.solutions[i].fitness 
		return q/len(self.solutions) 



	def stDeviat(self, media):
		"""  
		"""
		q=0 
		for i in range(len(self.solutions)):  
			q= q + (self.solutions[i].fitness - media)**2 
		 	
		return math.sqrt(q /len(self.solutions)) 



	def nBetter(self, b):
		"""  
		"""
		q = 0 
		for i in range(len(self.solutions)): 
			if self.solutions[i].fitness == b:
				q = q + 1  
		 	
		return q 
