import pandas as pd
import numpy as np
################################################################################
#
# Question 1
#
################################################################################
indexVals = list(range(0,52,2))
x = pd.Series(index = indexVals)

def values(x):
    if(x % 3 == 0):
        val = 0
    else:
        val = x**2 -1
    return(val)

x.index
for i in range(0, len(x)):
    x[i] = values(x.index[i])
    print(x.index[i], values(x.index[i]))
