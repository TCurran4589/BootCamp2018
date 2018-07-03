import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import linregress
from scipy.special import binom
import warnings
warnings.filterwarnings("ignore")
################################################################################
#
# Question 1
#
################################################################################

df =np.load("anscombe.npy")

################################################################################
#
# Question 2
#
################################################################################

n = np.array([0,1,2,3])
x = np.linspace(0,1,num = 10)
def bernstein(x, n = 4,v=4):
    for i in range(0,len(x)):
        for j in range(0,v):
            for k in range(0,n):
                g = binom(k,j) * np.power(x[i],j) * np.power((1 - x[i]), (k-j))
                print("X:{}, V:{}, N:{}, G:{}".format(x[i],j,k,g))
    return(g)

################################################################################
#
# Question 3
#
################################################################################

mlb = pd.DataFrame(np.load("MLB.npy")).rename(columns = {0: "Height(in)", 1:"Weight", 2:"Age"})

print(mlb.head())
#------------------------------------------------------------------------------#

plt.figure(figsize = (7,16))
p1 = plt.subplot(311)
p1.scatter(mlb['Age'], mlb['Height(in)'], edgecolor = 'none')
plt.title("MLB: Age vs Height")
plt.ylabel("Age")
plt.xlabel("Height (in)")
slope, intercept, r_value, p_value, std_err = linregress(mlb['Age'], mlb['Height(in)'])
p1.plot(mlb.Age, (intercept + slope*mlb['Age']), 'r')

#-----------------------------------------------------------------------------#
p2 = plt.subplot(312)
p2.scatter(mlb['Height(in)'], mlb['Weight'], edgecolor = 'none')
plt.title("MLB: Hieght vs Weight")
plt.ylabel("Height (in)")
plt.xlabel("Weight")
slope, intercept, r_value, p_value, std_err = linregress(mlb['Height(in)'], mlb['Weight'])
p2.plot(mlb['Height(in)'], (intercept + slope*mlb['Height(in)']), 'r')

#------------------------------------------------------------------------------#
p3 = plt.subplot(313)
p3.scatter(mlb['Age'], mlb['Weight'], edgecolor = 'none')
plt.title("MLB: Age vs Weight")
plt.ylabel("Weight")
plt.xlabel("Age")
slope, intercept, r_value, p_value, std_err = linregress(mlb['Age'], mlb['Weight'])
p3.plot(mlb.Age, (intercept + slope*mlb['Age']), 'r')

#------------------------------------------------------------------------------#

plt.show()


################################################################################
#
# Question 4
#
################################################################################

year, magnitude, long, lat = np.load("earthquakes.npy").T
plt.plot(year, magnitude, '.')
plt.xlabel("Year")
plt.ylabel("Magnitude")
plt.show()

# 1. How many earth quakes happened every year?
plt.hist(year, edgecolor = "black")
plt.xlabel("Year")
plt.ylabel("Number of Earth Quakes")
plt.title("Count of Earthquakes since 2000 (Magnitude > 5)")
plt.show()

# How often do stronger earthquakes happen compared to weaker ones?
import seaborn as sns
sns.distplot(magnitude,hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})
plt.title("Distribution of Magnitudes")
plt.xlabel("Magnitude")
plt.ylabel("Density")
plt.show()

#Where do the earthquakes happen?
plt.plot(long, lat, 'k,')
plt.axis("equal")
plt.title("Location of Earthquakes (2000 - 2010)")
plt.show()

################################################################################
#
# Question 5
#
################################################################################


def rosenbrock(x,y):
    return (np.power((1-x),2) + 100* np.power((y - np.power(x,2)),2))

x = np.linspace(-1.5, 1.5, 200)

X,Y = np.meshgrid(x,x)
Z = rosenbrock(X,Y)

plt.figure(figsize = (5,10))
ax1 = plt.subplot(211)
plt.pcolormesh(X,Y,Z, cmap = "magma")
plt.colorbar()

ax2 = plt.subplot(212)
plt.contourf(X,Y,Z, cmap = "viridis")
##cax = ax2.pcolormesh(X,Y,Z, cmap ='viridis' )
plt.colorbar()
plt.axis("equal")
plt.show()
################################################################################
#
# Question 5
#
################################################################################

countries = pd.DataFrame(np.load("countries.npy")).rename(columns = {0:'pop',1:'gdp',2:'male_height', 3:'female_height'})

names = ["Austria", "Bolivia", "Brazil", "China",
            "Finland", "Germany", "Hungary", "India",
            "Japan", "North Korea", "Montenegro", "Norway",
            "Peru", "South Korea", "Sri Lanka", "Switzerland",
            "Turkey", "United Kingdom", "United States", "Vietnam"]

countries['countries'] = names

countries = countries.set_index(countries.countries)

plt.hist(countries['male_height'], edgecolor = "black")
plt.title("Distribution of Average Male Height")
plt.ylabel("Count of Countries")
plt.xlabel("Average Male Height (cm)")
plt.show()



plt.scatter(countries['pop'], countries['gdp'])
plt.title('Relationship between GDP and Population')
plt.xlabel("Population")
plt.ylabel("GDP")

plt.bar(countries.index, countries['male_height'])
plt.xticks(rotation='vertical')
plt.title("Average Male Height")
plt.xlabel("Country")
plt.ylabel("Heigh (cm)t")
plt.show()


plt.bar(countries.index, countries['female_height'], color = "r")
plt.xticks(rotation='vertical')
plt.title("Average Female Height")
plt.xlabel("Country")
plt.ylabel("Heigh (cm)")
plt.show()
