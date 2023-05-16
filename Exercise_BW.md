# BC205: Algorithms for Bioinformatics.

## Exercise IV. Burrows-Wheeler Transformation

This exercise is split in two parts and will be performed with a partner. You will not work in pairs but you need a pair. 
Each pair A,B will work in the following way:

1. Member A will browse Uniprot (https://www.uniprot.org/) for a protein sequence of his/her choice. Then:
  a. He/She will obtain the Protein Accession Number and the fasta sequence of the protein 
  b. Will use the BWT to transform it using the dollar ($) sign for terminal symbol. $ will have top priority in sorting.
  c. He/She will send the **BWT Transform of the sequence** to member B.
 
2. Member B will have to:
  a. Implement the BWT reversal (decoding) algorithm to find the actual sequence A sent him/her
  b. BLAST it against uniprot (with Protein BLAST) and identify the accession number 
 
  
Once this is complete (or the deadline has arrived) A will send me the Accession Number and Fasta sequence of the protein 
and B will send me the Accession Number he/she identified. Both will also send me the code. 
Please do so independently even if you have cross-compared your results.
