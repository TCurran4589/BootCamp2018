import pandas as pd
import numpy as np

'''

Problem 1. Write a function that accepts a list L and returns the minimum, maximum, and
average of the entries of L (in that order). Can you implement this function in a single line?

'''

def problem1(L):
    print("min: ", np.min(L),"max: ",np.max(L),"average: ",np.mean(L))


L = np.arange(10)

problem1(L)


'''
Problem 2. Determine which of Python’s object types are mutable and which are immutable
by repeating the following experiment for an int, str, list, tuple, and set.

1. Create an object of the given type and assign a name to it.

2. Assign a new name to the first name.

3. Alter the object via only one of the names (for tuples, use my_tuple += (1,)).

4. Check to see if the two names are equal. If they are, then since changing one name
changed the other, the names refer to the same object and the object type is mutable.
Otherwise, the names refer to different objects—meaning a copy was made in step 2—and
therefore the object type is immutable.

'''
#answer: immutable
int_1 = 10
int_2 = int_1
int_2 += 5
int_2 == int_1

#answer: immutable
str_1 = "hello"
str_2 = str_1
str_2 *= 5
str_2 == str_1

#answer: mutable
list_1 = [1,2,3]
list_1
list_2 = list_1
list_2
list_2 += [4,5,6]
list_2 == list_1
list_2
list_1

#answer: immutable
tuple_1 = (1,2,3,4,5)
tuple_2 = tuple_1
tuple_2 += (1,)
tuple_2 == tuple_1
tuple_2

#answer: mutable
set_1 = (["a","b","c"])
set_2 = set_1
set_2 += ([1,2,3])
set_2 == set_1

set_2
set_1
'''

Create a module called calculator.py. Write a function that returns the sum
of two arguments and a function that returns the product of two arguments. Also use import
to add the sqrt() function from the math module to the namespace.

When this file is either run or imported, nothing should be executed.

In your solutions file, import your new custom module. Write a function that accepts two
numbers representing the lengths of the sides of a right triangle. Using only the functions from
calculator.py, calculate and return the length of the hypotenuse of the triangle.

'''
import calc
from math import sqrt
#a^2 + b^2 = c^2

a2 = calc.products(2,2)
b2 = calc.products(3,3)

c = sqrt(calc.addition(a2, b2))
print(c)

'''

Problem 4.
The power set of a set A, denoted P(A) or 2^A, is the set of all subsets of A,
including the empty set ∅ and A itself. For example, the power set of the set
A = {a, b, c} is 2^A = {∅, {a}, {b}, {c}, {a, b}, {a, c}, {b, c}, {a, b, c}}.

Write a function that accepts an iterable A. Use an itertools function to compute
the power set of A as a list of sets (why couldn’t it be a set of sets in Python?).

'''

from itertools import chain, cycle, combinations, permutations

A = ["a","b","c"]

def powerset(iterable):
    s = list(iterable)
    p_set = chain.from_iterable(combinations(s,r) for r in range(len(s)+1))
    return(list(p_set))


print(powerset(A))
'''
Problem 5.

Shut the box is a popular British pub game that is used to help children learn
arithmetic. The player starts with the numbers 1 through 9, and the goal of the game is to
eliminate as many of these numbers as possible. At each turn the player rolls two dice, then
chooses a set of integers from the remaining numbers that sum up to the sum of the dice
roll. These numbers are removed, and the dice are then rolled again. The game ends when
none of the remaining integers can be combined to the sum of the dice roll, and the player’s
final score is the sum of the numbers that could not be eliminated. For a demonstration, see
https://www.youtube.com/watch?v=vLlZGBQ6TKs.

Modify your solutions file so that when the file is run with the correct command line
arguments (but not when it is imported), the user plays a game of shut the box. The provided
module box.py contains some functions that will be useful in your implementation of the game.
You do not need to understand exactly how the functions work, but you do need to be able to
import and use them correctly. Your game should match the following specifications:

• Require three total command line arguments: the file name (included by default), the
player’s name, and a time limit in seconds. If there are not exactly three command line
arguments, do not start the game.

• Track the player’s remaining numbers, starting with 1 through 9.

• Use the random module to simulate rolling two six-sided dice. However, if the sum of the
player’s remaining numbers is 6 or less, role only one die.

• The player wins if they have no numbers left, and they lose if they are out of time or if
they cannot choose numbers to match the dice roll.

• If the game is not over, print the player’s remaining numbers, the sum of the dice roll,
and the number of seconds remaining. Prompt the user for numbers to eliminate. The
input should be one or more of the remaining integers, separated by spaces. If the user’s
input is invalid, prompt them for input again before rolling the dice again.
(Hint: use round() to format the number of seconds remaining nicely.)

• When the game is over, display the player’s name, their score, and the total number of
seconds since the beginning of the game. Congratulate or mock the player appropriately.

(Hint: Before you start coding, write an outline for the entire program, adding one feature
at a time. Only start implementing the game after you are completely finished designing it.)
Your game should look similar to the following examples. The characters in red are typed
inputs from the user.
'''


###############################################################################
# PSUEDO CODE:
#
#
###############################################################################

import box
import random
import numpy as np

def ShutTheBox():


    name = input("Name? ")

    time_limit = int(input("Time Limit? "))

    initial_list = list(range(1,10))

    assert isinstance(time_limit,(int, float)), "Time Limit is not a number"

    assert isinstance(name, (str)), "Name is not a string"

    def remove_nums(number_list):
        print("Numbers Left: {}".format(number_list))
        roll = random.randint(1,6) + random.randint(1,6)
        print("Roll: {}".format(roll))
        #print("Seconds Left: {}".format(time_limit))

        choices = [int(x) for x in input("Which Numbers would you like to eliminate? ").split()]

        while np.sum(choices) != roll:
            print("Those numbers do not add up to your roll")
            choices = [int(x) for x in input("Which Numbers would you like to eliminate? ").split()]
        else:
            remaining = set(initial_list) - set(choices)

        new_roll = random.randint(1,6) + random.randint(1,6)

        return(remaining, new_roll)



    numbers_left, roll2 = remove_nums(initial_list)

    while box.isvalid(roll2, numbers_left):
        numbers_left, roll2 = remove_nums(numbers_left)
#box.isvalid(roll, initial_list)
#    while box.isvalid(roll, initial_list):




ShutTheBox()
