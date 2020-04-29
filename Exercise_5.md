# BC205: Algorithms for Bioinformatics.

## Exercise V. Aligning Two Sequences against each other in their full length

In this exercise you are asked to implement the Needlemann-Wunsch Dynamic Programming Algorithm for 
the Global Alignment of two DNA sequences

For implementation purposes consider the following two sequences:

S1: ATGCACACGTGAGGGACCCCGAT
S2: ATACACGTACACGTGCACCGTGATGCTCGACTGCAAC

And the following scoring scheme:

Match:    +1
Mismatch:  0
Gap:      -1

#### You are advised to work in the following way:

    1. Allow for the sequences to be given by the user
    2. Allow for the scoring scheme to be provided 
    3. Return a dual output that includes: 
      a. The alignment (use dashes (-) for gaps)
      b. The total score of the alignment
