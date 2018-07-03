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
plt.text(r"it appears that of the characteristics measured on the data set \n \
         that girth and Volume are the most highly correlated. Which makes sense since \n \
         girth, or width, is a characteristics of volume", fontsize = 15)

plt.show()

#Data set #2
bdr = data("birthdeathrates")
bdr.info()
