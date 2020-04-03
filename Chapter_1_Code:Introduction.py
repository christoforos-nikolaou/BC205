#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BC205: Algorithms in Bioinformatics
Chapter 1. Introduction (Python Code) 

Created on Thu Feb 27 10:23:13 2020

@author: christoforos
"""

#%%
""" Simple Euclid """
def simple_euclid(a,b):
  while (b > 0): # as long as the smallest of the two (or the remainder) is not zero
    a, b = b, a%b # switch a and b to b and mod(a/b)
  print(a) # print the last a (since b is now 0
#%%

#%%
""" Recursive Euclid """

def rec_euclid(a,b):

# check if a>b, else reverse order
    if b>a:
        a,b=b,a

    if a>b:
        # best case scenario, b is lcd
        if a%b==0:
            lcd=b
            return(lcd)

        if a%b>0:
        # implement Euclid: b becomes a and mod(a/b) becomes b
            a,b=b,a%b            
            return(rec_euclid(a,b)) # <---what happens here?
  
  
#%%  


#%%
""" Simple Sort """

def simplesort(N):

    i=0
    S=[]
    minind=0
    while (i < len(N)):
        minimum = N[i]
        j = i
        while (j < len(N)):
            if minimum >= N[j]:
                minimum = N[j]
                minind = j
                j = j + 1
            else:
                j = j + 1 
        S.append(N[minind])
        N.remove(N[minind])
    return(S)
 #%%   
   
#%% 
""" Merge Sort """

def merge(a,b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

def mergesort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = int(len(x)/2)
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a,b)
#%%

#%%
""" Fibonacci Array """
def SimpleFibonacci(N):
	fib=[]
	fib.append(1)
	fib.append(1)
	for i in range(2,N):
		fib.append(fib[i-1]+fib[i-2])
	return fib[i]
#%%

#%%
""" Fibonacci Recursion """
def RecursiveFibonacci(N):
	a, b = 1, 1
	for i in range(N-2):
		a, b = b, a+b
	return b

#%%
    
