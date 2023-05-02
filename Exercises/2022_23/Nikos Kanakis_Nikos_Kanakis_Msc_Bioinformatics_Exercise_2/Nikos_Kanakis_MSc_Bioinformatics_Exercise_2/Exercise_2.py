import regex as re
import numpy as np
import math
import random




def read_fasta(filename):

    with open(filename) as file:
        lines = file.readlines()
        seq = [line.replace("\n","") for line in lines]

    return seq




def find_kmers(seq,k):

# There is a case where the sequence is not a multiple of k. 
# For example seq = ACACT and k = 2 -> kmers = AC, AC, T so I have to consider the last item.
# So I make dummy = AC, AC, T and then I make the list of kmers = AC, AC

    dummy = list(set([seq[i:i+k] for i in range(0, len(seq), k)]))
    kmers = [i for i in dummy if len(i)==k]

    return kmers




# A function to create a PWM from a set of aligned sequences of the same length
def pwm_kmers(sequences,k):

    nuc = ['A', 'C', 'G', 'T']
    profile=[[0.0 for i in range(len(sequences[0]))] for j in range(len(nuc))]
    
    for instance in sequences:
        for j in range(len(instance)):
            residue=instance[j]
            profile[nuc.index(residue)][j]+=1
    
    pwm = np.array(profile)
    pwm = pwm/len(sequences) 
 
    return pwm




def select_rand_kmers(sequences,k):

    rand_kmers = []

    for seq in sequences:
        kmers = find_kmers(seq,k)
        rand_kmers.append(random.choice(kmers))

    return rand_kmers





def scores_pwm(kmers,pwm):

    nuc = ['A', 'C', 'G', 'T']
    scores = [0 for i in kmers]

    for i, kmer in enumerate(kmers):
        for j, nucleotide in enumerate(kmer):
            scores[i] += pwm[nuc.index(nucleotide)][j]

    return scores 




def random_better_scores(scores_1,kmers_1,sequences,pwm,k):
    
    kmers_2 = select_rand_kmers(sequences,k)
    scores_2 = scores_pwm(kmers_2,pwm)

    for i in range(len(scores_1)):
        if scores_1[i]<scores_2[i]:
            kmers_1[i] = kmers_2[i]
            scores_1[i]=scores_2[i]

    return kmers_1,scores_1 
 



### Entropy and Information Content of a PWM

def pwm_Entropy_Information(pwm):
    
    k = pwm.shape[1]

    information = np.zeros([1,k]) #computing the information of each position

    for i in range(k):
        information[0,i] = 2-abs(sum([elem*np.log2(elem) for elem in pwm[:,i] if elem > 0]))
    
    sum_information = np.sum(information)
    mean_information = sum_information/k
    
    return mean_information





def Gibbs(filename,I,k):

    sequences = read_fasta(filename) 
                
    kmers = select_rand_kmers(sequences,k)
    pwm = pwm_kmers(kmers,k)
    scores = scores_pwm(kmers,pwm)
    max_score = pwm_Entropy_Information(pwm)

    while max_score < I:
        
        kmers,scores = random_better_scores(scores,kmers,sequences,pwm,k)
        pwm = pwm_kmers(kmers,k)
        max_score = pwm_Entropy_Information(pwm)

    return pwm,max_score


for k in range(3,8):

    # I put a small threshold to save time from running the code.
    pwm, max_score = Gibbs('motifs_in_sequence.fa', I = 0.2, k=k)
    print(f'For k = {k} and max_score = {max_score} the pwm equals to \n{pwm}.\n')