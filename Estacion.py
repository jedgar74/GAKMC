#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 11:41:13 2021

@author: tauger
""" 
from Vehiculo import * 
import statistics


class Estacion(object):   
    def __init__(self, name, nv =0):
        self.nv = nv
        self.name = name 
        self.empresa = 0
        self.v = []
        self.mvaveh = []
        self.id_veh = []
        self.f = []
        self.ninactive = 0
        
        
    def add(self, mva, tipo,  fec, stat):
         vv = Vehiculo(mva, tipo)
         vv.add(fec, stat)
         self.v.append(vv)     
         self.mvaveh.append(mva)   
         self.nv = self.nv+1 
         try:
            if self.f.index(fec) == -1:
                self.f.append(fec) 
         except:
            self.f.append(fec)
         
            
            
    def add2(self, mva, idv, tipo,  fec, stat):
         vv = Vehiculo(mva, tipo)
         vv.add(fec, stat)
         self.v.append(vv)        
         self.mvaveh.append(mva) 
         self.id_veh.append(idv)   
         self.nv = self.nv+1 
         try:
            if self.f.index(fec) == -1:
                self.f.append(fec) 
         except:
            self.f.append(fec)      
            
            
            
    def addD(self, mva,  fec, stat):
         idv = self.mvaveh.index(mva)
         self.v[idv].add(fec, stat)  
         try:
            if self.f.index(fec) == -1:
                self.f.append(fec) 
         except:
            self.f.append(fec)
     
        
    def gets(self, mva):
        try:
            if self.mvaveh.index(mva) != -1:
                return True
            else :    
                return False 
        except:
            return False    
        
        
    def compare(self, mva, fecha, stat):
        try:
            idv = self.mvaveh.index(mva) 
            if idv != -1:  
                self.v[idv].setstatus(fecha, stat)
            else :    
                # print('NO LIST: ', mva)
                pass
        except:
            # print('NO LIST: ', mva)
            pass
        
        
    def prints(self):
        print('Nombre de estación  ', self.name)
        print('Número de vehículos ', len(self.mvaveh))        
        for j in range(len(self.mvaveh)):  
            self.v[j].prints()    
            
            
    def prints2(self):
        print('Nombre de estación  ', self.name)
        print('Número de vehículos ', len(self.mvaveh))        
        for j in range(len(self.mvaveh)):  
            self.v[j].prints2() 

            
    def indtip(self):
        print("   ") 
        self.tip = [] 
        self.ntip = [] 
        for i in range(len(self.mvaveh)):   
            ind = 0
            c = self.v[i]
            try:
                ind = self.tip.index(c.tipo) 
                if ind != -1:
                    self.ntip[ind] = self.ntip[ind] + 1
                else :    
                    self.tip.append(c.tipo) 
                    self.ntip.append(1)
            except:  
                self.tip.append(c.tipo) 
                self.ntip.append(1)  
#            if self.verveh(c) == 1:   
#                # print( '*** 1' ) 
#                self.ntip[ind] = self.ntip[ind] - 1
#                self.ninactive = self.ninactive + 1
#                self.v[i].active = False
                
        print(self.tip, '\n', self.ntip)           
        return [self.tip, self.ntip]
        
        
    def indtipc(self):
        print("   ") 
        self.tipc = []  
        self.tipd = [] 
        self.tipe = [] 
        dd = [0] * len(self.f)
        #print(self.f)  
        
        for i in range(len(self.tip)):  
            ind = 0
            for k in range(len(self.mvaveh)):   
                c = self.v[k]
                #print(c.contipos(['On Rent']))
                if c.tipo == self.tip[i] and c.active == True:
                    ind = ind + 1
                    for j in range(len(c.fecha)):  
                        #print(self.f, c.fecha)
                        e = self.f.index(c.fecha[j])
                        if c.status[j] == 'On Rent': 
                            dd[e] = dd[e] + 1
                            
            self.tipc.append(max(dd))   
            self.tipd.append(round(sum(dd)/(len(self.f)),3) ) 
            self.tipe.append(round(statistics.stdev(dd),3))   
            dd = [0] * len(self.f)      
            
        print(self.tipc, '\n', self.tipd, '\n', self.tipe)           
        return [self.tipc, self.tipd, self.tipe]
    
        
    def indtipg(self, cond): 
        print("   ")
        self.tipc = []  
        self.tipd = [] 
        self.tipe = [] 
        dd = [0] * len(self.f)
        #print(self.f)  
        
        for i in range(len(self.tip)):  
            ind = 0
            for k in range(len(self.mvaveh)):   
                c = self.v[k]
                if c.tipo == self.tip[i] and c.active == True: 
                    ind = ind + 1
                    for j in range(len(c.fecha)):  
                        #print(self.f, c.fecha)
                        e = self.f.index(c.fecha[j])
                        for w in range(len(cond)): 
                            if c.status[j] == cond[w]: 
                                dd[e] = dd[e] + 1
                                
            self.tipc.append(max(dd))   
            self.tipd.append(round(sum(dd)/(len(self.f)),3) ) 
            self.tipe.append(round(statistics.stdev(dd),3))    
            
            dd = [0] * len(self.f)                
        print(self.tipc, '\n', self.tipd, '\n', self.tipe)    
        return [self.tipc, self.tipd, self.tipe]    
        
        
    
    def indtiplap(self, cond):   
        print("   ")
        vtotd = []
        vmaxd = [] 
        vmind = [] 
        vprod = [] 
        vintd = [] 
        
        for i in range(len(self.tip)):    
            vtot = []
            vmax = [] 
            vmin = [] 
            vpro = [] 
            vint = [] 
            for k in range(len(self.mvaveh)):   
                c = self.v[k]
                if c.tipo == self.tip[i] and c.active == True:
                    d = c.contipos(cond) 
                    vtot.append(d[0])
                    vmax.append(d[1])
                    vpro.append(d[2])
                    vint.append(len(d[3])-1)
                    if len(d[3]) == 1:
                        vmin.append(0) 
                    else :  
                        e = []   
                        e.extend(d[3]) 
                        e.sort()
                        vmin.append(min(e[1:])) 
            vtotd.append(vtot)
            vmaxd.append(vmax)
            vmind.append(vmin)
            vprod.append(vpro) 
            vintd.append(vint) 
                        
        print(len(self.f), '\n', vtotd, '\n', vmaxd, '\n', vmind, '\n', vprod, '\n', vintd) 
        return [len(self.f), vtotd, vmaxd, vmind, vprod, vintd]               
             
           
    # Verificar si un auto figura como fuera de servicio robado o extraviado
    def verveh(self, veh, cond= ['Missing', 'Stolen'] ): 
        auto = 0
        a  = 0        
        for j in range(len(veh.fecha)):
            for i in range(len(cond)):
                if veh.status[j] == cond[i]:
                    a  = a + 1
        if (a/len(veh.fecha)) > 0.8:     
            auto = 1
            print( '*** 1', veh.mva) 
        return auto
    
    
    # definir función de evaluación, recorrer de forma vertical los vehiculos rentados y disponibles y determinar si supera el valor máximo estimado por cada grupo
    def ver(self, kindof, nkindof, fec): 
        r = ['On Rent']  
        m = ['CHEQUEO', 'In Maintenance', 'STOP'] 
        d = ['DISPONIBLE', 'AVAILABLE', '0', 'Non-Rev. Transfer']
        rr= [ ]
        rd= [ ]         
        fo= [ ]    
        # return [fo, rr, rd]   
         
        for ii in range(len(nkindof)):  
            for i in range(len(kindof)):  
                 RR = 0 
                 RD = 0 
                 for w in range(len(fec)): 
                     for j in range(len(self.mvaveh)): 
                        c = self.v[j]
                        for ff in range(len(c.fecha)): 
                            if fec[w] == c.fecha[ff]:  
                                if c.tipo == kindof[i] and c.active == True and fec[w] == c.fecha[j]: 
                                    if c.status[j] in r: 
                                        RR = RR +1
                                    
                                    if c.status[j] in r or c.status[j] in m : 
                                        RD = RD +1 
                                    break    
                  
                 rr.append(RR )                            
                 rd.append(RD )       
                 if RR > nkindof[ii][i] or RD > nkindof[ii][i]: 
                     fo.append(1)   
                 else :    
                     fo.append(0)                     
    
        return [sum(fo), fo, rr, rd]    
    



   