import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''

Problem 1. There are two main ways to perform matrix multiplication in NumPy: with
NumPy’s dot() function (np.dot(A, B)), or with the @ operator (A @ B). Write a function
that defines the following matrices as NumPy arrays.

A =[[3, −1, 4],[1, 5, −9]]

B = [[2, 6, −5, 3],[5, −8, 9, 7],[9, −3, −2, −3]]

Return the matrix product AB.

For examples of array initialization and matrix multiplication, use object introspection in
IPython to look up the documentation for np.ndarray, np.array() and np.dot().

'''

A = np.array([[3,-1,4],
              [1,5,-9]])

B = np.array([[2,6,-5,3],
              [5,-8,9,7],
              [9,-3,-2,-3]])

ab_prod = np.matmul(A,B)

print(ab_prod)

'''
Problem 2. Write a function that defines the following matrix as a NumPy array.
A =
3 1 4
1 5 9
−5 3 1
Return the matrix −A3 + 9A2 − 15A.
In this context, A2 = AA (the matrix product, not the component-wise square). The
somewhat surprising result is a demonstration of the Cayley-Hamilton theorem
'''

a2 = np.array([[3,1,4],[1,5,9],[-5,3,1]])

ans = (-1 * a2 * 3) + (9*a2*2) -(15*a2)

print(ans)

'''

Problem 3. Write a function that defines the following matrices as NumPy arrays using the
functions presented in this section, not np.array(). Calculate the matrix product ABA.
Change the data type of the resulting matrix to np.int64, then return it.

'''

def problem3(cols, rows, dtype):

    print("Matrix A: ")
    print("--------------------------------------")
    Ia  = np.ones((cols,rows), dtype = dtype)
    A3 = np.triu(Ia)
    print(A3)
    print()

    Ib = np.ones((7,7), dtype = "int64")

    #Find the indces of the bottom triangles of matrix Ib
    bottom = np.tril_indices(7)

    #Find the indices of the top triangle of the matrix
    top = np.triu_indices(7)

    #Note that what ever the last triangle indexed will overtake the diagnal values
    Ib[top] = 5
    Ib[bottom] = -1
    print("Matrix B: ")
    print("--------------------------------------")
    print(Ib)
    print()

    aba = np.matmul(Ia,Ib)
    aba = np.matmul(aba,Ia)
    print("Product of A*B*A: ")
    print("--------------------------------------")
    print(Ib)

problem3(7,7,"int64")

'''

Write a function that accepts a single array as input. Make a copy of the array,
then use fancy indexing to set all negative entries of the copy to 0. Return the copy.

'''
def problem4(x):
    mask = x < 0
    x[mask] = 0
    return(x)

x = np.array([-1, 3,5, -10, 6])

problem4(x)


a5 = np.arange(6).reshape(2,3)

b5 = np.zeros((3,3), dtype = "int64")
b5_bottom = np.tril_indices(3)
b5[b5_bottom] = 3

c5 = np.zeros((3,3))
np.fill_diagonal(c5, -2)

def problem5(a,b,c):
    a = a.T
    zero_m = np.zeros(a.shape)
    I = np.identity(3, dtype = "int")
    matrix_row1 = [zero_m, a, I]
    matrix_row2 = [a, zero_m, zero_m]
    matrix_row3 = [b,zero_m, c]
    matrix = [matrix_row1, matrix_row2, matrix_row3]
    return(matrix)

problem5(a5,b5,c5)

'''
Problem 6. A matrix is called row-stochastica

if its rows each sum to 1. Stochastic matrices are fundamentally important for finite discrete random processes and some machine learning
algorithms.

Write a function than accepts a matrix (as a 2-D array). Divide each row of the matrix by
the row sum and return the new row-stochastic matrix. Use array broadcasting and the axis argument instead of a loop.

Similarly, a matrix is called column-stochastic if its columns each sum to 1.

'''

def problem6(x):
    row_sums = x.sum(axis = 1, keepdims = True)
    new_x = x / row_sums
    print(new_x)

x6 = np.arange(6).reshape(2,3)

print(problem6(x6))

'''

Problem 7

FINISH

'''

grid = np.load("grid.npy")

np.max(grid[:,:-3] * grid[:,1:-2] * grid[:,2:-1] * grid[:,3:])
