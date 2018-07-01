import pandas as pd
import numpy as np
import scipy.linalg

# Read it in and compute the spectral raduis using the tools for working with eigenvalues in scipy.linalg.

m = np.loadtxt("matrix_data.txt")

pd.DataFrame(m)

'''

Test the claim in (LSR) iteratively, computing $\| X^i v \|^{1/i}$ for
successively larger values of $i$. See if the sequence so generated converges to $r(A)$.

'''

np.linalg.eig(m)
