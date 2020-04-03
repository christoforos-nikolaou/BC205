# BC205: Algorithms for Bioinformatics. I. An Introduction
## Christoforos Nikolaou

## Algorithms in Bioinformatics

The course will cover:

- An introduction to the concept of Algorithms
- A listing of *some* of the major problems of Bioinformatics
- A detailed description of algorithmic approaches to these problems

## Evaluation
- Exercises (50%)
- Final exam (50%)

## Reading
- **Introduction to Algorithms. (Cormen, Leiserson, Rivest and Stein)** _for a general intro, but may be rather tecnhical for biologists_
- **Introduction to Bioinformatics Algorithms. (Pevzner and Jones)** _covers basic Bioinformatics algorithms with a right balance between CS and Biology_
- **Bioinformatics Algorithms. A practical approach (Pevzner and Compeau)** _very good choice for both disciplines, with a lot of practicals_
- **Genome-scale Algorithm desing (Tomescu, Bellazzougui, Cunial and Makinen)** _NGS-related but quite tecnhincal_


## Course Outline

- Introduction, concepts and algorithmic "warm-up"
- Analyzing Sequence Composition
- Motifs: Search, Evaluation and Discovery
- Sequence Alignment
- Data structures for NGS applications
- Algorithms inspired by NGS problems (mapping, peak finding and differential expression)
- Graph Algorithms

## What is an Algorithm

**Formally**  

> **Algorithm**: A systematic and _well-defined_ procedure that produces, _in a finite number of steps_, the answer to a question or the solution of a problem.  
[Encyclopaedia Britannica]

**Informally**  

> **Algorithm:** "Any well-defined computational procedure that takes some value, or sets of values as input and produces some value, or sets of values as output."
[Cormen, Leiserson, Rivest & Stein]


## Problems of Bioinformatics *(that we will be discussing)*

- Analyzing Sequence Composition (Algorithmic Introduction)
- Data Structures (Arrays, Hashes, Trees)
- Searching/Matching/Extracting Motifs in Sequences (Randomized Algorithms)
- Comparing Sequences through Alignments (Dynamic Programing)
- Next-generation Sequencing Analysis (Branch and Bound)
- Biological Networks (Graph Algorithms)

## Some (Simple) Problems
1. Finding the largest common divisor of two numbers
2. Sorting a set of integers
3. Calculating the Fibonacci series for up to a number N
4. Find the positive root of a quadratic equation

## And some not so simple ones
1. Ηow many TATA-boxes exist in a DNA sequence?
2. Where lies the origin of replication in a bacterial genome?
3. How similar are two genomic sequences?

## Step 1. Thinking the problem through
* The hardest part:
    * What is the input?
    * What is the (expected) output?
    * How can we do it?
    * How can we do it faster?

## Step 2. Formulate the problem
* Break the problem into pieces
* Identify (in detail) a process of simpler problems
* Work out the simpler problems in order

## Case 1: The Largest Common Divisor Problem  
* Given two integer numbers _a_ and _b_
* Find an integer _lcd_ that:
  - divides both _a_ and _b_ with 0 remainder
  - is the largest possible number

## A solution: Euclid's Algorithm for LCD

* Euclid is said to have proposed an elegant solution.

* The basis of the solution is both _a_ and _b_ should be able to be represented as products of _lcd_

* In this sense, the best case scenario for _lcd_ is that _mod(a/b)=0, lcd=a/b_, which means that the smaller of the two numbers is actually the _lcd_

* If this is not the case and _mod(a/b)=c_ then _lcd_ should be smaller or equal to the remainder of the division. The problem now is to find the _lcd_ of the remainder _c_ and the smaller number _b_. It is basically **the same problem**.

* Through a repetitive process in which _a, b_ are substituted by _b, mod(a/b)_ in each step we stop when _mod(a/b)=0_, declaring _b_ as the _lcd_.


## Euclid's Algorithm (Process)

1. Start with two numbers a, b (a > b)
2. Divide a/b and keep the remainder c
3. Now, divide b/c and keep the remainder d
4. Repeat the division until there is no remainder
5. Report the last divisor as the LCD of a and b.

## Let's make it more formal. Pseudocode

```
Input: A, B  

    # C=remainder(A/B)  

      if (C is greater than 0) {B->A; C->B; goto #}  

      if (C equals 0) {print LCD=Β; end}  
```

## Writing the damn thing: Programming
* You can choose your language of choice.
* Our focus will not be so much on coding as on the design and the general approach

## LCD Take#1
(Python Implementation)

```
def simple_euclid(a,b):
  while (b > 0): # as long as the smallest of the two (or the remainder) is not zero
    a, b = b, a%b # switch a and b to b and mod(a/b)
  print a # print the last a (since b is now 0)
```

## What does it do?
The solution above goes through a simple (but clever) iteration just as Euclid suggested

```
# enters an iterative process if b > 0
while (b > 0): # Checks if the smallest of the numbers is > 0
               # it's basically the remainder of the division

	# swaps a and b with b and the remainder of the division
	a, b = b, a%b
	      # Calculates the division
	      # Extracts the remainder
	      # Makes the swap

print a # returns the result as the last divisor that (gave 0 remainder)
```

## LCD Take#2
```
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
```

## What does it do?

* The most interesting part is the place where the function calls itself

```
        if a%b>0:
            a,b=b,a%b            
            return(euclid(a,b)) # <-HERE
```

* This is a nice example of **recursion**, a process through which we take advantage of our algorithmic process by **calling it** from within itself.
* While very useful it is not always the best way to proceed (as for instance in this case)


## Iteration vs Recursion

* In iteration control is performed by the value of b, while in recursion it is a more general control statement (_mod(a/b)>0_)
* Infinite iteration means waiting forever but infinite recursion means trouble, so **be careful!**
* In many cases (not this one) recursion appears to be more elegant, however iteration is always simpler, easier to follow and with smaller burden on the system


## Case 2: Sorting a series of integers
Starting with N integers, order them from the smallest to the largest

## Sorting Take #1: Simple Sort (Pseudocode)

```
Input N[i] list of numbers
Output S[i] list of sorted N

while(there is a list)
for i in 1:l # l is the size of the list
  minimum<-N[i] # assign an initial minimum value  
    for j in 1:l # loop over all elements
      if (minimum >= N[j]) # check for minimum constraint
        minimum <- N[j]
      else
        continue
    remove minimum from N
    append minimum to S
return(S)    

```

## Simple Sort
(Python Implementation)

```
def SimpleSort(N):

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
```    

## Step 3. Evaluating the Complexity
Pause and think:
* How many calculations did SimpleSort require?
* How does the number of calculations scale with the size of the list N?
  - For each element in the list we need N-1 comparisons
  - We then shorten the list by -1 and repeat
  - We thus need (N-1)+(N-2)+(N-3)...+1 calculations
  - This is the sum of a series with period=1 and is equal to:((N-1)(N-2))/2
* This means that as N increases, the number of calculations increases by N^2.

## Brute Force Approaches
* SimpleSort belongs to a type of algorithms that are called "Exhaustive" or "Brute Force".
* This means that they proceed with a simple "all out" approach that attacks the problem directly, in the hope that it is not too complex and expecting that the mere "force" of computation can solve it.
* Brute Force approaches work in a satisfactory way if the problem is not very complex.
* However they can be problematic if the problem is not simple as we will see in the following.

## Big-O, O() notation
* O()-notation is a means to express the complexity of an algorithm, in particular the way with which the number of calculation increases with the size of the input
* O() is shown as a function of input size (n) depending on the way processing time scales with n.
* For example SimpleSort is O(n^2) because as we saw it scales with n-quadratic

## Sorting Take #2: MergeSort
* Instead of taking each element and checking if it is the smallest in a list of gradually decreasing length, MergeSort implements a different (and faster strategy)
* It starts by **dividing** the list of numbers into two sublists and trying to sort these smaller lists before joining them back to the full list.
* You can imagine consecutive splits that come down to sublists of (N=2) in which the sorting is trivial: We basically need to check which is the greater of two numbers.
* The key in the process is to carefully implement the consecutive splits and then merging of the sublists (which gives the algorithm its name)
* This is done with a clever use of **recursion**.

## MergeSort. A case of Recursion
Pseudocode (Recursion)
The pseudocode below shows how the recursive sorting is done

```
Start with a list of L[N] numbers:
    # Split L[N] into two half-lists: A[N/2] and B[N/2]
    A[N/2]<- Goto #(A[N/2])
    B[N/2]<- Goto #(B[N/2])
    for i in 1:length(A) and j in 1:length(B):
        if (A[i]<B[j]):
          C=C.A[i] # add A[i] to a list C[N]
          remove A[i]
        if (A[i]>B[j]):
          C=C.B[j] # add B[j] to a list C[N]
          remove B[j]
```

## Merge Sort (Merging)
The code below describes the merge function that joins the two sublists **once** they have been sorted.

```
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
```

## MergeSort (Recursive Call)

While the following code shows the recursive call we described in the psuedocode above

```
def MergeSort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = int(len(x)/2)
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a,b)

```


## Big-O Notation (Merge Sort)
* **MergeSort**: takes an array of N and splits it in half, then sorts each half by recursive calls of the merge function. Let's break this into the two components:
    * Splitting is done into halves which means that for a list of N, log2(N) splits will be required
    * The merging process is done by parsing the elements of A and B lists one at a time, thus for N values it takes O(n) time.  

Combination of the two gives that **MergeSort is O(nlogn)**.

* Question: Which is faster? SimpleSort or MergeSort?
* Question: Can you figure out the time complexity of Euclid's algorithm?

## Divide and Conquer approaches
* MergeSort belongs to a different type of approaches that are called "Divide and Conquer"
* Divide and Conquer approaches proceed (as their name implies) by dividing a complex problem into simpler subproblems and solving them either recursively or iteratively (usually the first)
* In many cases they are the only way to go around difficult problems that would require a prohibitive amount of calculations using Brute Force.

## Case 3: Fibonacci Series
> Calculate a sum of N numbers where each one is produced as the sum of the two that came immediately before it.
(the first two numbers are by definition set to 1)  
```  
  N[1]=1  
  N[2]=1  
  N[3]=N[2]+N[1]=1+1=2  
  N[4]=N[3]+N[2]=2+1=3  
  N[5]=N[4]+N[3]=3+2=5  
  etc  
```

*The problem: Calculate the Fibonacci element number N*

## Fibonnaci Take #1: Using an Array
```
def SimpleFibonacci(N):
	fib=[]
	fib.append(1)
	fib.append(1)
	for i in range(2,N):
		fib.append(fib[i-1]+fib[i-2])
	return fib[i]
```

## Fibonacci Take #2: Using Recursion
```
def RecursiveFibonacci(N):
	a, b = 1, 1
	for i in range(N-2):
		a, b = b, a+b
	return b
```

## Fibonacci: Analysis
* Take #1
    * We create an array of length N
    * We go through the array calculating the i-th element with a simple addition of i-1, i-2
* Take #2
    * We swap the values of a, b with b and the sum of the two
    * We recursively call the algorithm for i-1 and i-2

## Ask yourself
1. How does array-Fibonacci scale with N?
2. How does recursive-Fibonacci scale with N?
3. What is the Big-O notations of the two
4. What do you think about recursion now?

## Enough with this. What about Bioinformatics?
* What we will be discussing in this class may appear detached from the above but it is _not_ so.
* Issues like recursion, time complexity and efficiency will matter
* The way we transform the problem into _formal sets_ of questions is crucial.

## Some (not so simple) problems
- Given a long DNA sequence can you locate a given string of characters within it.
- Can you say how many times it is there, and where?
- Given two strings of characters can you find the longest common subsequence of a) un-interrupted characters b) characters with gaps c) characters with gaps and also some mismatches?
