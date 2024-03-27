---
runme:
  id: 01HSFZVBHW1H98RKAA3180G6T8
  version: v3
---

# BC205

## Algorithms in Bioinformatics - MSc in Bioinformatics - University of Crete

This is the git repository on the Course on Algorithms in Bioinformatics (BC205) which forms part of the Program of the Masters in Bionformatics at the University of Crete

**Contact Details**  
*Christoforos Nikolaou: cnikolaou@fleming.gr*  
*web: https://computational-genomics.weebly.com/*  
*twitter: @guilderstern*

## 2023-2024 Academic Year (March-June 2024)

### We will be covering the following topics

__[1. Introduction to Algorithms: Types of Algorithms, Complexity and Iteration vs Recursion](https://nbviewer.org/github/christoforos-nikolaou/BC205/blob/master/Chapter_01_Introduction.html)__  (Mar 14 and Mar 21, 2024)  
a. General Introduction  
b. Concepts: Iteration vs Recursion  
c. Methods: Brute Force vs Divide and Conquer Approaches  
d. Problems: Finding the Largest Common Divisor and Numerical Sort

* Notes and code for the lecture in __pdf__ can be found [here](Chapter_01_Introduction.pdf)
* A -slightly outdated- set of slides can be found [here](https://github.com/christoforos-nikolaou/BC205/blob/master/BC205_Introduction_beamer.pdf)

__[2. Biological Sequence Analysis: Introduction to Bioinformatics Problems. Sequence Composition Analysis](https://nbviewer.jupyter.org/github/christoforos-nikolaou/BC205/blob/master/Chapter_02_Sequence_Analysis.html)__  (Mar 28, 2024)  
a. Why Sequence matters  
b. GC content and Genomic Signatures  
c. Problems: Locating horizontal gene transfer events in bacteria  
d. Problems: Locating the origin of replication in a bacterial genome

* Notes and code for the lecture may be found [here](Chapter_02_Sequence_Analysis.pdf)
* A set of (somewhat obsolete) slides to accompany the lecture may be found [here](BC205_SeqAnalysis_beamer.pdf)

__[Exercise 1](https://github.com/christoforos-nikolaou/BC205/blob/master/Exercise_1.md): Introduction and Sequence Analysis__  
Send your reports by __April 3, 2024__

**[3. Sequence Motifs. Ι](https://sites.google.com/site/uoccomputationalbiology/lectures/03-searching-and-discovering-motifs): Motif Definition and Detection** (Apr 04, 2024)  
a. Motif Definition  
b. Motif Creation  
c. PWMs and PSSMs  
d. Evaluating motifs using Entropy and Information Criteria

* Slides for the lecture (in greek) may be found [here](https://www.google.com/url?q=https%3A%2F%2Fwww.dropbox.com%2Fs%2Fwjs5bcf6vdrn0np%2Fcb_2016_lecture_03_motifs.pdf&sa=D&sntz=1&usg=AFQjCNEkOMAe5b213ffV8k3GniGQvI-8tA)
* A book chapter (in greek) on Motifs and their Description may be found [here](https://repository.kallipos.gr/bitstream/11419/1581/1/Chapter03_seqmotifs_R.pdf)

__[4. Sequence Motifs. ΙI](https://nbviewer.jupyter.org/github/christoforos-nikolaou/BC205/blob/master/Chapter_04_Motif_Discovery.html): Motif Discovery from Sequences__ (Apr 11, 2024)  
a. Motif Discovery Problem  
b. Gibbs Sampling  
c. Complementary approaches

__[Exercise 2](https://github.com/christoforos-nikolaou/BC205/blob/master/Exercise_4.md): Gibbs Sampler__  
Send your reports by __Apr 18, 2024__

__[5. Sequence Alignment](https://nbviewer.jupyter.org/github/christoforos-nikolaou/BC205/blob/master/Chapter_05_Sequence_Comparison.html):  Comparing sequences with pairwise sequence alignment__  (Apr 18, 2024)  
a. Sequence Similarity  
b. Edit distances  
c. Sequence Alignment  
d. Needleman-Wunsch and Smith-Waterman Algorithms  
e. Dynamic Programming

* A book chapter (in greek) on Sequence Alignment (Week 5) and Rapid Searches (Week 6) may be found [here](https://repository.kallipos.gr/bitstream/11419/1582/1/Chapter04_seqalignment_R.pdf)

__[6. Rapid Sequence Searches](https://nbviewer.jupyter.org/github/christoforos-nikolaou/BC205/blob/master/Chapter_06_Rapid_Searches.html):  Quick String-matching algorithms with applications to Genomics__  (Apr 25, 2024)

a. The problem of identical string matching  
b. Approaches that modify the pattern (Knuth-Morris-Pratt Algorithm (KMP), Boyer-Moore Algorithm (BM))  
c. Approaches that modify the pattern and the sequence (Z-Array transformation, Rabin-Karp Algorithm)  
d. FASTA Algorithm  
e. BLAST

* A book chapter (in greek) on Sequence Alignment (Week 5) and Rapid Searches (Week 6) may be found [here](https://repository.kallipos.gr/bitstream/11419/1582/1/Chapter04_seqalignment_R.pdf)
* Slides for the lecture (in greek) may be found [here](https://github.com/christoforos-nikolaou/BC205/blob/master/BC205_RapidSearches_beamer.pdf)

__[Exercise 3](https://github.com/christoforos-nikolaou/BC205/blob/master/Exercise_FASTA.md): Implementation of the FastA algorithm__  
Send your reports by __May 12, 2024__

__[7. NGS Mapping Algorithms](https://github.com/christoforos-nikolaou/BC205/blob/master/BC205_NGSMapping_beamer.pdf) Mapping and Pattern Search in genome-wide NGS-scale experiments__ (May 16, 2024)

a. Identical string matching for millions of sequences  
b. Data Transformation Techniques  
c. Suffix Trees  
d. Burrows-Wheeler Transform (BWT)

__[Exercise 4](https://github.com/christoforos-nikolaou/BC205/blob/master/Exercise_BW.md): Burrows-Wheeler Transformation__  
Send your reports by __June 9th, 2024__

__[8. Genome Analysis Algorithms]() Algorithmic approaches to deal with genomic data__ (May 23, 2024)  
a. Working with genome coordinates  
b. Coordinate overlaps  
c. Smallest distance of genomic segments  
Find a detailed tutorial for BedTools [here](https://bedtools.readthedocs.io/en/latest/content/overview.html)  
A recording of the lecture on BedTools may be found [here](https://www.dropbox.com/s/2pzaezejbh19153/BedTools_31052021.mp4)

__[BedTools Exercises (non obligatory)](https://github.com/christoforos-nikolaou/BC205/blob/master/BedTools_Applications.md): Working with Genomic Coordinates__

__[9. Networks: Introduction to Networks, Statistical and Topological Properties](https://github.com/christoforos-nikolaou/BC205/blob/master/cb_2016_lecture_09_biologicalnetworks.pdf)__ (May 30, 2024)  
a. Introduction. Why are networks important?  
b. Network topology  
c. Statistical Properties of Networks

Find an unpublished Chapter on Network Analysis with R [here](https://github.com/christoforos-nikolaou/BC205/blob/master/Ed2_Chapter17_NetworkAnalysisWithR.html)

__[10. Final Projects: Assignments](https://github.com/christoforos-nikolaou/BC205/blob/master/FinalProjects_2023.md)__ (June 6, 2024)

