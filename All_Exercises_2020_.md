# BC205: Algorithms for Bioinformatics.

## All Exercises (2020-)

## Exercise I. Iteration vs Recursion

#### 1. Factorial Calculation Iteration vs Recursion
Your exercise is this:
* Write **two versions** of program that will calculate the Factorial of (n) given n as input. These should be:  
  a. An iterative approach
  b. A recursive approach
* Try to estimate the number of calculations involved in each of the two approaches. Which one is faster?

## Exercise II. Recursion, initial sequence analysis

#### 2. Finding palindromes in a sequence using recursion
There is an easy way to define a palindrome sequence _S_ of length _l_ if we consider its indices _1:l_. This is:
```
S is a palindrome if S[1:l]==S[l:1]
```
* Write a function **using recursion** that will examine:
a. whether a sequence contains a palindrome in the middle (or not).
b. will return the longest possible palindrome 
