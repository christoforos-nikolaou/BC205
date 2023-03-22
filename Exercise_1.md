# BC205: Algorithms for Bioinformatics.

## Exercise 1. Introduction and Sequence Analysis (Deadline: April 7th, 2023)

You may choose **one** out of the following exercises and submit it by the deadline in any form you like, provided it contains:
1. The code for the solution, as well annotated with comments as possible.
2. A brief description/report of what you did and what you found.
3. The original data need to be included in the report (in the case that real data are involved)
4. A showcased example of a run must be included in the script if no real/original data are required

#### 1. Finding palindromes in a sequence using recursion
Palindrome sequences are (as their greek name suggests) sequences that are read identically from both directions.
Write a python script that will:  
a. define if a sequence contains a palindrome subsequence  
b. return the longest existing palindrome _p_ given a longer sequence _S_ 

#### 2. Identifying non-mers in a bacterial genome
Non-mers are k-mers that don't have a single instance in a greater corpus (e.g. a genome), that is they do not exist in a genome. 
Search the genome of E. coli for any given 10-mer and report the 10-mers that do not exist in the genome.
You may get the genome of E. coli from [here](files/ecoli.fa). 


#### 3. Use odds-ratio k-mers (k=2) to detect possible (Horizontal Gene Transfer) HGT events in a bacterial genome.
Employ a k-mer approach and calculate observed-over-expected ratios for k=2 and use the list of sixteen values as features instead of GC% in a similar approach to the one we used to identify possible events of HGT.
* Use a [Euclidean Distance](https://en.wikipedia.org/wiki/Euclidean_distance) to assess the differences between the 16-kmer signature of each window with the corresponding mean signature.
* Apply Z-transformation on this Euclidean Distance.

You may get the genome of Staphylococcus aureus from [here](files/Staaur.fa). 

#### 4. Use odds-ratio k-mers (k=2) to cluster bacterial genomes
Download ten different bacterial genomes (any ten you like) from [here](http://bacteria.ensembl.org/index.html) and use the same approach as in 3 (observed over expected k-mers of k=2 and Euclidean Distance).
Employ the distance approach between species and plot a hierarchical clustering of the ten genomes. Comment on the resulting tree.
