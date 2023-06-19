## Final Projects (June 2023)

Below you may find a list of suggested topics for your final project in our class.
Some of the topics are described in brief and without further details.
They will be further elaborated once they are assigned to people (or groups).

You may choose to work alone or in groups of two. Some projects are a bit simple to be assigned to two people so I am denoting each topic with either (1) or (2) at the end, to let you know which can be shared.

The **deadline** for handing in your projects is **Sunday July 9th, 2023**.

1. **Alignment-free pairwise sequence similarity using k-mer frequencies**. The project will build on approaches such as FASTA and will attempt to provide similar results to a NW alignment. (2)

2. **Suffix Tree Creation and Search**: Write a program that will create a Suffix Tree from a DNA sequence $S$ and then it will search for the existence of any given substring $s$. (2)  
[Eleni Mourouzidou] (Please use a sequence of a considerable length, to check for the speed of the implementation)

3. **Comparing genome segmentations**. The idea here is to propose ways to quantitatively compare two (or more) different segmentations of a linear series (such as genomes or chromosomes). You will start by assuming that the same genome is split in different ways into "states", e.g. A-A-B-B-B-A vs A-A-A-A-B-B. You should find a way to calculate how similar the two patterns are. (1)

4. **Network algorithms**. Finding the shortest path between two elements in a biological network. You will start with a network structure in any format you want (either an edge list or an adjacency matrix). Given two nodes A and B, you should find the shortest path between the two nodes. (1)   
[Konstantinos Rounis] A single implementation for the shortest path identification.  
[Nikos Kanakis] Comparative Methods for shortest path identification  
You may use [this dataset](https://www.dropbox.com/s/h8tlpwfbajiym0b/TNFnetwork.txt) which contains a detailed edgelist for the Protein-Protein Interactions of TNF obtained from STRING-DB.

5. **Distance and Clustering**. Implement the following process to create a hierarchical clustering of sequences. Given N nucleotide sequences and a simple substitution scheme (Match:1, Mismatch:0, Gap:-1) propose a way to: a) calculate similarities for all against all sequences from pairwise alignments and b) cluster them hierarchically using any metric you prefer. The final outcome will be a distance $NxN$ table. (2)
(Note: You can use an already defined Python function for the clustering strategy).  
[Ioannis Rafail Tzonevrakis]  
You may use [this file](https://www.dropbox.com/s/6543cdghmuoizi8/histone1.fa?dl=0) containing a set of protein sequences for the H1 histone from 10 eukaryotes spanning the entire kingdom. You may also still use the match/mismatch scheme suggested above, since the sequences are relatively strongly conserved.  

6. **Aggregate values of a given score for genomic intervals**. The idea here is rather simple. You are given two files. One is a bed-type genomic coordinate file and the other contains a compressed-type chromosome-position-score, where the score is a nucleotide-specific score. Write a program that will take the scores of the second file and aggregate them along the coordinates of the first to produce a new bed-type file with chromosome-start-end followed by an aggregate value of the interval. Allow the aggregate value to be chosen between sum, mean, standard deviation, maximum or minimum. (1)  
[Marianna Stagaki]  
You may use the following files:   
a) as coordinate file you may use [this file](https://www.dropbox.com/scl/fi/6fc8stk76dg2vm93p85pn/saccer2_refseq_genes_TSS_plusmin500.bed?dl=0&rlkey=x9expw5ae08odk1fiyzcfp1ct) which contains 1000bp-long regions from the yeast genome centered around the transcription start sites of all yeast protein coding genes.    
b) as a score file you may use [this file](https://www.dropbox.com/scl/fi/ordt8x4lh325nln6cel8w/sacCer2_phCons.wig?dl=0&rlkey=6a5ay1t02fqhe70w88puv0kq8) which contains a nucleotide-resolution score that corresponds to the degree of sequence conservation for the entire yeast genome. The file format is wig type (see more about how to interpret this format [here](https://www.ensembl.org/info/website/upload/wig.html#:~:text=A%20WIG%20file%20consists%20of,formatting%20options%3A%20fixedStep%20and%20variableStep))  

7. **Maximal coverage of valued elements**. Given: a) the total length of a genome (or a chromosome) and b) a set of _overlapping_ segment coordinates from that genome where each segment is assigned a value(score). Find the set of non-overlapping segments that maximizes the sum of values(scores) for the given genome. (2)  
[Anna Efstathiou, Olympia Dialekti Vouzina]  
You may use [this file](https://www.dropbox.com/scl/fi/t1uvn8xfwavlo6jmt1cx1/sacCer3_chrIV_nucs_overlapping.bed?dl=0&rlkey=vuyfn519sqsp3wnns89nsdlal) which contains overlapping predictions for the positions of >80k nucleosomes in the chromosome IV of S. cerevisiae.  

8. **Cluster Discovery in Biological Sequence**. The idea here is to approach biological sequences (genomes, proteins etc) as representations of "random walks" in which the probability of having a residue _N_ followed by another _N+1_ is the same throughout the sequence (and may be calculated, or set arbitrarily). Given a set of probabilities the goal of this work will be to identify clusters of sequences with clear over-representations, i.e. occurring more frequently than by chance. (2)

9. **Τοpologically Associated Domains from contact maps**. Contact maps (from chromosome conformation experiments) are square matrices whose values correspond to frequencies of contacts between particular regions in linear chromosomes. The idead for this project is to implement an algorithm for the identification and of topologically associated domains (TADs) which are defined as _blocks of linear sequence within which contacts are more frequent than between them and other areas_. (1)  
[Agapi Eleni Simaiaki]


10. **Creating a Suffix Trie from the Suffix Array of a given Sequence**. The idea here is purely algorithmic. Given a DNA sequence, first construct its suffix array and then use it to construct its suffix trie. Use sequences of different complexity to show how the suffix trie size scales with the the complexity of the sequence. (2)  
[Aggelos Kozonakis]
