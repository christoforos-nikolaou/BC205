## Final Projects (Proposals)

Below you may find a list of suggested topics for your final project in our class.
Some of them have been suggested by you and hence people who came up with the idea will have priority.
Most of the topics are vaguely described. They will be further elaborated once they are assigned to people (or groups).
  
One last thing I would like to suggest is that the final projects are **presented** by you to the whole class in a couple of dates we can set after the final deadline (June 30th)
  
* The list (items still being added)

1. **Alignment-free pairwise sequence similarity using k-mer frequencies**. The project will build on approaches such as FASTA and will attempt to provide similar results to a NW alignment. **(Sofia)**
2. **Identification of SLiMs in Viral genomes** [Not available]
3. **Linear-time Sequence searches on Suffix trees.** 
4. **Markov State Modeling (or topics related to Markov Chains and Hidden Markov Models)**. [Not available]
5. **Comparing genome segmentations**. The idea here is to propose ways to quantitatively compare two (or more) different segmentations of a linear series (such as genomes or chromosomes). You will start by assuming that the same genome is split in different ways into "states", e.g. A-A-B-B-B-A vs A-A-A-A-B-B. You should find a way to calculate how similar the two patterns are. **(Aris)**
6. **Optimal RNA folding algorithm**. Given a single-stranded RNA sequence and assuming nucleotides pair as A:U and G:C find a way to define the maximum number of pairings between them. **(Christos)**
7. **Network algorithms**. Finding the shortest path between two elements in a biological network. **(Danai)**
8. **Distance and Clustering**. Implement the following process to create a hierarchical clustering of sequences. Given N nucleotide sequences and a simple substitution scheme (Match:1, Mismatch:0, Gap:-1) propose a way to: a) calculate similarities for all against all sequences and b) cluster them hierarchically using the UPGMA algorithm on similarities **(Ioanna)**
9. **Maximal coverage of valued elements**. Given: a) the total length of a genome (or a chromosome) and b) a set of _overlapping_ segment coordinates from that genome where each segment is assigned a value(score). Find the set of non-overlapping segments that maximizes the sum of values(scores) for the given genome. **(Aggelos)**
10. **Cluster Discovery in Biological Sequence**. The idea here is to approach biological sequences (genomes, proteins etc) as representations of "random walks" in which the probability of having a residue _N_ followed by another _N+1_ is the same throughout the sequence (and may be calculated, or set arbitrarily). Given a set of probabilities the goal of this work will be to identify clusters of sequences with clear over-representations, i.e. occurring more frequently than by chance. **(Georgina)**
11. **Τοpologically Associated Domains from contact maps**. Contact maps (from chromosome conformation experiments) are square matrices whose values correspond to frequencies of contacts between particular regions in linear chromosomes. The idead for this project is to implement an algorithm for the identification and of topologically associated domains (TADs) which are defined as _blocks of linear sequence within which contacts are more frequent than between them and other areas_. **(Maria)**
12. **Creating a Suffix Trie from the Suffix Array of a given Sequence**. The idea here is purely algorithmic. Given a DNA sequence, first construct its suffix array and then use it to construct its suffix trie. Use sequences of different complexity to show how the suffix trie size scales with the the complexity of the sequence. 

[Note: For most of the topics I have suggested I can help with the definition of the problem, guide you with literature suggestions etc. For the topics you have suggested we can do this together (but it will require some work from your part as well)]
