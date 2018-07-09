import pandas as pd
import numpy as np
import time
import scipy.optimize as opt

#------------------------------------------------------------------------------#
#2.25
def wage(alpha, A, capital, labor)            :
    wages = np.zeros([len(labor)])
    for i in range(0, len(labor))             :
        wages[i]= (1-alpha) * A * (np.power((capital/labor[i]), alpha))
    return(wages)
#------------------------------------------------------------------------------#
#2.26
def interest(alpha, A, labor, capital, delta) :
    interest = np.zeros([len(labor)])
    for i in range(0, len(labor))             :
        interest[i] = alpha * A * np.power((labor[i]/capital), (1-alpha)) - delta
    return(interest)
#------------------------------------------------------------------------------#

def capital(bvec_guess, b0 = 0)               :
    k = b0 + bvec_guess.sum()
    return(k)

#------------------------------------------------------------------------------#

def labor_supply(n_periods = 3)               :
    labor = np.ones(n_periods)
    labor [-1] = .2
    return(labor)

#------------------------------------------------------------------------------#

def production(A, capital, alpha, labor)      :
    p = A * (capital ** alpha) * (labor ** (1-alpha))
    return(p)

#------------------------------------------------------------------------------#

def crra(sigma, c)                            :
    u = (np.power(c, (1-sigma)) - 1 )/ 1-sigma

    u_prime = np.power(c, (-1*sigma))

    u_dbprime = -sigma * np.power(x, (-sigma - 1))
    return(u, u_prime, u_dbprime)

#------------------------------------------------------------------------------#

def consumptions(wage, labor_n, interest, savings):
    c = np.zeros([len(labor_n)])
    for i in range(0,len(labor_n))             :

        for j in range(1, len(labor_n)):
            if(i == len(labor_n)):
                c_p = wage[i] * labor_n[i] + ((1 + interest[i])*savings[i])
                c[i] = c_p
            else:
                c_p = wage[i] * labor_n[i] + ((1 + interest[i])*savings[i]) - savings[j]
                c[i] = c_p
    return(c)
#------------------------------------------------------------------------------#

def feasible(f_params,bvec_guess):

    '''
    f_params   : tuple of nvec, A, alpha, delta
    bvec_guess : array; guess for the steady statesavings vector

    K_cnstr    : singleton Bolean that equals True if K <= 0 for given f_params and bvec_guess

    c_cnstr    : length 3 bootlean vector where the s^th element equals true if c_s <= 0 given f_params

    b_cnstr    : length 2 boolean vector that denotes which element of bvec guess is likely responsible
    for any of the consumption nonnegativity constraint violations identified by c_cnstr

    * if the first element of c_cnstr is True, then the first element of b_cnstr is true
    * if the scond element of c_cnstr is True than both element of b_cnstr is true
    * if the last element of c_cnstr is True than the last elmenet of b_cnstr is true

    nvec       : labor supply. If s = 1 or 2, n = 1 -- if n = 3, s = .2



    * f_params :

            * nvec = units of labor provided over n periods.
                      n = 1 for all periods except for last, in which n = .2

            * A =

            * alpha =

            * delta =

    '''
    #--------------------------------------------------------------------------#
    #Declare problem paramters
    n_periods, sigma, A, alpha, delta, beta = f_params
    b0 = bvec_guess[0]
    k = capital(bvec_guess, b0)
    l = labor_supply(n_periods)
    w = wage(alpha, A, k, l)
    r = interest(alpha, A, l, k, delta)

    p = production(A, k, alpha, l)
    c = consumptions(w,l, r, bvec_guess)
    #--------------------------------------------------------------------------#

    #initializing emply constraint check

    b_cnstr = np.zeros(2)
    c_cnstr = np.zeros(3)

    #--------------------------------------------------------------------------#
    #c constraint is 3 boolen vector
    #wage, labor_n, interest, savings_p, savings_tp1

    #Determine capital constraint
    if k <= 0                                     :
        k_cnstr = True
    else                                          :
        k_cnstr = False


    #consumption constraint                       : where c >= 0 for all periods and ages
    #If value is True, than the constrinat is met. If the value at index i is False
    # than the constraint is not met.
    for j in range(0, len(c))                     :
        if c[j] >= 0                              :
            c_cnstr[j] = True
        else                                      :
            c_cnstr[j] = False

    #Determine savings (b) constraint
    #True == constraint met
    #False = constraint not met
    #* if the first element of c_cnstr is True, then the first element of b_cnstr is true
    #* if the scond element of c_cnstr is True than both element of b_cnstr is true
    #* if the last element of c_cnstr is True than the last elmenet of b_cnstr is true
    if c_cnstr[0] == True                         :
        b_cnstr[0] = True

    if c_cnstr[1] == True                         :
        b_cnstr = np.array([True, True])

    if c_cnstr[-1] == True                        :
        b_cnstr[-1] = True

    properties = {
        'savings': bvec_guess,
        'capital': k,
        'labor': l,
        'wages': w,
        'interest': r,
        'production': p,
        'consumption': c
        }
    return(k_cnstr, b_cnstr, c_cnstr, properties)

#------------------------------------------------------------------------------#
# Initial Parameters
#------------------------------------------------------------------------------#
sigma = 3
A = 1
alpha = .35
delta = .6415
beta = .442
n_periods = 3
laborSupply = labor_supply(n_periods)

f_params = (n_periods, sigma, A, alpha, delta, beta)

#------------------------------------------------------------------------------#
'''
1.a                                               :
Which, if any, of the constraints is violated if you choose an initial guess
for steady-state savings of bvec guess = np.array([1.0, 1.2])?
'''

bvec_guess = np.array([0,1.0,1.2])
k_cnstr1, b_cnstr1, c_cnstr1,properties1 = feasible(f_params, bvec_guess)
print("#------------------------------------------------------------------------------#")
print("bvec_guess ={}".format(bvec_guess))
print("K constraing: {}".format(k_cnstr1))
print("B constraint: {}".format(b_cnstr1))
print("C constraint: {}".format(c_cnstr1))
print('We can see that the consumptions constriant (c >= 0) does not hold because the consumption in the last period is negative')
#---------------------------#------------------------------------------------------------------------------#
'''
1.b
Which, if any, of the constraints is violated if you choose an initial guess
for steady-state savings of bvec guess = np.array([0.06, -0.001])?
'''

bvec_guess = np.array([0.0,0.06,-0.001])
k_cnstr2, b_cnstr2, c_cnstr2, properties2 = feasible(f_params, bvec_guess)
print("#------------------------------------------------------------------------------#")
print("bvec_guess = {}".format(bvec_guess))
print("K constraing: {}".format(k_cnstr2))
print("B constraint: {}".format(b_cnstr2))
print("C constraint: {}".format(c_cnstr2))
print("We can see here that all constraints are met")
#------------------------------------------------------------------------------#
'''
1.b
Which, if any, of the constraints is violated if you choose an initial guess
for steady-state savings of bvec guess = np.array([0.1, 0.1])?
'''

bvec_guess = np.array([0.0,0.1,0.1])
k_cnstr3, b_cnstr3, c_cnstr3, properties3 = feasible(f_params, bvec_guess)
print("#------------------------------------------------------------------------------#")
print("bvec_guess = {}".format(bvec_guess))
print("K constraing: {}".format(k_cnstr3))
print("B constraint: {}".format(b_cnstr3))
print("C constraint: {}".format(c_cnstr3))
print("No constraints are violated")

properties1
