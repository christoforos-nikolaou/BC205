# BC205: Algorithms for Bioinformatics.

## Exercise III. Implementing a simplified version of the FastA algorithm

In this exercise you may work in pairs or groups of three (maximum).
You will be asked to implement the a simplified version of the FastA algorithm.

For implementation purposes you should consider the following:

1. Take the query sequence that you will find in this [link](https://github.com/christoforos-nikolaou/BC205/blob/master/query.fa) to search it against:
2. A set of sequences that contains the total number of coding (gene) sequences of _S. cerevisiae_ that you may find [here](https://www.dropbox.com/s/ilokqlhvez6tvga/all_yeast_genes_minplus1k.fa).
3. You are asked to implement a simplified version of the FastA algorithm using:  
   
   a. a simple score of +1/0 for word matches/mismatches. This means that _S[i]_ will be incremmented by +1 each time a k-mer is found.  

   b. k=5 as the length of the matched word 

   c. m=20 as the size of matched diagonals (_S[i]_) that you will keep in each search  

   d. g=3 as the maximum gap size before joining regions
   
   e. a total score of 50% of the length of the query sequence

   e. Final outputs will consist of a list of matched sequences that fulfill the above criteria alongside with their Total Scores.
   
   f. Report the highest matching sequence. Which gene does it correspond to?
