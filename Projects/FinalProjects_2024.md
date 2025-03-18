## Final Projects (June 2024)

Below you may find a list of suggested topics for your final project in our class.
Some of the topics are described in brief and without further details.
They will be further elaborated once they are assigned to people (or groups).

The **deadline** for handing in your projects is **Sunday July 7th, 2024**.

1. **Alignment-free pairwise sequence similarity using common subsequences**. There are various methods that attempt to work around the concept of sequence alignment in quantifying sequence similarity. One of them is based on Common Subsequences, which is basically a method based on k-mer frequency comparison taken to the extreme with either looking at the longest common substring (or substrings) between two given sequences.
   You are asked to:

   * Given one sequence that you may find [here](https://www.dropbox.com/scl/fi/tvihug3o0k5y25ragyifp/Ex1_query.fa?rlkey=x7bft3e0qsjov8ctu5frw31a5&st=2gf2vo2t&dl=0)
   * And a set of sequences you already searched for in Exercise 4, which you will find [here](https://www.dropbox.com/s/ilokqlhvez6tvga/all_yeast_genes_minplus1k.fa)
   * Write the code that will look for the longest common substring between two sequences and scan the query (unknown) sequence against the entire set of sequences.
   * a. Report the sequence from the collection that has the longest common substring
   * b. Report all the sequence(s) from the collection for which the longest common substring with the query sequence are longer than 30, 50 and 150 nucleotides.
2. **Suffix Array Creation and Sequence Search**. We have already discussed the construction of Suffix Arrays but you can read more about them [here](https://academic.oup.com/bib/article/15/2/138/212729?login=true).You are asked to:

   * Write a program that will create a Suffix Array from a DNA sequence $S$ and then it will search for the existence of any given substring $s$.
   * Implement it on a sequence of a considerable length, to check for the speed of the implementation.
3. **Use the BWT to compress a given sequence**. We have already discussed the Burrows-Wheeler Transform and how it could assist in the compression of a sequence. You are asked to:

   * Write the code that will take a sequence of any type (you may choose your own) and create the BWT.
   * Use the BWT to compress the sequence in a meaningful way. One such is through Run-Length Encoding, a simple approach that consists of replacing a string of same character strings with its multiple (e.g. AAAAA becomes A5).
   * The code should be reversable, meaning it should also contain the reversal of the compressed string into the original sequence.
4. **Find the Longest Palindrome of a Sequence using Suffix Tree**.
   You are asked to find the longest palindrome of a sequence using suffix trees. We have already discussed palindromes as substrings of a string that are identical when read from both directions. Your task here will be to do this faster with the use of a suffix tree. Try to think a bit outside of the box with this one, regarding **which** Suffix Tree you will need to build.
5. **Comparing genome segmentations**. The idea here is to propose ways to quantitatively compare two (or more) different segmentations of a linear series (such as genomes or chromosomes). You should find a way to calculate how similar the two patterns are. You may be inspired by the bedtools overlap function.You are asked to:

   * Take the two coordinate files you will find in the following links as [coord file 1](https://www.dropbox.com/scl/fi/8f6bngwk79ndlqtdi681k/NewRun_MAC1_t4.bed?rlkey=bwqugj7tujm0rkl9la7nqewho&st=0o31va86&dl=0) and [coord file 2](https://www.dropbox.com/scl/fi/sffd3acvrulg40jvce8z3/NewRun_AFT1_t4.bed?rlkey=f43phaxa0tc4ye4l61bytrgz8&st=c4ljukhs&dl=0)
   * Think of a strategy to calculate the degree of overlap between the two coordinate files.
   * How big or small is it?
   * How can it be compared against a null model?
   * Can you think of a way to score the overlap and assess its statistical significance?
   * Provide a script for all of the above.
6. **Network algorithms**. Finding the shortest path between two elements in a biological network. You will start with a network structure in any format you want (either an edge list or an adjacency matrix). Given two nodes A and B, you should find the shortest path between the two nodes. You may use [this dataset](https://www.dropbox.com/s/h8tlpwfbajiym0b/TNFnetwork.txt) which contains a detailed edgelist for the Protein-Protein Interactions of TNF obtained from STRING-DB.
7. **Distance and Clustering**. Implement the following process to create a hierarchical clustering of sequences. Given N nucleotide sequences and a simple substitution scheme (Match:1, Mismatch:0, Gap:-1) propose a way to: a) calculate similarities for all against all sequences from pairwise alignments and b) cluster them hierarchically using any metric you prefer. The final outcome will be a distance $NxN$ table. (2)
   (Note: You can use an already defined Python function for the clustering strategy)You may use [this file](https://www.dropbox.com/s/6543cdghmuoizi8/histone1.fa?dl=0) containing a set of protein sequences for the H1 histone from 10 eukaryotes spanning the entire kingdom. You may also still use the match/mismatch scheme suggested above, since the sequences are relatively strongly conserved.
8. **Aggregate values of a given score for genomic intervals**. The idea here is rather simple. You are given two files. One is a bed-type genomic coordinate file and the other contains a compressed-type chromosome-position-score, where the score is a nucleotide-specific score.
   You are asked to:

   * Get the genome coordinate file which you will obtain from [here](https://www.dropbox.com/scl/fi/6fc8stk76dg2vm93p85pn/saccer2_refseq_genes_TSS_plusmin500.bed?dl=0&rlkey=x9expw5ae08odk1fiyzcfp1ct) and which contains 1000bp-long regions from the yeast genome centered around the transcription start sites of all yeast protein coding genes.
   * Get the genome score file that you will obtain from [here](https://www.dropbox.com/scl/fi/ordt8x4lh325nln6cel8w/sacCer2_phCons.wig?dl=0&rlkey=6a5ay1t02fqhe70w88puv0kq8) which contains a nucleotide-resolution score that corresponds to the degree of sequence conservation for the entire yeast genome. The file format is wig type (see more about how to interpret this format [here](https://www.ensembl.org/info/website/upload/wig.html#:~:text=A%20WIG%20file%20consists%20of,formatting%20options%3A%20fixedStep%20and%20variableStep))
   * Write a program that will take the scores of the second file and aggregate them along the coordinates of the first to produce a new bed-type file with chromosome-start-end followed by an aggregate value of the interval. Allow the aggregate value to be chosen between sum, mean, standard deviation, maximum or minimum. You may use the following files:  b)
9. **Maximal coverage of valued elements**. Given: a) the total length of a genome (or a chromosome) and b) a set of _overlapping_ segment coordinates from that genome where each segment is assigned a value(score). Find the set of non-overlapping segments that maximizes the sum of values(scores) for the given genome.
   You are asked to:

   * Obtain [this file](https://www.dropbox.com/scl/fi/t1uvn8xfwavlo6jmt1cx1/sacCer3_chrIV_nucs_overlapping.bed?dl=0&rlkey=vuyfn519sqsp3wnns89nsdlal) which contains overlapping predictions for the positions of >80k nucleosomes in the chromosome IV of S. cerevisiae.
   * Devise a strategy according to which the coordinate segments in the file (that means each row in the file) will be considered on the basis of their score (given in the 4th column)
   * The output should be a **subset** of the original files that will contain the maximum number of non-overlapping segments that sum up to the highest overall score.
   * You can try to compare a greedy approach, with a dynamic programming approach **(BUT! stay away from Brute Force)**
   * Provide the python code that will take the above file as input and return a similar set of non-overlapping coordinates.
10. **Cluster Discovery in Biological Sequence**. The idea here is to approach biological sequences (genomes, proteins etc) as representations of "random walks" in which the probability of having a residue _N_ followed by another _N+1_ is the same throughout the sequence (and may be calculated, or set arbitrarily). Given a set of probabilities the goal of this work will be to identify clusters of sequences with clear over-representations, i.e. occurring more frequently than by chance.
11. **Τοpologically Associated Domains from contact maps**. Contact maps (from chromosome conformation experiments) are square matrices whose values correspond to frequencies of contacts between particular regions in linear chromosomes. The idead for this project is to implement an algorithm for the identification and of topologically associated domains (TADs) which are defined as _blocks of linear sequence within which contacts are more frequent than between them and other areas_.
    You are asked to:

    * Obtain contact data in a matrix that you will find in [this file](https://www.dropbox.com/scl/fi/hkwcq6cpvk60hdsakwtyn/chr11_contact_matrix.tsv?rlkey=cwvxzmvur7qiss3jsq6p18zeg&st=yxl6u99j&dl=0)
    * Employ strategies to identify breakpoints in the contact data. You may draw inspiration from approaches described [here](https://www.dropbox.com/scl/fi/n5bnfnvti7skmoh0atyuo/Crane-et-al._Nature_Condensin-driven-remodelling-of-X-chromosome-topology-during-dosage-compensation.pdf?rlkey=6x3pcj70yuvt7rgxn1k20ubfx&st=te0k2a5r&dl=0) and [here](https://www.dropbox.com/scl/fi/h31erjanerx779v6f10qx/Dixon-et-al._Nature_Topological-domains-in-mammalian-genomes-identified-by-analysis-of-chromatin-interactions.pdf?rlkey=roz282jpfbjth4wxak0fkac60&st=899erhx1&dl=0)
    * Write a python script that will take the contact file as input and return a bed file that will contain contiguous elements (TADs) separated by boundaries
12. **Creating a Suffix Trie from the Suffix Array of a given Sequence**. The idea here is purely algorithmic. Given a DNA sequence, first construct its suffix array and then use it to construct its suffix trie. Use sequences of different complexity to show how the suffix trie size scales with the the complexity of the sequence.
