import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Question #1:

from pydataset import data
trees = data("trees")
trees.info()
plt.figure(figsize = (7,12))

plt.subplot(311)
plt.scatter(x = trees.Girth, y = trees.Height)
plt.title("Tree Girth vs Height")
plt.xlabel("Girth")
plt.ylabel("Height")

plt.subplot(312)
plt.scatter(x = trees.Volume, y = trees.Height)
plt.title("Tree Volume vs Height")
plt.xlabel("Volume")
plt.ylabel("Height")

plt.subplot(313)
plt.scatter(x = trees.Volume, y = trees.Girth)
plt.title("Tree Volume vs Girth")
plt.xlabel("Volume")
plt.ylabel("Girth")

plt.show()

'''

it appeasr that of the characteristics measured on the data set, that girth and Volume
are the most highly correlated. Which makes sense since girth, or width, is a characteristic
of volume

'''

#Data set #2
