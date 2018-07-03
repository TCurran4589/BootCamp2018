import pandas as pd
import numpy as np
import scipy.linalg as sc
import matplotlib.pyplot as plt
from numba import jit

# Read it in and compute the spectral raduis using the tools for working with eigenvalues in scipy.linalg.

X = np.loadtxt("matrix_data.txt")

'''
Test the claim in (LSR) iteratively, computing $\| X^i v \|^{1/i}$ for
successively larger values of $i$. See if the sequence so generated converges to $r(A)$.
'''

spectral_radius1 = lamda = np.abs(sc.eigvalsh(X)).max()
max_eig = np.linalg.eigvals(X).max()

'''

if X  has all positive entries and v is strictly positive n * 1 vector
||X^i * v||^(1/i) = rho(X) (Spectral Radius)

X = any n x n matrix
lambda = spectral radius of X
v = any strictly positive n * 1 vector
spectral radius - maximum absolute value of all X's eigen values
'''

def gelfand(X, i):
    a = np.linalg.matrix_power(X, i)
    v = X[:,1]
    b = np.matmul(a,v)
    c = np.linalg.norm(b)
    d = np.power(c, (1/i))
    return(d)

%time

i = 1
gelfand_vals = []

while gelfand(X, i) < max_eig:
    val = gelfand(X, i)
    gelfand_vals.append(val)
    i += 1
else:
    gelfand_vals.append(val)
    matching_index = i
    print("The Local Spectral Radius Theorem Converges at iteration {}".format(i))

plt.figure(figsize = (10,10))
plt.plot(gelfand_vals, label = "Generated Values")
plt.scatter(x = matching_index, y = max_eig, color = "green", marker = "*", label = "Eigen Value")
plt.legend()
plt.title("Exercise 1")
plt.xlabel("Iterations")
plt.ylabel("Generated Value")
plt.show()

###############################################################################
# Excercise #2
'''
Recall that the quadratic map generates time series of the form

xt+1=4xt(1−xt)

for some given  x0x0 , and that these trajectories are chaotic.

This means that different initial conditions generate seemingly very different outcomes.

Nevertheless, the regions of the state space where these trajectories spend most of their time are in fact typically invariant to the initial condition.

Illustrate this by generating 100 histograms of time series generated from the quadratic map, with  x0x0  drawn independently from the uniform distribution on  (0,1)(0,1) .

Do they all look alike?

Try to make your code efficient.

'''
###############################################################################

#Draws a random set of x's between 0-1
x_0 = np.random.uniform(0,1, 100)

#quadratic map: 4 x_i * (1 - x_i) = x_i+1
quadMap = []
for i in range(0, len(x_0)):
    x = x_0[i]
    x_t = 4*x*(1-x)
    quadMap.append(x_t)

plt.hist(quadMap)


###############################################################################
# Excercise #2
'''
In the lecture it was claim that, if $(\mathbb X, g)$ is a dynamical system,
$g$ is continuous at $\hat x \in \mathbb X$ and, for some $x \in \mathbb X$,
$g^t(x) \to \hat x$, then $\hat x$ is a steady state of $(\mathbb X, g)$.

Prove this.

'''
###############################################################################
