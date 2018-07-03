from scipy.stats import norm, beta
import numpy as np
import pandas as pd
from numba import jit
import matplotlib.pyplot as plt
class kde():

    def __init__(self, X, bandwidth = None):
        self.X = X
        self.n = len(X)

        if bandwidth is None:
            sigma = np.std(X)
            silverman_val = 1.06 * sigma * (len(X) ** (-.2))
            self.bandwidth = silverman_val
        else:
            self.bandwidth = bandwidth

    def estimator(self, x):
        est_vals = np.zeros(len(x))
        a = 1 / (self.bandwidth * self.n)

        for i in range(0, len(x)):
            total = 0
            for j in range(self.n):
                k = norm.pdf((x[i] - self.X[j]) / self.bandwidth)
                total = total + (a*k)
            est_vals[i] = total

        return(est_vals)



x_dist = np.linspace(0,1,100)
#--------------------------------
dist_1 = np.random.beta(2,2,100)
dist_2 = np.random.beta(2,5,100)
dist_3 = np.random.beta(.5,.5, 100)
#--------------------------------

kde1 = kde(dist_1)
plt.plot(x_dist, kde1.estimator(x_dist), label = "Estimated Probability")
plt.plot(x_dist, beta.pdf(x_dist, 2,2), label = "Actual Probabality")
plt.title(r"KDE for $\alpha$ = 2 and $\beta$ = 2 for x $\in$ [0,1]")
plt.ylabel("Density")
plt.xlabel("X Value [0,1]")
plt.show()


kde2 = kde(dist_2)
kde_est2 = kde2.estimator(x_dist)
plt.plot(x_dist, kde2.estimator(x_dist), label = "Estimated Probability")
plt.plot(x_dist, beta.pdf(x_dist, 2,5), label = "Actual Probabality")
plt.title(r"KDE for $\alpha$ = 2 and $\beta$ = 5 for x $\in$ [0,1]")
plt.ylabel("Density")
plt.xlabel("X Value [0,1]")
plt.show()


kde3 = kde(dist_3)
kde_est3 = kde3.estimator(x_dist)
plt.plot(x_dist, kde3.estimator(x_dist), label = "Estimated Probability")
plt.plot(x_dist, beta.pdf(x_dist, .5,.5), label = "Actual Probabality")
plt.title(r"KDE for $\alpha$ = .5 and $\beta$ = .5 for x $\in$ [0,1]")
plt.ylabel("Density")
plt.xlabel("X Value [0,1]")
plt.show()

###############################################################################
#
# Question #2
#
###############################################################################

n = 100
rho   = .9
beta  = 0.0
sigma = .1
mu    = -3
s     = .2

def new_n(mu, sigma, n):
    X_t = np.random.normal(mu, sigma, n)
    xi = norm.pdf(0,1, n)
    X_tp1 = (rho * X_t) + beta + (sigma * xi)
    kde_x_tp1 = kde(X_tp1)
    kde_estimator_tp1 = kde_x_tp1.estimator(x)
    return(kde_estimator_tp1)



#generate n random draws of X_t from N(y,s2) distribution (i.e. xi distribution)
X_t = np.random.normal(mu, sigma, n)
xi = norm.pdf(0,1,n)
X_tp1 = (rho * X_t) + beta + (sigma * xi)
x = np.linspace(-4,-1,n)

kde_x_tp1 = kde(X_tp1)
kde_estimator_tp1 = kde_x_tp1.estimator(x)
x_theoretical = norm.pdf(x, mu, s)

plt.plot(x,kde_estimator_tp1, label = r"KDE for $X_{t+1}$, n = 100")
plt.plot(x, x_theoretical, label = r"Theoretical Distribution")
plt.plot(x,new_n(mu = -3, sigma = .1, n = 200), label = r"KDE for n = 200" )
plt.plot(x,new_n(mu = -3, sigma = .1, n = 150), label = r"KDE for n = 150" )
plt.plot(x,new_n(mu = -3, sigma = .1, n = 50), label = r"KDE for n = 50" )
plt.plot(x,new_n(mu = -3, sigma = .1, n = 500), label = r"KDE for n = 500" )
plt.plot(x,new_n(mu = -3, sigma = .1, n = 1000), label = r"KDE for n = 1000" )
plt.title("Kernal Density Estimation Simulation" )
plt.ylabel("Density")
plt.legend()
plt.show()
