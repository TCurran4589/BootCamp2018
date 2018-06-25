import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy.optimize import fminbound
from scipy import interpolate
import pandas as pd

'''

Question 2.4 using Value Function Iteration (VFI)

'''

#Step 1 - Set parameter Values:

gamma   = .05 # coefficient of relative risk aversion

beta    = .96 # Discount Factor

delta   = .05 # Rate of Physical Depreciation

alpha   = .4  # curvature of production Function

sigma_z = .2  # Standard Deviation of productivity shocks

#Step 2 - Create Grid Space:

'''
------------------------------------------------------------------------
Create Grid for State Space
------------------------------------------------------------------------
lb_w      = scalar, lower bound of cake grid
ub_w      = scalar, upper bound of cake grid
size_w    = integer, number of grid points in cake state space
w_grid    = vector, size_w x 1 vector of cake grid points
------------------------------------------------------------------------
'''

lb_w = 1 #sells at least 1 barrel of oil
ub_w = 500 #at most sells 500 barrels of Neoclassical
size_b = 200 # number of grid points
b_grid = np.linspace(lb_w, ub_w, size_b)

'''
------------------------------------------------------------------------
Create grid of current utility values
------------------------------------------------------------------------
C        = matrix, current consumption (c=w-w')
U        = matrix, current period utility value for all possible
           choices of w and w' (rows are w, columns w')
------------------------------------------------------------------------
'''

C = np.zeros((200, 200))

for i in range(size_b):
    for j in range(size_b):
        C[i,j] = b_grid[i] - b_grid[j]

C[C<=0] = 1e-15
