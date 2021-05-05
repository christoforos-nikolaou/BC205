# BC205: Algorithms for Bioinformatics.

## Exercise III. Implementing a simplified version of the FastA algorithm

In this exercise you may work in pairs or groups of three (maximum).
You will be asked to implement the a simplified version of the FastA algorithm.

For implementation purposes you should consider the following:

1. Create a set of sequences that will correspond to the database. The set should contain sequences in the order of 10^3, with an average size of a few hundred bps. A suggestion is to use the set of coding (gene) sequences of a small genome such as E. coli or S. cerevisiae.
2. Choose a sequence from the database at random. 
3. Modify the chosen sequence with a limited number of substitutions, insertions or deletions but **not rearrangements**.
4. Implement a simplified version of the FastA algorithm using:
   a. a simple score of +1/0 for word matches/mismatches
   b. k=10 as the length of the matched word
   c. n=20 as the number of the n highest scoring pairs
   d. g=5 as the maximum gap size before joining regions, accounting for a gap penalty of -1 for each gapped nucleotid 
   e. Final outputs will consist of the the simple joined sequences with scores equalling the sum of scores (including gap penalties)  
