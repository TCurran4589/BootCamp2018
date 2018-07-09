import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Question #1:

from pydataset import data
trees = data("trees")
trees.info()
plt.figure(figsize = (7,15))

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

#Data set #2
bdr = data("birthdeathrates")
bdr.info()

bdr.head()
import seaborn as sns

regplot = sns.lmplot(x = "birth",y = "death", data = bdr, fit_reg = True)

#Birth Death Rates
p = sns.barplot(x = bdr.index, y = bdr.birth, data = bdr)
plt.title("Births by Country")
p.set_xticklabels(bdr.index, rotation = 90)
plt.show()

p = sns.barplot(x = bdr.index, y = bdr.death, data = bdr)
plt.title("Deaths by Country")
p.set_xticklabels(bdr.index, rotation = 90)
plt.show()
