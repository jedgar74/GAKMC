#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 09:03:25 2021

@author: tauger
"""

class Counter(object): 
  """  Defines the counter for the number evaluations of fitness. The limit variable 
  defines the upper limit of evaluations and the count variable records the current 
  count up to limit  
  """

  """ ATTRIBUTES  
  """


  def __init__(self, limit):
    """  
    """
    self.limit = limit
    self.count = 0



  def getCount(self):
    """  
    """
    return self.count 



  def setCount(self, count):
    """  
    """
    self.count = count



  def getLimit(self):
    """  
    """
    return self.limit 



  def setLimit(self, limit):
    """  
    """
    self.limit = limit 



  def incCount(self, u=1):
    """ 
    """
    self.count = self.count+u
 
