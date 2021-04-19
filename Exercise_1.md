# BC205: Algorithms for Bioinformatics.

## Exercise I. Introduction to Sequence Analysis (with recursion)

#### Finding palindromes in a sequence using recursion
There is an easy way to define a palindrome sequence _S_ of length _l_ if we consider its indices _1:l_. This is:
```
S is a palindrome if S[1:l]==S[l:1]
```
* Write a function **using recursion** that will examine:
a. whether a sequence contains a palindrome in the middle (or not).
b. will return the longest possible palindrome 
