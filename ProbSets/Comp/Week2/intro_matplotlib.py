import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###############################################################################
# Question 1
###############################################################################

n = np.random.normal(size = (2,3))
print(n)
row_averages = np.mean(n, axis=1)

def problem1(n):
    n = np.random.normal(size = (n,n))
    row_averages = np.mean(n, axis=1)
    variance = np.var(row_averages)
    return(variance)

problem1_array = np.zeros(10)

for i in range(0,10):
    for j in range(100,1001,100):
        problem1_array[i] = problem1(j)
print(problem1_array)

plt.plot(problem1_array)
plt.show()

###############################################################################
# Question 2
###############################################################################

x = np.linspace(-2*np.pi, 2*np.pi)
sin = np.sin(x)
tan = np.tan(x)
cos = np.cos(x)

plt.ion()
plt.plot(x,sin)
plt.plot(x,tan, color = "r")
plt.plot(x, cos, color = "g")
plt.show()

###############################################################################
# Question 3
###############################################################################

x = np.linspace(-2,6)
print(x)

def p3(x):
    y1 = []
    y2 = []
    for i in range(0, len(x)):
        if x[i]<1:
            y = 1 / ( x[i] - 1)
            y1.append(y)
        elif x[i] > 1:
            y = 1 / (x[i] - 1)
            y2.append(y)
    return(y1, y2)

y1, y2 = p3(x)
plt.plot(x[x < 1],y1,'g:', color = 'purple', linewidth = 4)
plt.plot(x[x > 1],y2,'g:', color = 'purple', linewidth = 4)
plt.xlim(-2,6)
plt.ylim(-6,6)
plt.title("Problem #3")
plt.show()

###############################################################################
# Question 4
###############################################################################
x = np.linspace(0, 2 * np.pi)
x*2

def p4(x):
    sin = np.sin(x)
    sin2x = np.sin(2*x)
    sin2 = [np.sin(x)*2 for x in range(len(x))]
    sin2_2 = [np.sin(2*x)*2 for x in range(len(x))]
    return(sin, sin2x, sin2, sin2_2)

sin, sin2x, sin2, sin2_2 = p4(x)

plt.figure(figsize=(10,8))
g1 = plt.subplot(2,2,1)
g1.plot(x, sin)
plt.axis([0,2,-2, 2 * np.pi] )
plt.title("Sin")
g2 = plt.subplot(2,2,2)
g2.plot(x, sin2x)
plt.axis([0,2,-2, 2 * np.pi] )
plt.title("Sin 2X")
g3 = plt.subplot(2,2,3)
g3.plot(x, sin2)
plt.axis([0,2,-2, 2 * np.pi] )
plt.title("Sin*2")
g4 = plt.subplot(2,2,4)
g4.plot(x, sin2_2)
plt.title("(Sine*2) * 2")
plt.axis([0,2,-2, 2 * np.pi] )
plt.show()

###############################################################################
# Question 5
##############################################################################

fars = np.load("/Users/thomascurran/Documents/GitRepos/BootCamp2018/Computation/Wk2_DataVis/FARS.npy")
plt.figure(figsize = (10,6))
ax1 = plt.subplot(121)
ax1.plot(fars[:,1], fars[:,2], "k,")
plt.title("Location of Car Accidents")
plt.axis("equal")
ax2 = plt.subplot(122)
ax2.hist(fars[:,0], bins = 12, range=[0,23], edgecolor = "black")
plt.title("Hours of Car Accidents")
plt.show()



###############################################################################
# Question 5
###############################################################################


x = np.linspace(-2*np.pi, 2 * np.pi)
y = x.copy()
def p6(x,y):
    g = (np.sin(x) * np.sin(y))/ x * y
    return(g)
X,Y = np.meshgrid(x,y)
Z = p6(X,Y)

plt.figure(figsize = (10,5))
ax1 = plt.subplot(121)
plt.pcolormesh(X,Y,Z, cmap ="viridis")
plt.colorbar()
ax2 = plt.subplot(122)
plt.contourf(X,Y,Z, 10, cmap = "viridis")
plt.colorbar()
plt.axis([-2*np.pi,2*np.pi, -2 * np.pi, 2 * np.pi])
plt.show()

























,
