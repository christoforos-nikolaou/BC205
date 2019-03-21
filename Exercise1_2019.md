# Option 1: Compare Genome Sequences with k-mer frequency tables accounting for background composition

- Task 1: Obtain the first chromosome from the genomes of the following organisms: 
(*H. sapiens, M. musculus, R. norvegicus, D. melanogaster, C. elegans and S. cerevisiae*). The sequences need to be in fasta format or similar.
You may use the database of your choice but you are advised to opt for the [UCSC Table Browser](https://genome.ucsc.edu/cgi-bin/hgTables).
- Task 2: Calculate a table of o/e 2-mer frequencies for a given sequence. Use mononucleotide frequencies as background. 
- Task 3: Calculate the Manhattan distance of the k-mer frequency for all sequence pairs
- Task 4: Return a table with the Manhattan distances alongside your code and a brief discussion of your results. 
Does the Distance table correspond to what you would expect in terms of distances between the species?

# Option 2: Detect regions of extreme nucleotide composition in a given sequence

- Task 1: Download the genome of *Legionella pneumophila* from the database of your choice. Any strain will do
- Task 2: Use a sliding window approach with a window size of adequate length and calculate a table of o/e 2-mer frequencies for a given sequence. Use mononucleotide frequencies as background (See Task 2 above). Adequate length of window should be adjusted bearing in mind the k-mer size.
- Task 3: Calculate a mean o/e k-mer frequency table for the whole genome to use as reference
- Task 4: Calculate the Manhattan distance of the k-mer frequency for all positions in the genome
- Task 5: Calculate mean and sd values of the distances (d) and report the regions that fall our of 2-standard-deviations.



