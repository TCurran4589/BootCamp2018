__author__ = "Tom Curran"

import pandas as pd
import numpy as np
from scipy.linalg import norm
import scipy.linalg as la

#---------------------------------------------------------------------------#
'''
Problem 1. Write a function that accepts an m ⇥ n matrix A of rank n.
Use Algorithm 3.1 to compute the reduced QR decomposition of A.

Consider the following tips for implementing the algorithm.

• Use scipy.linalg.norm() to compute the norm of the vector in step 6.

• Note that steps 7 and 10 employ scalar multiplication or division,
while step 9 uses vector multiplication.

To test your function, generate test cases with NumPy’s np.random module.
Verify that R is upper triangular, Q is orthonormal, and QR = A.
You may also want to compare your results to SciPy’s QR factorization routine,
scpiy.linalg.qr().


'''
#---------------------------------------------------------------------------#
# Generate a random matrix and get its reduced QR decomposition via SciPy.
A = np.random.random((6,4))
Q,R = la.qr(A, mode = 'economic')

print(A.shape)
print(Q.shape)
print(R.shape)

# Verify that R is upper triangular, Q is orthonormal, and QR = A.
np.allclose(np.triu(R), R)
np.allclose(Q.T @ Q, np.identity(4))
np.allclose(Q @ R, A)

A2 = A.copy()

def modified_gramschmidt(A):
    m = np.shape(A)[0]
    n = np.shape(A)[1]

    q = np.zeros(A.shape)
    r = np.zeros((n,n))
    z = np.zeros(A.shape)

    for i in range(0,n):
        r[i,i] = la.norm(A[:,i])
        q[:,i] = A[:,i] / r[i,i]
        for j in range(0,n):
            r[i,j] = np.dot(q[:,i],A[:,j])
            A[:,j] = A[:,j] -( r[i,j] * q[:,i])

    return(q,r)

q2 ,r2 = modified_gramschmidt(A)
qr = np.matmul(q2, r2)

#---------------------------------------------------------------------------#
'''
Problem 2. Write a function that accepts an invertible matrix A.
Use the QR decomposition of A and (3.1) to calculate |det(A)|.

You may use your QR decomposition algorithm from Problem 1 or SciPy’s QR routine.

Can you implement this function in a single line?

(Hint: np.diag() and np.prod() may be useful.)

Check your answer against la.det(), which calculates the determinant.

'''

def determinant_calc(B):

    while B.shape[0] != B.shape[1]:
        raise ValueError("Please enter a square matrix7")


#---------------------------------------------------------------------------#
'''
Problem 3. Write a function that accepts an invertible n ⇥ n matrix A and a
vector b of length n. Use the QR decomposition to solve Ax = b in the following
steps:
1. Compute Q and R.
2. Calculate y = QTb.
3. Use back substitution to solve Rx = y for x.
'''
#---------------------------------------------------------------------------#


'''
Problem 4. Write a function that accepts as input a m⇥n matrix A of rank n.

Use Algorithm 3.2 to compute the full QR decomposition of A.

Consider the following implementation details.
• NumPy’s np.sign() is an easy way to implement the sign() operation in step 7.
 However, np.sign(0) returns 0, which will cause a problem in the rare case that
 u0 = 0 (which is possible if the top left entry of A is 0 to begin with).

 The following code defines a function that returns the sign of a single
 number, counting 0 as positive.
'''

'''
• In steps 9 and 10, the multiplication of u and (uTX) is an outer product (
xyT instead of the usual xTy). Use np.outer() instead of np.dot() to
handle this correctly.

Use NumPy and SciPy to generate test cases and validate your function.

'''
