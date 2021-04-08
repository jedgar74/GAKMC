#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:27:41 2021

@author: tauger
"""

import mysql.connector


class DBkm100(object):   
    
    def __init__(self): 
        self.conexion=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="090509", 
                                  database="km100")
        self.con=self.conexion.cursor(buffered=True)
        
    def query(self, querytxt, parameters=None): 
        q = (querytxt) 
        if parameters == None:
            self.con.execute(q) 
        else :        
            self.con.execute(q, parameters)
            
        return self.con     
            