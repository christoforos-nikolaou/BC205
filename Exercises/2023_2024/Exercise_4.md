# BC205: Algorithms for Bioinformatics.

## Exercise II. Discovering and Evaluating hidden motifs in Sequences

For your second exercise you will need to implement the Gibbs Sampler for motif discovery in the language of your choice. 

A dataset of 50 short sequences is given may be found [here](https://www.dropbox.com/s/w9cpq4bwsb90j1i/motifs_in_sequence.fa). 
A short motif has been embedded in some of these sequences which you will have to discover through a Gibbs sampling approach.

What you need to do:  

#### Part 1  

    1. Implement the Gibbs Sampler in Python  
    2. Use a free parameter for the size k of the motif you will be searching for   
    3. Repeat the search for various values of k (e.g. from k=3 to k=7)  

**Result 1: Return the discovered motifs as PWMs**

#### Part 2  

    1. Calculate the Information Content of the discovered PWMs for each k
  
**Result 2: Report the k and the motif with the greatest (scaled) Information Content**     
