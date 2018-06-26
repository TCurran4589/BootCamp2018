import pandas as pd
import numpy as np
from random import choice

################################################################################
#
# Question #1
#
################################################################################

def arithmagic():
    step_1 = input("Enter a 3-digit number where the first and last "
                   "digits differ by 2 or more: ")

    if len(step_1) < 3:
        raise ValueError("Number must be 3 or more digits")

    if int(str(step_1[-1])) - int(str(step_1)[0]) < 2:
        raise ValueError(
            "Difference between first and last digit must be greater than 2")

    step_2 = input("Enter the reverse of the first number, obtained "
                   "by reading it backwards: ")

    if str(step_2) != str(step_1)[::-1]:
        raise ValueError(
            "Your input is not the correct reverse of the first step")

    step_3 = input("Enter the positive difference of these numbers: ")

    if int(step_3) < 0:
        raise ValueError(
            "Not the positive difference between step 1 and step 2")

    step_4 = input("Enter the reverse of the previous result: ")

    if str(step_4) != str(step_3)[::-1]:
        raise ValueError(
            "Your input is not the correct reverse of the third step")

    print(str(step_3), "+", str(step_4), "= 1089 (ta-da!)")


arithmagic()


################################################################################
#
# Question #2
#
################################################################################

def random_walk(max_iters=1e12):
    walk = 0
    directions = [1, -1]
    try:
        for i in range(int(max_iters)):
            walk += choice(directions)
        return walk
    except:
        raise KeyboardInterrupt(
            "Process interrupted at iteration {}".format(i))


random_walk()

################################################################################
#
# Question #3
#
################################################################################

class ContentFilter:

    def __init__(self, file_name):

        self.file_name = file_name

        try:
            with open(self.file_name) as file:
                #self.contents = file.readlines()
                self.contents = file.read().split('\n')

        except:
            raise FileNotFoundError("File not found")

        finally:
            file.close()

    def uniform(self, case = "upper"):
        '''
        1. uniform(): write the data to the outfile with uniform case. Include an
        additional keyword argument case that defaults to "upper".
        If case="upper", write the data in upper case. If case="lower", write the data
        in lower case. If case is not one of these two values, raise a ValueError.
        '''

        if case == 'upper':
            self.uniform_file = [self.contents[i].upper() for i in range(len(self.contents))]
            return(self.uniform_file)
        elif case == 'lower':
            self.uniform_file = [self.contents[i].lower() for i in range(len(self.contents))]
            return(self.uniform_file)
        else:
            raise ValueError("case must be 'upper' (default) or 'lower'")

    def reverse(self, new_file, unit = "line"):
        '''
        2. reverse(): write the data to the outfile in reverse order.

        Include an additional keyword argument unit that defaults to "line".

        If unit="word", reverse the ordering of the words in each line, but write the lines in the same order as
        the original file.

        If unit="line", reverse the ordering of the lines, but do not
        change the ordering of the words on each individual line.

        If unit is not one of these two values, raise a ValueError.
        '''

        def reverse_words(string):
            string_i = string.split(" ")
            string_i.reverse()
            output = (" ").join(string_i)
            return(output)

        self.new_file = new_file

        if unit == 'word':
            self.reversed_words = [reverse_words(self.contents[i]) for i in range(len(self.contents))]
            with open(self.new_file, 'w') as outfile:
                [outfile.write((self.reversed_words[i]+"\n")) for i in range(len(self.contents))]
                outfile.close()
                print("Reversed words written to {}".format(self.new_file))

        elif unit == 'line':
            with open(self.new_file, 'w') as outfile:
                self.reversed_lines = self.contents[::-1]
                [outfile.write((self.reversed_lines[i]+"\n")) for i in range(len(self.contents))]
                print("Lines Successfully Revered, new file written to {}".format(self.new_file))
        else:
            raise ValueError("check unit argument, must be either 'line' (default) or 'word'")

    def transpose(self):
        



works = ContentFilter("test.txt")


print(works.uniform(case = "lower"))

print(works.reverse(new_file = "murica.txt", unit ="word"))
print(works.reverse(new_file = "murica_reverselines.txt", unit = "line"))




################################################################################
'''
Problem 4.

Add the following methods to the ContentFilter class for writing the
contents of the original file to new files. Each method should accept a the name
of a file to write to and a keyword argument mode that specifies the file access
mode, defaulting to 'w'. If mode is not 'w', 'x', or 'a', raise a ValueError with
an informative message.


3. transpose(): write a “transposed” version of the data to the outfile. That is,
write the first word of each line of the data to the first line of the new file,
the second word of each line of the data to the second line of the new file,
and so on. Viewed as a matrix of words, the rows of the input file then become
the columns of the output file, and vice versa. You may assume that there are an
equal number of words on each line of the input file.
'''
################################################################################

with open("test.txt","r") as file:
    murica = file.read().split("\n")
