#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 09:16:44 2021

@author: tauger
"""

from problem.Problem import *  
import numpy as np  


class CarRentalFleetR3 (Problem): 
	""" 
	    
	"""
 

	def __init__(self, namInst=None): 
		super().__init__()
		self.nameShort = "CRFP"     
		self.typeState = "REAL" 
		self.op = Operators()  
 
		if (not namInst == None): 
			self.readInstance(namInst) 
         
 
	def readInstance(self, namFile):
		"""  Read the parameters of the problem instance
		""" 
		pass
#		self.TYPES = [] 
#		self.MANMEDIA = [] 
#		self.MAXIMA = [] 
#		self.MEDIA = []  
#		self.STDV = [] 
#             
#		self.STATIONS = 0  
#        
#		with open('./files/instances/'+namFile, 'r') as fileobj:
#		    content = fileobj.read()
#		    lines = content.split('\n')   
#        
#		# Each cycle is a instance
#		cntr = '' 
#        
#		for j in range(len(lines)):  
#			r = lines[j].split()     
#            
#          
#			if (len(r) != 0):      
#				if (cntr == '' ): 
#					if (r[0]=='STATIONS:'):
#						self.STATIONS = int(r[1])
#						print(self.STATIONS) 
#					elif (r[0]=='SETV:'):
#						self.SETV = int(r[1])
#						print(self.SETV)  
# 
#					elif (r[0]=='TOTALV:'):
#						self.TOTALV = r[1:len(r)]
#						print(self.TOTALV ) 
# 
#					elif (r[0]=='TYPES:'):
#						cntr = 'TYPES'
#						print(cntr )  
#                        
#					elif (r[0]=='MAXIMA:'):
#						cntr = 'MAXIMA'
#						print(cntr ) 
#					elif (r[0]=='MEDIA:'):
#						cntr = 'MEDIA'
#						print(cntr )  
#					elif (r[0]=='STDV:'):
#						cntr = 'STDV'
#						print(cntr )          
#                        
#					elif (r[0]=='MANMAXIMA:'):
#						cntr = 'MANMAXIMA'
#						print(cntr )                        
#					elif (r[0]=='MANMEDIA:'):
#						cntr = 'MANMEDIA'                        
#						print(cntr )                        
#                        
#					elif (r[0]=='DISMAXIMA:'):
#						cntr = 'DISMAXIMA'
#						print(cntr )                        
#					elif (r[0]=='DISMEDIA:'):
#						cntr = 'DISMEDIA'                        
#						print(cntr )                        
#                        
#
#				elif (r[0]=='TYPES:'):
#					cntr = 'TYPES'
#					print(cntr ) 
#				elif (r[0]=='MAXIMA:'):
#					cntr = 'MAXIMA'
#					print(cntr ) 
#				elif (r[0]=='MEDIA:'):
#					cntr = 'MEDIA'
#					print(cntr )  
#				elif (r[0]=='STDV:'):
#					cntr = 'STDV'
#					print(cntr )  
#				elif (r[0]=='MANMAXIMA:'):
#					cntr = 'MANMAXIMA'
#					print(cntr )   
#				elif (r[0]=='MANMEDIA:'):
#					cntr = 'MANMEDIA'
#					print(cntr )                   
#				elif (r[0]=='DISMAXIMA:'):
#					cntr = 'DISMAXIMA'
#					print(cntr )   
#				elif (r[0]=='DISMEDIA:'):
#					cntr = 'DISMEDIA'
#					print(cntr )                     
#                    
#                    
#				elif (cntr == 'TYPES' ):                
#					self.TYPES.append(r) 
#					print(self.TYPES)              
#                 
#				elif (cntr == 'MAXIMA' ):                
#					self.MAXIMA.append(r) 
#					print(self.MAXIMA)                
#       
#				elif (cntr == 'MEDIA'):                
#					self.MEDIA.append(r) 
#					print(self.MEDIA)              
#       
#				elif (cntr == 'STDV'):                
#					self.STDV.append(r) 
#					print(self.STDV)  
#                
#				elif (cntr == 'MANMAXIMA' ):                
#					self.MANMAXIMA.append(r)  
#					print(self.MANMAXIMA)  
#                
#				elif (cntr == 'MANMEDIA' ):                
#					self.MANMEDIA.append(r)  
#					print(self.MANMEDIA)  
#                
#				elif (cntr == 'DISMAXIMA' ):                
#					self.DISMAXIMA.append(r)  
#					print(self.DISMAXIMA)  
#                
#				elif (cntr == 'DISMEDIA' ):                
#					self.DISMEDIA.append(r)  
#					print(self.DISMEDIA)  
#                    
#                    
#                    
#                    
#		self.nVar =self.SETV *  self.STATIONS 
#		self.upperlimits = np.ones(self.nVar) 
#		self.lowerlimits = np.zeros (self.nVar) 
#		# print(self.perm)        
#		self.evals()
        

	def evaluate(self, s, printing=""):
		"""   This method assesses fitness function
		""" 
		count = 0  
		counte = 0  
		self.proposal = []
		self.valxstation = []
        
        
        # podemos Definir la función objetivo Como aquella que brinde 
        # la menor cantidad de conflictos posibles definiendo conflicto 
        # como algo una función que no debe superar ciertos límites

        # aquellos conflictos que generen obstaculización en el desarrollo
        # de la labor deben ser cumplido a toda costa y aquellos que sean
        # tentativos opcionales se calificarán con una pena menor
        
        # las funciones asociadas a las restricciones puede ser Dinámico, 
        # es decir puede variar con el tiempo. Entre menor sea el 
        # conflicto mejor será la propuesta   
        
        # para lo anterior debemos definir unos pesos asociadas a las 
        # restricciones aquellos aquellas restricciones que sean 
        # fundamentales deben tener un peso alto aquellas que no
        # un valor bajo
        
        # el total de vehículos por grupo no puede ser menor que la media utilizada diariamente
		obj1 = []  
        
        # el total de vehículos por grupo es mayor que el máximo de vehículos diario  por grupo
		obj2 = []    
        
		obj3 = []  
		obj4 = []   
          
		obj5 = []  
		obj6 = [] 
		w =[1.0, 1.0, 1.0, 0, 0.15, 0.05]
        
        
		for i in range(self.stations.STATIONS):  
			proposalxstation = []
			tmp = []
            
			obj1t = 0 
			obj2t = 0
			obj3t = 0
			obj4t = 0
			obj5t = 0
			obj6t = 0
            
			for j in range(self.stations.SETV):  
                # Definimos la propuesta de aumento o disminución de vehículos por grupo 
				# dif = s.vars[self.stations.STATIONS*i+j]-0.5 
				dif = s.vars[self.stations.SETV*i+j]-0.5
                
				# print("")    
				vs = int( round(dif * self.variab[i][j])  )
				# print(vs, dif * self.variab[i][j])  
				tot = int(self.stations.OPFLMEDIA[i][j]) + vs
				# -J tot = int(self.stations.TYPES[i][j]) + vs
				# print(dif, self.variab[i][j], vs, tot)   
                
				# definimos las diferentes condiciones
                
				# se penaliza si el número de vehículos es menor Qué es la media histórica
				if tot < float(self.stations.MEDIA[i][j]):
					obj1t = obj1t + int(-tot + float(self.stations.MEDIA[i][j]))                   
					# print("") 
					# count = count+1  
                    
                    
				#  se penaliza si el número de vehículos totales Es mayor que el estimado total
				if tot  >  self.maxveh[i][j]:
					# print("")
					obj2t = obj2t + (tot - self.maxveh[i][j]) #int(-vs + float(self.MEDIA[i][j]))                                       
                       
                    
                #  Se penaliza sí estimado de vehículos Es mayor que el total del mismo grupo en un porcentaje   
				# dv = float(self.MAXIMA[i][j])+(self.variab[i][j]/2)
				# dv = (dv - int(self.TYPES[i][j]))/int(self.TYPES[i][j])
				# dc = (tot - int(self.TYPES[i][j]))/int(self.TYPES[i][j]) 
#				if dv  >  0.10 and dc  >  0.30:
#					print("ccccccccccccccccccccccccccccc")
#					count = count + dc #int(-vs + float(self.MEDIA[i][j]))   
#				fv = 0              
                
				if int(self.stations.OPFLMEDIA[i][j]) + vs  <  float(self.stations.MAXIMA[i][j]):     
				# -J if int(self.stations.TYPES[i][j]) + vs  <  float(self.stations.MAXIMA[i][j]):      
					obj3t = obj3t + 1                                 
                    
#				if tot  <  (float(self.MAXIMA[i][j])*(1+float(self.MANMEDIA[i][j])) ):
#					count = count + 0 #int(-vs + float(self.MEDIA[i][j]))                                       
#					# print("") 
#					# count = count+1    
                    
				if int(self.stations.OPFLMEDIA[i][j])  == 0 :                    
				# -J if int(self.stations.TYPES[i][j])  == 0 :
					tmpc = 0
				else :   
					tmpc = (tot - float(self.stations.MAXIMA[i][j])) / int(self.stations.OPFLMEDIA[i][j])
					# -J tmpc = (tot - float(self.stations.MAXIMA[i][j])) / int(self.stations.TYPES[i][j])
				tmp.append(tmpc)  
                
				fc = 0 
                
				if int(self.stations.OPFLMEDIA[i][j]) > 0 :
					fc = tot/int(self.stations.OPFLMEDIA[i][j])
				# -J if int(self.stations.TYPES[i][j]) > 0 :
					# -J fc = tot/int(self.stations.TYPES[i][j])
                    
                    
                    
				if tot > 0 and int(self.VPRC[i][j])/tot < 0.25 :
					obj4t = obj4t + int(self.VPRC[i][j])/int(self.stations.OPFLMEDIA[i][j]) 
					# -J obj4t = obj4t + int(self.VPRC[i][j])/int(self.TYPES[i][j])  
					
				if int(self.VPRC[i][j]) > 0 and fc*int(self.VFEC[i][j])/int(self.VPRC[i][j]) < 0.25 :
					obj4t = obj4t + 1 - 4*int(self.VFEC[i][j])/int(self.VPRC[i][j])
				
				if int(self.VPRC[i][j]) > 0 and fc*int(self.VFEC[i][j])/int(self.VPRC[i][j]) > 0.75:
					obj4t = obj4t +  4*(int(self.VFEC[i][j])/int(self.VPRC[i][j]) - 0.75)  	               
                

                
				if ( 2/3*(float(self.stations.DISPMEDIA[i][j]) + vs) +  float(self.stations.MEDIA[i][j])  )  > float(self.stations.MAXIMA[i][j])  :
					obj5t = obj5t + 2/3*(float(self.stations.DISPMEDIA[i][j]) + vs) + float(self.stations.MEDIA[i][j]) - float(self.stations.MAXIMA[i][j])
					# print("5. ", j, vs, obj5t )   
                    
                    
				if ( 2/3*(float(self.stations.DISPMEDIA[i][j]) + vs) +  float(self.stations.MEDIA[i][j])  )  < float(self.stations.MAXIMA[i][j])  :
					obj6t = obj6t - 2/3*(float(self.stations.DISPMEDIA[i][j]) + vs) + float(self.stations.MEDIA[i][j]) + float(self.stations.MAXIMA[i][j])
					# print("6. ", j, vs, obj6t)     
                    
				proposalxstation.append(vs)                    
                    
			obj1.append(obj1t)
			obj2.append(obj2t)
			obj3.append(obj3t)
			obj4.append(obj4t)
			obj5.append(obj5t)
			obj6.append(obj6t)
				
				
			# print(tmp)                
			tmp  = sum(tmp) / self.stations.SETV 
#			print(tmp)    
#			print(self.proposal)	
            
#			print(i, round(tmp, 3) , proposalxstation)                    
			self.proposal.append(proposalxstation)  
			self.valxstation.append(tmp) 
		#----CCC----print(self.proposal)   
        
        # We add the necessary restrictions
#		print("--> ", sum(np.asarray(obj1)), sum(np.asarray(obj2)), sum(np.asarray(obj3)), sum(np.asarray(obj4)), sum(np.asarray(obj5)), sum(np.asarray(obj6)) )
		count = sum(np.asarray(obj1)*w[0]) + sum(np.asarray(obj2)*w[1]) + sum(np.asarray(obj3)*w[2]) + sum(np.asarray(obj4)*w[3]) + sum(np.asarray(obj5)*w[4]) + sum(np.asarray(obj6)*w[5])
 
		# print(count)
		s.setFitness(count)
        
		if printing != "":
			# print("h", "onAvailability", onAvailability)  
			# print("h", "onConflicts", onConflicts)     
			# print("h", "onLectures", onLectures)    
			# print("h", "onRoomCapacity", onRoomCapacity)   	
			# print()             
            
			# print("s", "onRoomStability", onRoomStability) 
			# print("s", "onIsolatedLectures", onIsolatedLectures)  
			# print("s", "onMinWorkingDays", onMinWorkingDays)  
			# print("s", "onRoomOccupation", onRoomOccupation) 
			
			print("\nFitness", count)   	
			print()   
			# print(self.variab)             
			# for i in range(self.nVar):     
				# if (s.vars[i] !=0):      
					# day = (i  //  (self.periods*self.rooms))
					# periods = i % self.periods
					# room = ((i // self.periods) % self.rooms)
					# print("day", day+1, "room", self.irooms[room][0], "periods", periods+1, self.icourses[s.vars[i] -1][0], int(self.icourses[s.vars[i] -1][4]), self.irooms[room][1])          
                    
  
	def evals(self):
		# Tasa de variabilidad máxima positiva y negativa,, 
		# en este caso sería la diferencia entre el valor máximo histórico y la media de vehículos alquilados de forma diaria.
		self.variab = []
		for i in range(self.stations.STATIONS):  
			veh = []
			for j in range(self.stations.SETV): 
				va = 2.0*(float(self.stations.MAXIMA[i][j])  - float(self.stations.MEDIA[i][j]) )
				if va  < 1:
					va = 1
				veh.append(va)
			self.variab.append(veh)   
                
        # Calculamos el número máximo de vehículos requerido en el peor de los casos, de la siguiente forma 
        # máximo histórico más estimado vehículos de mantenimiento más vehículos de contingencia definición por un factor x 
		self.maxveh = []
		fact =1
		for i in range(self.stations.STATIONS):   
			veh = []            
			for j in range(self.stations.SETV): 
				veh.append( (float(self.stations.MAXIMA[i][j])+float(self.stations.MANMEDIA[i][j])) + fact )
			self.maxveh.append(veh) 


                        
	def setInstance(self, stations, STDV=[]): 
		self.stations = stations   
        
		self.nVar = self.stations.SETV * self.stations.STATIONS
		print("*** --- ", self.stations.MAXIMA)  
		print("*** --- ", self.stations.MEDIA)
		if STDV == []:
			self.STDV = np.ones(self.nVar).tolist()
		else : 
			self.STDV = STDV            
            
		self.upperlimits = np.ones(self.nVar) 
		self.lowerlimits = np.zeros (self.nVar) 
        
		self.VFEC = []
		self.VPRC = []
		# print("*** VFEC3 ", VFEC)  
		for i in range(self.stations.STATIONS):    
			veh = []              
			vec = []             
			for j in range(self.stations.SETV): 
				fact = 0
				facc = 0
				# print("*** VFE6 ", VFEC[i][j])  
				# print("*** VFE6 ", len(VFEC[i][j]))  
				for l in range(len(self.stations.VFEC[i][j]) ):
					if self.stations.VFEC[i][j][l]  > 0:
						facc = facc +1
					if self.stations.NumeroDias > 0:
						if self.stations.VFEC[i][j][l]/self.stations.NumeroDias > 0.8:
						    fact = fact +1  
				veh.append(fact  )
				vec.append(facc  )
			self.VFEC.append(veh) 
			self.VPRC.append(vec) 
		# print("*** VFE3 ", self.VPRC, self.VFEC) 
		 
		self.evals()
         
