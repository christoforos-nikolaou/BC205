# BC205: Algorithms for Bioinformatics.

## Exercise. BedTools Applications

In this set of exercises you are asked to **think** of ways, in which you would implement bedTools commands and combinations thereof to perform the following analyses.

1. From a list of chromosomal coordinates, _extract the sequences of the promoters_ of the closest genes, considering as promoter the -5000..+1000bp region from the transcription start site.
2. Calculate the _significance_ of the overlap between two sets of genomic coordinates, assuming the jaccard index as a measure of that overlap.
3. Given a set of genomic coordinates and the coordinates of the same genome's repeated elements, extract the sequences of the initial coordinates that _are not_ part of repeated sequences.