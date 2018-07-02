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

#generate n random draws of X_t from N(y,s2) distribution (i.e. xi distribution)

random_ints = np.random.randint(50,200,5)

Xt = np.random.normal(mu, s, n)

#generate random shocks
xi_rand = norm.pdf(0,1,n)
#Update the draws from the using the rule: rho * X_t + b + sigma * xit+1
Xt_1 = (rho * Xt) + beta + (sigma * xi_rand)

kde_ar = kde(Xt_1)
kde_ar_est = kde_ar.estimator(x)
plt.plot(x, kde_ar_est)


def plot_random_n(n, i):
    xt2 = np.random.normal(mu, s, n)
    xi_rand2 = norm.pdf(0,1,n)
    Xt_1_2 = (rho * xt2) + beta + (sigma * xi_rand2)
    kde_ar2 = kde(xt2)
    kde_ar_est2 = kde_ar.estimator(x)

    subplot_num = int("22" + str(i))
    plt.subplot(subplot_num)
    plt.plot(x,kde_ar_est2 )
    plt.show()
[plot_random_n(n = random_ints[i], i = 1) for i in range(0, len(random_ints))]
for i in range(0, 5):
    x = "2" + "2" + str(i)
    print(x)



#plt.plot(x, norm.pdf(0,1,100))
plt.show()
