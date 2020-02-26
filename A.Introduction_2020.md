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
  
> *"Any well-defined computational procedure that takes some value, or sets of values as input and produces some value, or sets of values as output."*  
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
        
      if (C equals 0) {print LCD=C; end}  
```

## Writing the damn thing: Programming
* You can choose your language of choice.
* Our focus will not be so much on coding as on the design and the general approach

## LCD Take#1 
(Python Implementation)

```
def simple_euclid(a,b)

while (b > 0): # as long as the smallest of the two (or the remainder) is not zero
	a, b = b, a%b # switch a and b to b and mod(a/b)
	
print a # print the last a (since b is now 0)
```

# What does it do?
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
            return(euclid(a,b)) # <---what happens here?
```

# What does it do?

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
