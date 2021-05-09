#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:19:38 2021

@author: tauger
"""
# from geopy.geocoders import Nominatim
from geopy import distance


class GPS ( ):
 
    def __init__(self):
        pass



    def calcdistance(self, d1, d2, prints=None): 
        #print(".....",d1)
        s1 = d1.split(",")
        s2 = d2.split(",")
        
        p1 = (s1[1], s1[0]) 
        p2 = (s2[1], s2[0])
         
        d = self.distancebc(p1, p2) 
         
        return d 



    def distancebc(self, p1, p2, prints=None):   
        d = distance.distance(p1, p2)
         
        if prints != None :
            print('valor p1 p2    :', d.km )
         
        return int(d.km )        
    
#valor1 = -68.40151730000002 
#valor2 = 18.6433581
#
#valor1d = -70.65463490000002 
#valor2d = 19.7717673
#
#valor1dd = (18.6433581, -68.40151730000002)
#valor2dd = (19.7717673, -70.65463490000002) 
#
#d = distance.distance(valor1dd, valor2dd)
#print('valor MM DM    :', d.km ) 