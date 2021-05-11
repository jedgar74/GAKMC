#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:27:41 2021

@author: tauger
"""

import mysql.connector


class DBkm100(object):   
    
    def __init__(self, db=None): 
        
        if db == None:
            db="km100"
        
        self.conexion=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="090509", 
                                  database=db)
        self.con=self.conexion.cursor(buffered=True)
        
        
    def query(self, querytxt, parameters=None): 
        q = (querytxt) 
        if parameters == None:
            self.con.execute(q) 
        else :        
            self.con.execute(q, parameters)
            
        return self.con     
        
        
    def insert(self, inserttxt, val, parameters=None): 
        q = (inserttxt) 
        if parameters == None:
            self.con.execute(q, val) 
        else :        
            self.con.executemany(q, val)
            
        # if len(val)==1:
        #     self.con.execute(q, val) 
        # elif len(val)>1:     
        #     self.con.executemany(q, val)
            
        self.conexion.commit()         



    def nrows(self, parameters=None): 
        res = self.con.fetchone() 
        try:
            return res[0]
        except : 
            return 0   
            
