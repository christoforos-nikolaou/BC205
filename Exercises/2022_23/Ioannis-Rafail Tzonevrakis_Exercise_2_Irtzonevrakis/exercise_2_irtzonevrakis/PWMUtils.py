# PWMUtils.py
# Purpose: Gibbs sampler and utilities for handling PWMs
# Author: Ioannis-Rafail Tzonevrakis

import numpy as np
from numpy.typing import ArrayLike
from collections import Counter
import random

class PWM:
    def __init__(self, sequences: list):
        """Gets a PWM based on the input sequences.
           Parameters:
                   * sequences: A list of sequences to process
        """

        # Store the input sequences
        self.sequences = sequences

        # Initialize empty counters
        pwm = [Counter() for i in range(len(sequences[0]))]
        # Count bases
        for seq in sequences:
            for i, c in enumerate(seq):
                pwm[i][c] += 1
        # Create PWM: Ensure the correct ordering (hence the specific indexing),
        # and divide by sequence length
        self.pwm = np.array([[x[i] for i in 'ACGT'] for x in pwm]).T / len(sequences)

    def get_entropy(self) -> tuple[ArrayLike, ArrayLike, ArrayLike]:
        """Get the entropy of a motif.
           Returns:
               * A tuple of three arrays, the first containing the contribution of
                 the individual positions on the total entropy, the second containing
                 the total information in the PWM, and the third one the information
                 content, scaled by motif length."""
        # Get information content: For each position, the maximum possible entropy is 2:
        # 1 possible position to complete randomness (p_{expected} = 1/4) =>
        # log2(1/(1/4)) = 2.
        # Also, the total entropy of a PWM is given by the sum of the
        # product of the probability of each position by the log2 of
        # said probability. Here, we implement this using the sum
        # of a masked logarithm; All invalid values are masked and
        # filled with zeroes, so that they don't contribute ot the toal
        # sum.
        information = 2-np.abs(np.sum(self.pwm*np.ma.log2(self.pwm).filled(0), axis=0))
        # Sum the information content
        sum_information = np.sum(information)
        # Scale
        sum_information_scaled = sum_information/self.pwm.shape[1]
        # Return
        return information, sum_information, sum_information_scaled

    def get_max_score(self) -> float:
        """Gets the maximum possible score of the current PWM"""
        return np.sum(np.max(self.pwm, axis=0))

    def score_sequence(self, seq) -> float:
        """Scores a sequence with the current PWM.
           Parameters:
               seq: Sequence to score
           Returns:
               The score."""
        # A dictionary that maps nucleotides to PWM indices
        lut = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        if len(seq) != self.pwm.shape[1]:
            # Sanity check!
            raise ValueError(f"The given sequence's length differs from the motif length ({len(seq)} != {self.pwm.shape[1]})")
        # Return the score
        return sum(self.pwm[lut[c], i] for i, c in enumerate(seq))


def gibbs_sampler(sequences: list, k: int, thres: float, maxit=1000) -> PWM:
    """Gibbs sampler for motif discovery
       Parameters:
           * sequences: List of sequences to sample from
           * k: Motif length
           * thres: Entropy threshold to stop search at
           * maxit: Maximum number of iterations
       Returns:
           * The found PWM"""
    kmers = []

    # Cache all unique k-mers for all sequences:
    for seq in sequences:
        kset = list(set([seq[i:i+k] for i in range(0, len(seq)-k+1)]))
        kmers.append(kset)

    # Sample a random k-mer from each sequence:
    pwm_kmers = [random.choice(x) for x in kmers]
    # Create a PWM out of the sampled k-mers
    pwm = PWM(pwm_kmers)
    # Get the PWMs total information content
    score = pwm.get_entropy()[1]
    # Initialize iteration counter
    ic = 0
    # Until we reach the threshold, or have exceeded our iteration count,
    # repeat:
    while (score < thres) and (ic < maxit):
        # For each sequence, iterate through all possible k-mers and score
        # them, finding the one with the best score. Then, replace the sampled
        # sequence with the one with the best score:
        pwm_kmers = [max([[x, pwm.score_sequence(x)] for x in km],
                         key=lambda x: x[1])[0] for km in kmers]
        # Compute a new PWM with the sampled k-mers and get its total
        # information content
        pwm = PWM(pwm_kmers)
        score = pwm.get_entropy()[1]
        ic += 1
    # Return the PWM we found
    return pwm
