# -*- coding: utf-8 -*-
"""
RedTower
author: Luis Carlos Rojas Torres
e-mail: redtower.soft@gmail.com
"""
import numpy as np
import num_solvers as ns
import matplotlib.pyplot as plt

class conical_BSF:
    def __init__(self, oR1 = 0.325, oR2 = 0.10, iR = 0.09, length = 1.9, E = 45_000_000):
        self.oR1 = oR1
        self.oR2 = oR2
        self.iR = iR
        self.length = length
        self.E = E
       
    def Rs(self, s):
        if(s >= 0 and s<= self.length):
            return self.oR2+(self.oR1-self.oR2)*(self.length-s)/self.length
        else:
            return 0

    def get_EI(self, s):
        if(s >= 0 and s<= self.length):
            I = 0.25*np.pi*((self.Rs(s))**4-(self.iR**4))
        else:
            return 0
        
        return self.E*I
   

    def get_dEI_dS(self, s):
        return self.E*np.pi*((self.oR2-self.oR1)/self.length)*self.Rs(s)**3

class RSR:
    def __init__(self, length = 3.2, EI = 10000):
        self.length = length
        self.EI = EI
        
    def get_EI(self):
        return self.EI
        

class JOB:
    def __init__(self, bsf, rsr, F=62500,angleL = 45, h = 0.01):
        self.bsf = bsf
        self.rsr = rsr
        self.F = F
        self.angle_at_L = angleL*np.pi/180
        self.h = h
        
    def get_inv_EI(self,s):
        EI = self.bsf.get_EI(s) + self.rsr.get_EI()
        return (1/EI)
    
    def alpha(self, s):
        return self.get_inv_EI(s) * self.bsf.get_dEI_dS(s)
    
    def beta(self, s):
        return self.F*self.get_inv_EI(s) 
    
    def f1(self, s, u1, u2):
        return u2
    
    def f2(self, s, u1, u2):
        return -self.alpha(s)*u2 - self.beta(s)*np.sin(self.angle_at_L-u1)
        

bsf = conical_BSF()
rsr = RSR()
job = JOB(bsf, rsr,62500,45)        
output = ns.shooting_method(job.f1, job.f2, 0, rsr.length, job.h, 0, job.angle_at_L, 51)


'''
bsf = conical_BSF()
x = np.arange(0,3.2,0.01)
y = list()
for i in x:
    y.append(bsf.get_dEI_dS(i))

plt.plot(x,y)
plt.grid()
'''

