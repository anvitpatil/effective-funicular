# Python 3 program to print Latin Square 
import numpy as np
l=[]
# Function to prn x n Latin Square 
def printLatin(n): 

	# A variable to control the 
	# rotation point. 
	k = n + 1

	# Loop to prrows 
	for i in range(1, n + 1, 1): 
	
		# This loops runs only after first 
		# iteration of outer loop. It prints 
		# numbers from n to k 
		temp = k 
        l1=[]
        while (temp <= n) : 
			l1.append(temp) 
			temp += 1
        l.append(l1)
		# This loop prints
        #  numbers 
		# from 1 to k-1. 
        l1=[]
        for j in range(1, k): 
			l1.append(j) 
        l.append(l1)
        k -= 1
        print() 

# Driver Code 
n = 5

# Invoking printLatin function 
printLatin(n) 
l=np.array(l)
print(l)
# This code is contributed by R_Raj 
