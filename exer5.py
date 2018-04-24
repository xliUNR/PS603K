#!/usr/bin/python
import sys
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt



#define last digit function
def last_digit(n):
    n = str(n)
    return int(n[len(n)-1])



#initialize arrays to be used to store histogram numbers
turnout = [0,0,0,0,0,0,0,0,0,0]
volandov = [0,0,0,0,0,0,0,0,0,0]
#also initialize array for x axis of graph, these correspond to digits
digits = [0,1,2,3,4,5,6,7,8,9]

#read in filename from command line args
filename = str(sys.argv[1])
print(filename)

#read in csv file as a matrix
data = pd.read_csv(filename).as_matrix()

#loop over all rows and find last digit of turnout col and volandov col
for i in range(0, len(data) ):
    turnoutIdx = last_digit(data[i][0])
    volandovIdx = last_digit(data[i][1])

    turnout[turnoutIdx]+=1
    volandov[volandovIdx]+=1

#print results 
print("Voter turnout last digit analysis: \n")
print(turnout)
print("Volandov percentage last digit analysis: \n")
print(volandov)

#graph results
turnoutGraph = plt.bar( digits, turnout )
plt.xlabel('Digits')
plt.ylabel('Frequency')
plt.title('Voter Turnout Last digit analysis')
plt.show(turnoutGraph)

VolGraph = plt.bar( digits, volandov )
plt.xlabel('Digits')
plt.ylabel('Frequency')
plt.title('Volandov Percentage Last digit analysis')
plt.show(VolGraph)

