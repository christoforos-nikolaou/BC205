## Final Projects (June 2025)

Below you may find a list of suggested topics for your final project in our class.
Some of the topics are described in brief and without further details.
They will be further elaborated once they are assigned to people (or groups).

The **deadline** for handing in your projects is **Sunday July 13th, 2025**.

---
1. **Maximal coverage of valued elements**. (Genomics, Epigenomics)  
   **Background**: Very often in the fields of genomics and epigenomics we are dealing with a set of genomic coordinates of segments defined through an experimental protocol that we wish to map on the genome in an objective way. Such segments may be overlapping regions of different TF-binding sites or nucleosome positions. In this project, you are asked to provide a strategy to distribute a subset of non-overlapping genomic segments, starting from a bigger set of overlapping ones, using a pre-assigned score/value to each one.   
   **Details**:  
   Given: a) the total length of a genome (or a chromosome) and b) a set of _overlapping_ segment coordinates from that genome, where each segment is assigned a value(score). Find the set of non-overlapping segments that maximizes the sum of values(scores) for the given genome.
   You are asked to:

   * Obtain [this file](https://www.dropbox.com/scl/fi/t1uvn8xfwavlo6jmt1cx1/sacCer3_chrIV_nucs_overlapping.bed?dl=0&rlkey=vuyfn519sqsp3wnns89nsdlal) which contains overlapping predictions for the positions of >80k nucleosomes in the chromosome IV of S. cerevisiae.
   * Devise a strategy according to which the coordinate segments in the file (that means each row in the file) will be considered on the basis of their score (given in the 4th column)
   * The output should be a **subset** of the original files that will contain the maximum number of non-overlapping segments that sum up to the highest overall score.
   * You can try to compare a greedy approach, with a dynamic programming approach **(BUT! stay away from Brute Force)**
   * Provide the python code that will take the above file as input and return a similar set of non-overlapping coordinates.

---

2. **Use the BWT to compress a given sequence**. (Algorithm/Software Development)  
   **Background**: We have already discussed the Burrows-Wheeler Transform and how it could assist in the compression of a sequence. 
   **Details**:
   You are asked to:  
   * Write the code that will take a sequence of any type (you may choose your own) and create the BWT.
   * Use the BWT to compress the sequence in a meaningful way. One such is through Run-Length Encoding, a simple approach that consists of replacing a string of same character strings with its multiple (e.g. AAAAA becomes A5).
   * The code should be reversable, meaning it should also contain the reversal of the compressed string into the original sequence.
  
---

3. **Comparing genome segmentations**. (Genomics)  
   **Background**: One very common problem we have to deal with, while handling genomics data is to estimate and statistically assess the overlap between two sets of genomic coordinates. Suppose you have the same experiment conducted twice for the identification of the genome-wide binding sites of a given TF. How can you say if the experiments are in agreement or not? The idea here is to propose ways to quantitatively compare two (or more) different segmentations of a linear series (such as genomes or chromosomes). You should find a way to calculate how similar the two patterns are. You may be inspired by the bedtools **intersect** function.
   **Details**:
   * Take the two coordinate files you will find in the following links as [coord file 1](https://www.dropbox.com/scl/fi/8f6bngwk79ndlqtdi681k/NewRun_MAC1_t4.bed?rlkey=bwqugj7tujm0rkl9la7nqewho&st=0o31va86&dl=0) and [coord file 2](https://www.dropbox.com/scl/fi/sffd3acvrulg40jvce8z3/NewRun_AFT1_t4.bed?rlkey=f43phaxa0tc4ye4l61bytrgz8&st=c4ljukhs&dl=0)
   * Think of a strategy to calculate the degree of overlap between the two coordinate files.
   * How big or small is it? How can it be compared against a null model?
   * Can you think of a way to score the overlap and assess its statistical significance?
   * Provide a script for all of the above.

---

4. **Aggregate values of a given score for genomic intervals**. (Genomics, Data Analaysis)  
   **Background**: The idea here is rather simple. You are given two files. One is a bed-type genomic coordinate file and the other contains a compressed-type chromosome-position-score, where the score is a nucleotide-specific score.   
**Details**: You are asked to:  
   * Get the genome coordinate file which you will obtain from [here](https://www.dropbox.com/scl/fi/6fc8stk76dg2vm93p85pn/saccer2_refseq_genes_TSS_plusmin500.bed?dl=0&rlkey=x9expw5ae08odk1fiyzcfp1ct) and which contains 1000bp-long regions from the yeast genome centered around the transcription start sites of all yeast protein coding genes.
   * Get the genome score file that you will obtain from [here](https://www.dropbox.com/scl/fi/ordt8x4lh325nln6cel8w/sacCer2_phCons.wig?dl=0&rlkey=6a5ay1t02fqhe70w88puv0kq8) which contains a nucleotide-resolution score that corresponds to the degree of sequence conservation for the entire yeast genome. The file format is wig type (see more about how to interpret this format [here](https://www.ensembl.org/info/website/upload/wig.html#:~:text=A%20WIG%20file%20consists%20of,formatting%20options%3A%20fixedStep%20and%20variableStep))
   * Write a program that will take the scores of the second file and aggregate them along the coordinates of the first to produce a new bed-type file with chromosome-start-end followed by an aggregate value of the interval. Allow the aggregate value to be chosen between sum, mean, standard deviation, maximum or minimum. 
  
---

5. **Implement a Predator-Prey Dynamic Modeling on a bacterial community**. (Dynamic Systems)    
   **Background**: The Lotka–Volterra equations, also known as the Lotka–Volterra predator–prey model, are a pair of first-order nonlinear differential equations, frequently used to describe the dynamics of biological systems in which two species interact, one as a predator and the other as prey.   
   **Details**: In this project you will be tasked with both obtaining the test data and implementing the model.   
    * You are asked to check [MGnify](https://www.ebi.ac.uk/metagenomics) the metagenomics database of EBI and obtain time-series data with at least two different species with a predator-prey relationship (e.g, Predator: Bdellovibrio bacteriovorus, Prey: Escherichia coli). The data need to be time-series so that you have the necessary data points to test the model.    
    * Next, you will need to implement the Lotka-Volterra system of equations (see [here](https://mathworld.wolfram.com/Lotka-VolterraEquations.html)) on the data and identify the most likely parameters of the model. You may check [here](https://github.com/christoforos-nikolaou/BC205/blob/figures/LotkaVolterra.png) for some notation on the parameters you are asked to estimate.  
    * Provide the code and relevant plots related to your models.

---

6.  **Creating a Suffix Trie from the Suffix Array of a given Sequence**. (Algorithms, Sequence Analysis)  
    **Details**: The idea here is purely algorithmic. Given a DNA sequence, first construct its suffix array and then use it to construct its suffix trie. Use sequences of different complexity to show how the suffix trie size scales with the the complexity of the sequence.

---

7. **Identifying ultra-conserved non-coding sequences in the human genome** (Evolutionary Genomics)  
   **Background**: Ultra-conserved non-coding sequences (UCNS) are regions of DNA that have been remarkably well-preserved across different species during evolution, even though they don't code for proteins. These sequences are particularly notable for their high degree of conservation, often exceeding what's seen in protein-coding regions.  
   **Details**: You are asked to:  
   * obtain conservation data from multiple vertebrate species from the [UCSC Table Browser](https://genome.ucsc.edu/cgi-bin/hgTables). You may restrict your data acquisition for one chromosome.   
   * Propose ways to scan the data to identify UCNS. Think of a strategy that will require some arbitrary criteria on minimum length and mean conservation. Also think of ways to distinguish the UCNS from actual protein coding (or other coding) sequences. Could you do this without relying on the annotation of coding sequences?  
   * Provide the code and the results in a way that can be evaluated (number of identified segments, statistics on lengths, conservation, distance from known genes etc)  

---

8. **Estimating the complexity of a DNA sequence** (Algorithms, Sequence Analysis)  
   **Background**: The concept of DNA sequence complexity lies at the heart of a number of applications related to the identification of repeats, the estimation of coding potential and automatic coding sequence annotation. The idea here is to propose an algorithm that will quantitatively evaluate the degree of complexity (or, on the other hand, simplicity) of a given sequence.   
   **Details**: You are asked to:  
   * implement an approach to assess sequence complexity based on the Kolmogorov "algorithmic complexity" as described by G. Chaitin, which basically calculates a product of the ratios of observed/maximal numbers of different k-mers in a sequence. See more [here](https://resources.qiagenbioinformatics.com/manuals/clccancerresearchworkbench/200/index.php?manual=How_sequence_complexity_is_calculated.html)  
   * the code for this type of analysis in python  
   * an analysis of sliding window complexity scores along a natural sequence. After choosing a complete chromosome of a given organism, you should calculate the complexity of sequences of a given length (e.g. 1000 nucleotides) for the entire length. As a bonus you may compare the data that you obtain against annotated elements of the genome (repeats vs coding sequences etc). The idea is to provide some proof that your approach does indeed pick up low/high complexity regions in the genome.  

   ---


