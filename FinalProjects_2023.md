## Final Projects (June 2023)

Below you may find a list of suggested topics for your final project in our class.
Some of the topics are described in brief and without further details. 
They will be further elaborated once they are assigned to people (or groups).

You may choose to work alone or in groups of two. Some projects are a bit simple to be assigned to two people so I am denoting each topic with either (1) or (2) at the end, to let you know which can be shared.

The **deadline** for handing in your projects is **Sunday July 9th, 2023**.


1. **Alignment-free pairwise sequence similarity using k-mer frequencies**. The project will build on approaches such as FASTA and will attempt to provide similar results to a NW alignment.  (2)
  
2. **Suffix Tree Creation and Search**: Write a program that will create a Suffix Tree from a DNA sequence $S$ and then it will search for the existence of any given substring $s$. (2)

3. **Comparing genome segmentations**. The idea here is to propose ways to quantitatively compare two (or more) different segmentations of a linear series (such as genomes or chromosomes). You will start by assuming that the same genome is split in different ways into "states", e.g. A-A-B-B-B-A vs A-A-A-A-B-B. You should find a way to calculate how similar the two patterns are. (1) 
    
4. **Network algorithms**. Finding the shortest path between two elements in a biological network. You will start with a network structure in any format you want (either an edge list or an adjacency matrix). Given two nodes A and B, you should find the shortest path between the two nodes. (1) 
   
5. **Distance and Clustering**. Implement the following process to create a hierarchical clustering of sequences. Given N nucleotide sequences and a simple substitution scheme (Match:1, Mismatch:0, Gap:-1) propose a way to: a) calculate similarities for all against all sequences and b) cluster them hierarchically using any metric you prefer. The final outcome will be a distance $NxN$ table. (2)
   
6. **Aggregate values of a given score for genomic intervals**. The idea here is rather simple. You are given two files. One is a bed-type genomic coordinate file and the other contains a three-column output which correspond to chromosome-position-score, and where the score is a nucleotide-specific score. Write a program that will take the scores of the second file and aggregate them along the coordinates of the first to produce a new bed-type file with chromosome-start-end followed by an aggregate value of the interval. Allow the aggregate value to be chosen between sum, mean, standard deviation, maximum or minimum. (1)

7. **Maximal coverage of valued elements**. Given: a) the total length of a genome (or a chromosome) and b) a set of _overlapping_ segment coordinates from that genome where each segment is assigned a value(score). Find the set of non-overlapping segments that maximizes the sum of values(scores) for the given genome. (2) 
   
8.  **Cluster Discovery in Biological Sequence**. The idea here is to approach biological sequences (genomes, proteins etc) as representations of "random walks" in which the probability of having a residue _N_ followed by another _N+1_ is the same throughout the sequence (and may be calculated, or set arbitrarily). Given a set of probabilities the goal of this work will be to identify clusters of sequences with clear over-representations, i.e. occurring more frequently than by chance. (2)


8.  **Τοpologically Associated Domains from contact maps**. Contact maps (from chromosome conformation experiments) are square matrices whose values correspond to frequencies of contacts between particular regions in linear chromosomes. The idead for this project is to implement an algorithm for the identification and of topologically associated domains (TADs) which are defined as _blocks of linear sequence within which contacts are more frequent than between them and other areas_. (1)


9.  **Creating a Suffix Trie from the Suffix Array of a given Sequence**. The idea here is purely algorithmic. Given a DNA sequence, first construct its suffix array and then use it to construct its suffix trie. Use sequences of different complexity to show how the suffix trie size scales with the the complexity of the sequence. (2)

