# Exercise 1.3
# Ioannis-Rafail Tzonevrakis
from collections import Counter
from typing import Iterable
from numpy.typing import ArrayLike
from warnings import warn
from math import prod
from collections import defaultdict
import numpy as np


class Sequence:
    """A class for manipulating sequences, accessed via a FASTA file stored
       on the user's disk drive.

       Please note that, for the sake of avoiding over-engineering beyond the
       assignment's requirements, the methods in this class assume
       only one sequence is present in the input FASTA file."""

    def __init__(self, fasta_path: str) -> None:
        """Initialize the Sequence class.
           Parameters:
                * fasta_path: Path to the FASTA file containing the
                              sequence.
        """
        self.fasta_path = fasta_path
        # Create a null property to store the base frequencies in, if computed
        self.base_freqs = None

    def get_windowed_oe_ratio_d2_zscores(self, size: int, pct_overlap: float,
                                         k: int) -> ArrayLike:
        """Computes the observed-over-expected kmer frequency ratio for all k-mers
           over the entire sequence, then proceeds to compute the same metric across
           all overlapping windows of a specified length over the sequence, and the
           Euclidean distance between the overall and window-specific metrics.
           All Euclidean distances are then Z-transformed and returned to the user.
           Parameters:
               * size: Overlapping window length
               * pct_overlap: Percentage overlap between adjacent windows
               * k: k-mer length to use for metric calculation
           Returns:
               A numpy array, containing the Z-transformed Euclidean distances.
           """
        def euclidean_distance(d1, d2):
            # Euclidean distance helper function (square root of sum of squares)
            # To avoid computing terms twice with no reason, get the union of the
            # sets of the keys of the two dictionaries
            # NOTE: We've made sure that both input dictionaries are defaultdicts
            # with a default return value of zero, so that terms which only exist
            # in one of the two dictionaries are computed properly
            return sum((d1[v]-d2[v])**2 for v in set(d1.keys()).union(set(d2.keys())))**0.5
        # Get the observed-over-expected-normalized kmer frequencies for the entire sequence
        overall_oe_kmers = self.get_oe_kmers(self.count_kmers(k=k))
        # Get an iterator over the kmer counts of the overlapping windows
        window_kmer_iterator = self.windowed_kmer_count(window_size=size,
                                                        pct_overlap=pct_overlap,
                                                        k=k)
        # Compute the Euclidean distance between the overall and window
        # observed-over-expected-normalized k-mer frequencies
        distances = np.array([euclidean_distance(overall_oe_kmers,
                                                 self.get_oe_kmers(i)) for i in window_kmer_iterator])
        # Z-score normalize distances
        distances = (distances-distances.mean())/distances.std()
        return distances

    def get_windowed_gc_content_zscores(self, size: int, pct_overlap: float) -> ArrayLike:
        """Computes the z-scored of the z-scores of the GC-content of partially-overlapping
           windows.
           Parameters:
               size: Window size to iterate over
               pct_overlap: Percentage by which consecutive windows will overlap
           Returns:
               A numpy array, containing the z-scores over each window."""
        # Compute GC content over each window
        rv = np.array([(w.count('C')+w.count('G'))/size for w in
                       self.overlapping_window_view(size=size, pct_overlap=pct_overlap)])
        # Return Z-scores of GC content
        return (rv-rv.mean())/rv.std()

    def get_base_freqs(self) -> None:
        """Compute the nucleotide (base) frequencies across the entire sequence."""
        if self.base_freqs is not None:
            warn('Overwriting currently computed base frequencies')
        self.base_freqs = Counter()
        with open(self.fasta_path) as fp:
            for l in fp:
                if l[0] == '>':
                    continue
                # Count the characters in the current line (after converting them to
                # uppercase to avoid counting 'a' and 'A' as separate entities and
                # stripping of newlines), then add that result to the class'
                # base frequency counter; Also update total character count
                ls = l.strip()
                self.base_freqs += Counter(ls.upper())
        # Get the total sequence length by the sum of all counts
        total_length = sum(self.base_freqs.values())
        # Compute the actual frequencies by dividing the counts by the total sequence length
        self.base_freqs = {k: self.base_freqs[k]/total_length for k in self.base_freqs.keys()}

    def overlapping_window_view(self, size: int, pct_overlap: float) -> Iterable:
        """Get an iterator over partially-overlapping windows across a sequence.
           Parameters:
               size: Window length
               pct_overlap: Percentage overlap of adjacent windows
           Returns:
               A generator, that may be iterated through to get the next
               overlapping window."""
        # Initialize circular buffer
        substr = ''
        # Part of the sequence to delete every time the buffer fills:
        # Since we want some degree of overlap, we won't be removing the entire contents,
        # rather some percentage of the oldest contents, that is determined by the
        # pct_overlap parameter:
        if pct_overlap == 0:
            del_size = size
        else:
            del_size = int(size*pct_overlap)
        with open(self.fasta_path) as fp:
            for l in fp:
                if l[0] == '>':
                    # Skip headers
                    continue
                # Strip the file line of newlines, extraneous spaces, etc
                ls = l.strip()
                for c in ls:
                    if c not in 'ACGT':
                        # Ignore uncertain base characters
                        # (lower-case bases or N)
                        continue
                    # Iterate over the line (character-by-character), add each character
                    # to the cyclical buffer until it fills up
                    substr += c
                    if len(substr) < size:
                        continue
                    # Buffer is full, yield it to whoever is iterating us
                    yield substr
                    # Remove the oldest part of the circular buffer, based on the
                    # desired percent overlap
                    substr = substr[del_size:]
            # We don't have anything else to iterate over, yield the final windows, where
            # the length is not necessary equal to the desired window size:
            for i in range(len(substr) // del_size):
                yield substr[i*del_size:]

    def windowed_kmer_count(self, window_size: int, pct_overlap: float, k: int) -> Iterable:
        """Count the kmers within overlapping windows across the sequence.
           Parameters:
               window_size: Overlapping window size
               pct_overlap: Consecutive window overlap percentage
               k: length of k-mers to get
           Returns:
               A generator that iterates through dictionaries containing the count
               of the unique k-mers in each overlapping window"""
        # Get an overlapping window iterator over the sequence
        wv = self.overlapping_window_view(size=window_size, pct_overlap=pct_overlap)
        for window in wv:
            # Iterate through the window, counting the distinct k-mers
            #
            # We don't use a circular buffer here since the window is
            # already stored in memory, and thus there's nothing to load; As
            # such, no memory savings would be experienced by using a different
            # data structure.
            #
            # The end of the range is +1 to be able to get all k-mers
            # in small sequences; For example, the 2-mers of 'GAT' should be
            # 'GA' and 'AT', not just 'GA'.
            yield Counter((window[i:i+k] for i in range(0, len(window)-k+1)))

    def get_oe_kmers(self, kmer_counts) -> dict:
        """Transform a kmer counts dictionary, as returned by count_kmers,
           by its observed-to-expected frequency ratio.
           Parameters:
               kmer_counts: The counts dictionary to transform. All k-mers in
                            the dictionary should have the same length
           Returns:
               A dictionary, containing the counts transformed by their
               observed-to-expected frequency"""
        if self.base_freqs is None:
            # Base frequencies have not been computed yet, compute them.
            self.get_base_freqs()
        # All k-mers in the input dict should have the same length; Therefore,
        # we can get the k-mer length without explicitly requesting it from
        # the caller by computing the length of the first dictionary key
        k = len(list(kmer_counts.keys())[0])
        # If we're working with k-mers, we've iterated over length-k of the
        # string. Therefore, the total sequence length would equal the sum
        # of all k-mer counts + k + 1.
        total_length = sum(kmer_counts.values())+k-1
        # Return the transformed k-mer counts as a dictionary
        # Transformation details: The k-mer counts are normalized by the total length
        # of their source string (yielding the observed frequency), and then divided
        # by the product of the sequence frequencies (expected frequency)
        rv = {k: (kmer_counts[k]/total_length)/prod([self.base_freqs[j] for j in k]) for k in kmer_counts.keys()}
        # Return a defaultdict with a default of zero, so that
        # a frequency of zero is assumed if a k-mer has not been observed
        # in a specific sequence when computing distances.
        return defaultdict(lambda: 0, rv)

    def kmer_iterator(self, k: int) -> Iterable:
        """Create an iterator over the k-mers of the sequence.
           Parameters:
                * k: Length of k-mers to consider.
           Output:
                * A generator, that iterates over the k-mers in the sequence."""
        # Avoid reading the entire file into memory; Create instead
        # a circular buffer which will store our substring
        substr = ''

        with open(self.fasta_path) as fp:
            for l in fp:
                if l[0] == '>':
                    # Line is a header, skip
                    continue
                ls = l.strip()
                for c in ls:
                    if c not in 'ACGT':
                        # Ignore uncertain base characters
                        # (lower-case bases or N)
                        continue
                    substr += c
                    if len(substr) < k:
                        continue
                    # Our buffer is full, yield substring (-> k-mer)
                    yield substr
                    # We are back from the yield (next has been called); Remove the
                    # oldest data (first character) from the circular buffer before
                    # continuing iterating:
                    substr = substr[1:]

    def count_kmers(self, k: int) -> Counter:
        """Count the sequence's distinct k-mers.
           Parameters:
                * k: Length of k-mer to consider.
           Output:
                * A Counter dictionary, representing the count of appearences
                  (value) of each distinct k-mer (key)."""
        # Return a Counter which uses our kmer_iterator function as input:
        kmers = self.kmer_iterator(k=k)
        return Counter(kmers)


