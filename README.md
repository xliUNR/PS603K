# PS603K
I am uploading my last digit analysis program into this repository. 
This program was written for exercise 5 for Political Science 603K: Cybersecurity.
This program looks at the last digits of input numbers to see if there is a pattern.
Ideally, if these numbers are random, the distribution should be uniform. Any deviations from uniformity suggests election tampering.
## Dependencies
This program was developed in Python2 using the following packages: matplotlib, numpy, and pandas.

## How the program works
This program will read in a n row by 2 col .csv file into matrix. File name is provided via command line argument.
The program features a function last_digit that returns the last digit of input number.
Function stolen from here: https://artofproblemsolving.com/community/c76406h1091794s3_last_digit_program
Credit to Frog123 for writing it.

The last digit is used as an index for histogram bucket array. 
Program iterates over every row.
Each array position is incremented by 1 each time the digit that corresponds to that index occurs. 
These arrays are then graphed in a bar chart using matplotlib.pyplot
