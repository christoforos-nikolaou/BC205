# BC205: Algorithms for Bioinformatics.

## Exercise III. Implementing the FASTA algorithm

For this third exercise you will need to implement the FASTA algorithm to perform a pairwise string matching. 

In more detail you are asked to implement a simplified version according to which:  
1. You will start with two short DNA sequences of your choice (no longer than 100nts each)
2. You will set a k-mer value between 3 and 5, provided as a parameter in the function. 
3. You will consider each match having a +1 value. No substitution matrices are to be used. You either have 1(match) or 0(no match).  
4. The minimum diagonal score will be a free parameter. This means that the diagonals to be used in the final alignment will be scored according to a sum value given by the user.   
5. The gap limit, that is the distance between matching diagonals will also be a free parameter (as above).  

The reported result should be a function that will use as input SeqA, SeqB, k-mer value, minimum score of diagonal to be merged, maximum score of gap.

The output of the function may be **all** possible alignments. You don't have to choose for the best one as this requires some additional programming steps.