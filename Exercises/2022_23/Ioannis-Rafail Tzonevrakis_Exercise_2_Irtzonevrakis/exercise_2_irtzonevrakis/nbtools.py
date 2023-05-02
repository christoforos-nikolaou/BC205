# nbtools.py
# Purpose: Multiple starting configuration Gibbs sampler
#          (Workaround for iPython limitation)
# Author: Ioannis-Rafail Tzonevrakis

from PWMUtils import gibbs_sampler

def multiseed_gibbs(k:int, n:int, sequences: list) -> list:
    """Multiple starting configuration Gibbs sampler.
       This function has been defined in a separate file rather than within
       the Jupyter notebook because a bug in iPython prevents proper use
       of multiprocessing with notebooks defined within the notebook
       environment. For details, see:

       https://stackoverflow.com/questions/41385708/multiprocessing-example-giving-attributeerror

       Parameters:
           * k: Motif length
           * n: Number of repetitions
           * sequences: Input sequences
       Returns:
           * A list of the returned PWMs
       """
    # Define a threshold, some amount below the theoretical maximum; If it's
    # unachievable, the default iteration limit of 1000 is going to kick in
    thres = 2*k-0.6
    return [gibbs_sampler(sequences=sequences, thres=thres, k=k) for i in range(n)]

