import quantecon as qe
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mpl_toolkits.mplot3d import Axes3D


###############################################################################
#
# Question 1
#

'''
Compute and plot the stationary distribution of the matrix using one of the
methods in quantecon's MarkovChain object, combined with matplotlib.
'''
###############################################################################

P = [[0.222, 0.222, 0.215, 0.187, 0.081, 0.038, 0.029, 0.006],
     [0.221, 0.220, 0.215, 0.188, 0.082, 0.039, 0.029, 0.006],
     [0.207, 0.209, 0.210, 0.194, 0.090, 0.046, 0.036, 0.008],
     [0.198, 0.201, 0.207, 0.198, 0.095, 0.052, 0.040, 0.009],
     [0.175, 0.178, 0.197, 0.207, 0.110, 0.067, 0.054, 0.012],
     [0.182, 0.184, 0.200, 0.205, 0.106, 0.062, 0.050, 0.011],
     [0.123, 0.125, 0.166, 0.216, 0.141, 0.114, 0.094, 0.021],
     [0.084, 0.084, 0.142, 0.228, 0.170, 0.143, 0.121, 0.028]]

mc = qe.MarkovChain(P, ("1","2","3","4","5","6","7","8"))
stationary_dist_p = mc.stationary_distributions
print(stationary_dist_p)
plt.plot(list(range(0, len(P[0]))),stationary_dist_p[0], color = 'r')
plt.scatter(list(range(0, len(P[0]))),stationary_dist_p[0])
plt.title(r"Stationary Distribution of $P$")
plt.ylabel("Probability")
plt.xlabel("Period")
plt.show()



###############################################################################
#
# Question 1
#

'''

Exercise 2
This Markov chain is asymptotically stationary and ergodic, which means that,
for any sample path $\{X_t\}$ generated according to $P$, we have

$$ \lim_{n \to \infty} \frac{1}{n} \sum_{t=1}^n \mathbb 1\{X_t = j\} = \psi(j) $$
where $\psi$ is the stationary distribution and $j$ is an integer between 0 and
7 (the set of possible states).

Use this fact to compute an approximation to the stationary distribution $\psi$.
Confirm visually that your result is similar to the stationary distribution you
computed in exercise 1.

You can make use of the simulate method in MarkovChain.
'''
###############################################################################

simulation = qe.MarkovChain(P).simulate_indices(ts_length = 1000, random_state = 1234)
'''
state = np.zeros(len(P[0]))

for i in range(0, len(state)):
    states = simulation == i
    state[i] = np.sum(states)
'''

state_count = pd.Series(simulation).value_counts()/1000

plt.plot(list(range(0, len(P[0]))), state_count, color = 'g', label = 'Simulation')
plt.scatter(list(range(0, len(P[0]))),state_count, color = 'g')
plt.plot(list(range(0, len(P[0]))),stationary_dist_p[0],  ':',color = 'r', label = 'Actual')
plt.scatter(list(range(0, len(P[0]))),stationary_dist_p[0],color = 'r')
plt.title(r"Simulation vs Actual Stationary Distributions of $P$")
plt.ylabel("Probability")
plt.xlabel("Period")
plt.legend()
plt.show()


###############################################################################
#
# Question 3
#

'''
Exercise 3
Ergodicity also implies that, if we simulate a large number of paths and then
look at the cross section at some $T$, where $T$ is suitably large, then the
empirical distribution should be close to the stationary distribution.

Confirm this by simulation and visual inspection, as above.

(In this context, the empirical distribution of a sample is the fraction of
observations that take value $j$ for each $j$ in $0, \ldots, 7$.)
'''
################################################################################

#simulate a large number of paths:
paths = np.zeros(1000)

#T is suitably large
T = 1000

for i in range(len(paths)):
    T_sim = qe.MarkovChain(P).simulate_indices(ts_length = T)
    paths[i] = T_sim[-1]

counts = pd.Series(paths).value_counts()/1000


plt.figure(figsize = (10,10))
plt.plot(list(range(0, len(P[0]))), counts, '--', color = 'b', label = 'Ex #3')
plt.scatter(list(range(0, len(P[0]))),counts, color = 'b')
plt.plot(list(range(0, len(P[0]))), state_count,':', color = 'g', label = 'Ex #2')
plt.scatter(list(range(0, len(P[0]))),state_count, color = 'g')
plt.plot(list(range(0, len(P[0]))),stationary_dist_p[0],  color = 'r', label = 'Ex #1')
plt.scatter(list(range(0, len(P[0]))),stationary_dist_p[0],color = 'r')
plt.title(r"Simulation vs Actual Stationary Distributions of $P$")
plt.ylabel("Probability")
plt.xlabel("Period")
plt.legend()
plt.show()
