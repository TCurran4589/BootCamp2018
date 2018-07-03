import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

series_vals = np.zeros(len(x))

for i in range(0, len(x)):

    series_vals[i] = values(x.index[i])

ex1 = pd.Series(series_vals, index = indexVals)

print(ex1)
################################################################################
#
# Question 2
#
################################################################################
'''

d - number of dollars invested

p - probability stock goes up by a dollar (d)

(1-p) -probablity stock goes down by 1 dollar

'''

def investment(p, d=100):
    dates = pd.date_range('2000-01-01', '2000-12-31', freq = "D")
    vals = pd.Series(index = dates)
    vals[0] = d
    for i in range(1, len(vals)):
        prob = np.random.binomial(1, p)
        if(prob == 1):
            vals[i] = vals[i-1] + 1
        elif(prob == 0):
            vals[i] = vals[i-1] - 1
    return(vals)

probs = np.random.uniform(0.01, 0.90, ,4)
dollars = np.random.randint(10,1000,4)

for i in range(0, len(probs)):
    x = investment(p = probs[i], d = dollars[i])
    x.plot(title = 'Investments')


################################################################################
#
# Question 3
#
################################################################################

 #build toy data for SQL operations
name = ['Mylan', 'Regan', 'Justin', 'Jess', 'Jason', 'Remi', 'Matt', 'Alexander', 'JeanMarie']
sex = ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'M', 'F']
age = [20, 21, 18, 22, 19, 20, 20, 19, 20]
rank = ['Sp', 'Se', 'Fr', 'Se', 'Sp', 'J', 'J', 'J', 'Se']
ID = range(9)
aid = ['y', 'n', 'n', 'y', 'n', 'n', 'n', 'y', 'n']
GPA = [3.8, 3.5, 3.0, 3.9, 2.8, 2.9, 3.8, 3.4, 3.7]
mathID = [0, 1, 5, 6, 3]
mathGd = [4.0, 3.0, 3.5, 3.0, 4.0]
major = ['y', 'n', 'y', 'n', 'n']
studentInfo = pd.DataFrame({'ID': ID, 'Name': name, 'Sex': sex, 'Age': age,'Class': rank})
otherInfo = pd.DataFrame({'ID': ID, 'GPA': GPA, 'Financial_Aid': aid})
mathInfo = pd.DataFrame({'ID': mathID, 'Grade': mathGd, 'Math_Major': major})

studentInfo[(studentInfo['Age']>19) & (studentInfo['Sex']=='M')][['ID', 'Name']]
################################################################################
#
# Question 4
#
################################################################################

pd.merge(studentInfo[studentInfo['Sex'] == 'M'], otherInfo, on = 'ID', how = 'inner')[['ID', 'Age','GPA']]
################################################################################
#
# Question 5
#
################################################################################
df = pd.read_csv("crime_data.txt", header = 1, index_col = 0)

df['Crime Rate'] = df['Total'] / df['Population']

df.columns

mean_burg = np.mean(df.Burglary)
mean_crime = np.mean(df.Total)
print(np.mean(df.Burglary))
print(np.mean(df.Total))

print(df[(df.Burglary > mean_burg) & (df.Total < mean_crime)])

plt.plot(df.Population, df.Murder)
plt.show()

crime80s = df[(df.index >= 1980) & (df.index < 1990)][['Population','Violent','Robbery']].to_csv("crime_subset.csv")

################################################################################
#
# Question 6
#
################################################################################
titanic = pd.read_csv("titanic.csv")

titanic.drop(['Sibsp','Parch','Cabin','Boat','Body', 'home.dest'], axis = 1,inplace = True)

titanic['Age'].fillna(np.mean(titanic['Age']), inplace = True)
titanic.dropna(inplace = True)
titanic.isna().sum()


survived = np.sum(titanic.Survived)
survived_p = np.sum(titanic.Survived) / len(titanic.Survived)

print("Number Survived: ", survived, "Percent Survived: ", survived_p)

avg_price = np.mean(titanic.Fare)
max_price = titanic.Fare.max()

print("Average Price: ", avg_price)
print("Max Price: ",max_price)
oldest_survivor = titanic[titanic['Survived'] == 1][['Age']].max()
youngest_survivor = titanic[titanic['Survived'] == 1][['Age']].min()
print("Oldest Survivor: ", oldest_survivor)
print("Youngest Survivor: ", youngest_survivor)


oldest_death = titanic[titanic['Survived'] == 0][['Age']].max()
youngest_death = titanic[titanic['Survived'] == 0][['Age']].min()
print("Youngest Death: ", youngest_death)
print("Oldest Death: ", oldest_death)
