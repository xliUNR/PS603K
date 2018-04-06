#!/usr/bin/python
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""
    This program plots histogram bar charts of last digits
"""


# define last digit function
def last_digit(n):
    n = str(n)
    return int( n[len(n) - 1] )



# initialize histogram buckets
turnout = [0] * 10
volandov = [0] * 10

# initialize variables for graphing
N = 10 # number of digits 0 - 9
ind = np.arange(N) # x locations for each digit
width = 0.35 # width of bars

# read in data from file
filename = str(sys.argv[1]) # takes in command line argument
print(filename) 

#read in csv file as a matrix
data = pd.read_csv(filename).as_matrix()

# Run last digit analysis 
for i in range( 0 , len(data) ):
    turnoutIdx = last_digit( data[i][0] )
    volIdx = last_digit( data[i][1] )

    turnout[ turnoutIdx ] += 1
    volandov[ volIdx ] += 1

# print results
print("Voter turnout histogram: \n")
print( turnout )

print("Volandov percentage histogram: \n")
print( volandov )

# create figure and subplots
fig, ax = plt.subplots()

turnoutBars = ax.bar( ind, turnout, width, color='r' ) 
volBars = ax.bar( ind + width, volandov, width, color='y' )

# add labels for graph
ax.set_ylabel('Digit occurances')
ax.set_title('Last Digit Histogram of Voting percentages')
ax.set_xticks(ind + width / 2 )
ax.set_xticklabels( ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') )
ax.legend( ( turnoutBars[0], volBars[0] ) , 
        ('Voting turnout', '% vote for Volandov'))

ax.legend( bbox_to_anchor=(1.05, 1), loc=2, norderaxespad=0. )

plt.show()
