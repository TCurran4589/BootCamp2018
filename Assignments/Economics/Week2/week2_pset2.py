import scipy.stats
import numpy as np
import pandas as pd
from numba import jit
import matplotlib.pyplot as plt
class kde():

    def __init__(self, X, bandwidth = None):
        self.X = X
        self.n = len(X)

        if(bandwidth is None):
            self.bandwidth = s_rule(X)
        else:
            self.bandwidth = bandwidth

    def s_rule(X):
        sigma = np.std(X)
        silverman_val = 1.06 * sigma * (len(X) ** (-.2))
        return(silvernman_val)

    def estimator(self, x):
        est_vals = np.zeros(len(x))
        a = 1 / (self.bandwidth * self.n)

        for i in range(0, len(x)):
            total = 0
            for j in range(self.n):
                k = scipy.stats.norm.pdf((x[i] - self.X[j]) / self.bandwidth)
                total = total + (a*k)
            est_vals[i] = total

        return(est_vals)



x_dist = np.linspace(0,1,100)

dist_1 = np.random.beta(2,2,100)
dist_2 = np.random.beta(2,5,100)
dist_3 = np.random.beta(.5,.5, 100)

kde1 = kde(dist_1)
kde1.estimator(x_dist)
plt.plot(x_dist, kde1.estimator(x_dist))
plt.plot(x_dist, kde1.estimator(x_dist), label = "Estimated Probability")
plt.plot(x_dist, scipy.stats.beta.pdf(x_dist, 2,2), label = "Actual Probabality")
plt.title(r"KDE for $\alpha$ = 2 and $\beta$ = 2 for x $\in$ [0,1]")
plt.ylabel("Density")
plt.xlabel("X Value [0,1]")
plt.show()


kde2 = kde(dist_2)
kde_est2 = kde2.estimator(x_dist)
kde3 = kde(dist_3)
kde_est3 = kde3.estimator(x_dist)
