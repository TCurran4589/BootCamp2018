import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy.optimize import fminbound
from scipy import interpolate
import pandas as pd
import ar1_approx as ar1
'''

Question 2.4 using Value Function Iteration (VFI)

'''

#Step 1 - Set parameter Values:

gamma   = .5 # coefficient of relative risk aversion

beta    = .96 # Discount Factor

delta   = .05 # Rate of Physical Depreciation

alpha   = .4  # curvature of production Function

sigma_z = .2  # Standard Deviation of productivity shocks

mu = 0

rho = 0
'''
------------------------------------------------------------------------
Create Grid for State Space
------------------------------------------------------------------------
lb        = scalar, lower bound of cake grid
ub        = scalar, upper bound of cake grid
size_w    = integer, number of grid points in cake state space
w_grid    = vector, size_w x 1 vector of cake grid points
------------------------------------------------------------------------
'''

lb = 10
ub = 15

size_c = 50
size_z = 50

c_grid = np.linspace(lb, ub, size_c)

z_grid, pi = ar1.addacooper(size_z, mu, rho, sigma_z)
z_grid = np.exp(z_grid)
prob_m = np.transpose(pi)
'''
------------------------------------------------------------------------
Create grid of current utility values
------------------------------------------------------------------------
C        = matrix, current consumption (c=w-w')
U        = matrix, current period utility value for all possible
           choices of w and w' (rows are w, columns w')
------------------------------------------------------------------------
'''
C = np.zeros((size_c, size_c,size_c))
for i in range(size_c):
    for j in range(size_c):
        for k in range(size_c):
            C[i, j, k] = z_grid[k] * c_grid[i] ** alpha + (1-delta) * c_grid[i] - c_grid[j]




C[C<=0] = 1e-15


if gamma == 1:
    U = np.log(C)
else:
    U = (C ** (1 - gamma)) / (1 - gamma)


U[C<0] = -9999999


'''
------------------------------------------------------------------------
Value Function Iteration
------------------------------------------------------------------------
VFtol     = scalar, tolerance required for value function to converge
VFdist    = scalar, distance between last two value functions
VFmaxiter = integer, maximum number of iterations for value function
V         = vector, the value functions at each iteration
Vmat      = matrix, the value for each possible combination of w and w'
Vstore    = matrix, stores V at each iteration
VFiter    = integer, current iteration number
TV        = vector, the value function after applying the Bellman operator
PF        = vector, indicies of choices of w' for all w
VF        = vector, the "true" value function
------------------------------------------------------------------------
'''
VFtol = 1e-8
VFdist = 7.0
VFmaxiter = 3000
V = np.zeros((size_c,size_c)) # initial guess at value function
Vmat = np.zeros((size_c, size_c, size_z)) # initialize Vmat matrix
Vstore = np.zeros((size_c,size_c, VFmaxiter)) #initialize Vstore array
VFiter = 1
while VFdist > VFtol and VFiter < VFmaxiter:
    print("Interation #", VFiter, "Distance:", VFdist)
    for i in range(size_c):
        for j in range(size_c):
            for k in range(size_z):
                E_V = 0
                for q in range(0,size_z-1):
                    E_V += prob_m[k, q] * V[j, q]
                Vmat[i, j, k] = U[i, j, k] + beta * E_V


    Vstore[:,:, VFiter] = V.reshape(size_c,size_z,) # store value function at each iteration for graphing later
    TV = Vmat.max(1) # apply max operator to Vmat (to get V(w))
    PF = np.argmax(Vmat, axis=1)
    VFdist = (np.absolute(V - TV)).max()  # check distance
    V = TV
    VFiter = VFiter + 1

if VFiter < VFmaxiter:
    print('Value function converged after this many iterations:', VFiter)
else:
    print('Value function did not converge')

VF = V # solution to the functional equation

###############################################################################
# 4.2 Plot the Value function
###############################################################################
# Plot value function at several iterations# Plot v
plt.figure(figsize = (15,15))
fig, ax = plt.subplots()
ax.plot(c_grid, VF[:,0],  label="First Iteration")
ax.plot(c_grid, VF[:,10], label="10th Iteration")
ax.plot(c_grid, VF[:,20], label="20th Iteration")
ax.plot(c_grid, VF[:,30], label="30th Iteration")
ax.plot(c_grid, VF[:,40], label="40th Iteration")

# Now add the legend with some customizations.
legend = ax.legend(loc='lower right', shadow=False)
# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize('large')
for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width
plt.xlabel('Size of Cake')
plt.ylabel('Value Function')
plt.title('Value Function')
plt.show()


###############################################################################
# 4.3 Plot the Policy function for Choice of consumption
###############################################################################

optC = c_grid[PF]

plt.figure(figsize = (15,15))
fig, ax = plt.subplots()
ax.plot(c_grid[:], optC[:][18], label='Consumption')
# Now add the legend with some customizations.
legend = ax.legend(loc='lower right', shadow=False)
# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize('large')
for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width

plt.xlabel('Size of Cake')
plt.ylabel('Optimal Consumption')
plt.title('Policy Function, consumption - deterministic cake eating')
plt.show()

###############################################################################
# 4.4 Plot the policy function for the choice of capital next period
###############################################################################


###############################################################################
# Question #3
###############################################################################

gamma   = .5 # coefficient of relative risk aversion

beta    = .96 # Discount Factor

delta   = .05 # Rate of Physical Depreciation

alpha   = .4  # curvature of production Function

sigma_z = .2  # Standard Deviation of productivity shocks

mu = 0

rho = .8


'''
 --------------------------------------------------------------------------------
Create Grid for State Space
------------------------------------------------------------------------
lb_w      = scalar, lower bound of cake grid
ub_w      = scalar, upper bound of cake grid
size_w    = integer, number of grid points in cake state space
w_grid    = vector, size_w x 1 vector of cake grid points
------------------------------------------------------------------------
'''

lb_w = 10
ub_w = 15
size_w = 20
sigma_v = .1
size_z = 20  # Number of grid points
w_grid = np.linspace(lb_w, ub_w, size_w)

z_grid, pi = ar1.addacooper(size_z, mu, rho, sigma_v)
z_grid = np.exp(z_grid)
prob_m = np.transpose(pi)


'''
------------------------------------------------------------------------
Create grid of current utility values
------------------------------------------------------------------------
C        = matrix, current consumption (c=w-w')
U        = matrix, current period utility value for all possible
           choices of w and w' (rows are w, columns w')
------------------------------------------------------------------------
'''
C = np.zeros((size_w, size_w, size_w))
for i in range(size_w):
    for j in range(size_w):
        for k in range(size_w):
            C[i, j, k] = z_grid[k] - w_grid[i] ** alpha + (1-delta) * w_grid[i] - w_grid[j]
C[C<=0] = 1e-15

if gamma == 1:
    U = np.log(C)
else:
    U = (C ** (1 - gamma))

'''
------------------------------------------------------------------------
Value Function Iteration
------------------------------------------------------------------------
VFtol       = scalar, tolerance required for value function to converge
VFdist      = scalar, distance between last two value functions
VFmaxiter   = integer, maximum number of iterations for value function
V           = matrix, the value functions at each iteration
TV          = matrix, the value function after applying the Bellman operator
PF_discrete = matrix, matrix of policy function: eat=1, not eat=0
Vstore      = array, stores V at each iteration
VFiter      = integer, current iteration number
EV          = scalar, expected value function for a given state
U_eat       = matrix, utility from eating cake now
Vwait       = matrix, value of waiting to eat the cake
VF          = vector, the "true" value function
------------------------------------------------------------------------
'''
VFtol = 1e-8
VFdist = 7.0
VFmaxiter = 3000
V = np.zeros((size_w, size_w))
TV = np.zeros((size_w, size_w))
PF_discrete = np.zeros((size_w, size_w))
Vmat = np.zeros((size_w, size_w, size_z))
Vstore = np.zeros((size_w, size_w, VFmaxiter))
VFiter = 1
while VFdist > VFtol and VFiter < VFmaxiter:
    print("Interation #", VFiter, "Distance:", VFdist)
    for i in range(size_w):
        for j in range(size_w):
            for k in range(size_z):
                E_V = 0
                for q in range(size_z):
                    E_V += prob_m[k, q]* V[j, q]
                Vmat[i, j, k] = U[i, j, k] + beta * E_V
    TV = Vmat.max(1)
    Vstore[:, :, VFiter] = V.reshape(size_w, size_z,)
    PF = np.argmax(Vmat, axis=1)
    VFdist = (np.absolute(V - TV)).max()
    V = TV
    VFiter += 1
if VFiter < VFmaxiter:
    print('Value function converged after this many iterations:', VFiter)
else:
    print('Value function did not converge')


VF = V # solution to the functional equation

print(VF)

###############################################################################
# 2.1 Plot the value function for at least 3 values of the productivity shock
###############################################################################
plt.figure(figsize = (15,15))
fig, ax = plt.subplots()
ax.plot(w_grid[1:], VF[1:,0],  label="First Iteration")
ax.plot(w_grid[1:], VF[1:,1], label="10th Iteration")
ax.plot(w_grid[1:], VF[1:,2], label="20th Iteration")
legend = ax.legend(loc='lower right', shadow=False)
plt.show()

###############################################################################
# 2.2 Plot the policy function for the choice of consumption for at least 3 values
# of the productivity shock.
###############################################################################
optK = w_grid[VF]
plt.figure(figsize = (15,15))
fig, ax = plt.subplots()
ax.plot(w_grid[1:], optK[:][1], label="First Iteration")
ax.plot(w_grid[1:], optK[:][2], label="First Iteration")
ax.plot(w_grid[1:], optK[:][3], label="First Iteration")
#ax.plot(w_grid[1:], VF[1:,1], label="10th Iteration")
#ax.plot(w_grid[1:], VF[1:,2], label="20th Iteration")
legend = ax.legend(loc='lower right', shadow=False)
plt.show()

###############################################################################
# 2.3 Plot the policy function for the choice of capital next period for at least 3
#values of the productivity shock.
###############################################################################

###############################################################################
# 2.3 Plot the policy function for the choice of capital next period for at least 3
#values of the productivity shock.
###############################################################################
