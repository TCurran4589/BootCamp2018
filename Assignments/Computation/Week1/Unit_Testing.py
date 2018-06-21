import pandas as pd
import numpy as np

def smallest_factor(n):
    if n == 1:
        return(1)
    for i in range(2, int(n**.5)):
        if n % i == 0:
            return(i)


smallest_factor(10)
