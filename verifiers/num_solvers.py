# -*- coding: utf-8 -*-
"""
RedTower
author: Luis Carlos Rojas Torres
e-mail: redtower.soft@gmail.com
"""
import numpy as np
import matplotlib.pyplot as plt

def fx(x,y):
    return -1000*y + 3000 - 2000*np.exp(-x)

def RK4(f1,x_initial = 0, x_final = 0.05, h = 0.001, initial_condition = 0):
    s = np.arange(x_initial, x_final+h, h)
    
    y = list()
    y.append(initial_condition)
    
    for i in s[1:]:
        k1 = fx(i,y[-1]) 
        k2 = fx(i+0.5*h, y[-1] + 0.5*h*k1)
        k3 = fx(i+0.5*h, y[-1] + 0.5*h*k2)
        k4 = fx(i+h, y[-1] + 0.5*h*k1)

        y.append( y[-1] + h*(k1 + 2*k2 + 2*k3 + k4)/6)

    fig, axes = plt.subplots(1, 1, figsize=(6, 6), sharex=True,sharey=True, squeeze=False)
    axes[0,0].set_title("u1")
    axes[0,0].plot(s,y)
    
    return (s,y)    
    
RK4(fx)

def RK4_for_2eq(f1, f2, x_initial = 0, x_final = 1, h = 0.1, u10 = 0, u20 = 0):
    '''
    RK4 for two equations:
        u1' = f1(x,u1,u2)
        u2' = f2(x,u1,u2)
        s = x_initial to x_ final with steps of h
    Parameters
    ----------
    f1 : double
        right hand of equation1
    f2 : TYPE
        right hand of equation2
    x_initial : TYPE, optional
        initial domain value 
    x_final : TYPE, optional
        final domain value 
    h : TYPE, optional
        Step in domain discretization
    u10 : TYPE, optional
        initial value in u1
    u20 : TYPE, optional
        initial value in u2

    Returns
    -------
    s : TYPE
        DESCRIPTION.
    u1 : TYPE
        DESCRIPTION.
    u2 : TYPE
        DESCRIPTION.

    '''
    u1 = list() # phi
    u2 = list() # k
    s = np.arange(x_initial, x_final+h, h)
    
    u1.append(u10)
    u2.append(u20)
    
    for i in s[1:]:
        k1u1 = f1(i,u1[-1],u2[-1])
        k1u2 = f2(i,u1[-1],u2[-1])
                        
        k2u1 = f1(i+0.5*h, u1[-1]+0.5*h*k1u1, u2[-1]+0.5*h*k1u2)
        k2u2 = f2(i+0.5*h, u1[-1]+0.5*h*k1u1, u2[-1]+0.5*h*k1u2)
               
        k3u1 = f1(i+0.5*h, u1[-1]+0.5*h*k2u1, u2[-1]+0.5*h*k2u2)
        k3u2 = f2(i+0.5*h, u1[-1]+0.5*h*k2u1, u2[-1]+0.5*h*k2u2)
                
        k4u1 = f1(i+h, u1[-1]+0.5*h*k3u1, u2[-1]+0.5*h*k3u2)
        k4u2 = f2(i+h, u1[-1]+0.5*h*k3u1, u2[-1]+0.5*h*k3u2)

        u1.append(u1[-1] + h*(k1u1+2*k2u1+2*k3u1+k4u1)/6)
        u2.append(u2[-1] + h*(k1u2+2*k2u2+2*k3u2+k4u2)/6)
        
    '''
    fig, axes = plt.subplots(1, 2, figsize=(6, 6), sharex=True,sharey=True, squeeze=False)
    axes[0,0].set_title("u1")
    axes[0,0].plot(s,u1)
    
    axes[0,1].set_title("u2")
    axes[0,1].plot(s,u2)
    '''
    return (s,u1,u2)

def shooting_method(f1, f2, x_initial= 0, x_final=1, h = 0.01, bv_at_x_initial = 0, bv_at_x_final= 1, total_iterations = 50, tolerance = 0.01):
    sk = list()
    ite = 1
    
    uNsk_add1 = 0
    uNsk = 0
    
    s = list()
    u1 = list()
    u2 = list()
    
    while( ite < total_iterations ):
        
        if(ite == 1):
            sk.append((bv_at_x_final-bv_at_x_initial)/(x_final-x_initial))
            
        elif(ite == 2):
            uNsk = u1[-1]
            sk.append( sk[-1] + ( bv_at_x_final - uNsk )/( x_final - x_initial ))
                        
        else:
            uNsk_add1 = u1[-1]
            sk.append( sk[-2] + (sk[-1]-sk[-2])*(bv_at_x_final-uNsk)/(uNsk_add1-uNsk) )
            uNsk = uNsk_add1
            
        
        (s,u1,u2) = RK4_for_2eq(f1, f2, x_initial, x_final, h, bv_at_x_initial, sk[-1])
        print(" ite: " + str(ite) + "  - u1[-1]: " + str(u1[-1]))

        if (abs(u1[-1]-bv_at_x_final) < 0.001):
            break

        ite+=1
        
    
    fig, axes = plt.subplots(1, 2, figsize=(6, 6), sharex=True,sharey=True, squeeze=False)
    axes[0,0].set_title("u1")
    axes[0,0].plot(s,u1)
    axes[0,0].grid()
    
    axes[0,1].set_title("u2")
    axes[0,1].plot(s,u2)
    axes[0,1].grid()
    return (s,u1,u2)


def BSF_solver(f1, f2, x_initial= 0, x_final=1, h = 0.01, bv_at_x_initial = 0, bv_at_x_final= 1, total_iterations = 10, tolerance = 0.01):
    (s,u1,u2) = shooting_method(f1, f2, x_initial, x_final, h, bv_at_x_initial, bv_at_x_final, total_iterations, tolerance)
    
    def fx(x,u1,u2):
        return 
    
    
'''
# test

def f1(x,u1,u2):
    return u2
def f2(x,u1,u2):
    return (-np.exp(x*u1)*u2 - x*(u1**2))

sol = shooting_method(f1, f2, x_initial= 0, x_final=0.5, h = 0.1, bv_at_x_initial = 0, bv_at_x_final= 1, total_iterations = 5, tolerance = 0.01)

'''