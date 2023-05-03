# %% Read for the PWM

import numpy as np
import random, re, math
from collections import Counter

# We start of by the given function to read our fasta file. In this case the 50 (l=100) sequences.
def readmultifasta(file):
    import re
    f = open(file, 'r')
    seqs = []
    for line in f:
        x=re.match(">", line)
        if x == None:
            seqs.append(line.rstrip())
    return(seqs)

# Secondly, let's create another function to take random k-mers from each sequence.
def randomizer(all_seq,len_kmer):
# We use 2 variables, 1 for the fasta (or sequences) and 1 for the length of k-mers we are interested    
    random_seq = [] #Initialize an empty list to add all our kmers
    for seq in all_seq:
        k_index = random.randint(0,len(max(all_seq))-len_kmer) #This way it is provided we will take a different random kmer each time from each sequence
        random_seq.append(seq[k_index:k_index+len_kmer])
      
    return random_seq

# Now let's create a function to generate the position weight matrix, as seen from the course.
def pwm_get(sequences): #The input here is sequences or kmers
    nuc = ['A', 'C', 'G', 'T'] #initialize the order of the nucleotides
    profile=[[0 for i in range(len(sequences[0]))] for j in range(len(nuc))]# and create an empty initial profile
    for instance in sequences:
        
        for j in range(len(instance)):
            residue=instance[j]
            if residue == 'N': #I also added this in case we are dealing with unidentified nucleotides and are not using the single string read method
                continue
            profile[nuc.index(residue)][j]+=1
            profile[nuc.index(residue)][j]=float(profile[nuc.index(residue)][j]) #we now fill in the profile depending in the appearance of a nucleotide
    import numpy as np
    pwm = np.array(profile)
    pwm = pwm/len(sequences) #We divide by the length to get a propabilistic type matrix
    return(np.array(pwm))

#  With this function we can now calculate tha information content of a given pwm and consider if we are willing to keep it or not
def EntropyInformation(pwm):
    #We apply the Entropy and Information Content calculation
    import numpy as np
    k = pwm.shape[1] #get the dimensions of our pwm
    information = np.zeros([1,k]) #computing the information of each position. Create row vector with zeros and k columns
    for i in range(k):
        information[0,i] = 2-abs(sum([elem*np.log2(elem) for elem in pwm[:,i] if elem > 0])) #apply Shannon equation
    sumInfo = np.sum(information)
    scaledSumInfo = sumInfo/k
    
    return(information, sumInfo, scaledSumInfo) #Return kmer position specific information content, max information and mean information 


# The idea here is to create a function with 3 variables. Sequences, motif length of interest and the information threshold.
def gibbs(sequences, kmer, threshold):
    
    nuc = ['A', 'C', 'G', 'T'] #Initialize our nucleotide order
    rand_kmers = randomizer(seqs,kmer) #Generate a randomly chosen kmer of specific length from each sequence
    pwm = pwm_get(rand_kmers) #Generate the initial pwm from our randomly chosen motifs
    counts = 0 #Initialize the loop count
    while True:
        info, sum_info, mean_info = EntropyInformation(pwm) #Generate the initial pwm information, maybe we are lucky
        #The above ensures each time we start a repeat we check for the information from the new
        # pwm which is generated at the end of the loop.
        if mean_info >= threshold and counts > 1000: 
            #If we reach our threshold and a number of repeats have occured (just to be sure we can get the maximum information),
            #then it return the list of kmers chosen (used to count them as well, and all the information along with our pwm)
            return (rand_kmers, info, sum_info, mean_info, pwm)
        
        #print(mean_info, end = f' At {counts} counts\n') #With this we can view how the information changes as the repeats go
        
        seq_dict = {} #This dictionary will be used to store the ifnormation of the current kmer of each sequence and compare it with the new
        all_scores = [] #This list will store the candidate kmer with their maximum score, 1 per sequence
        init_index = 0 #The index for the random kmer list in order to replace the old motif with the new

        for k in sequences: #Take each of the sequences
            score_init = 0 #Initialize the score of the current motif list
            
            for l_init in range(len(rand_kmers[score_init])):
                score_init += pwm[nuc.index(rand_kmers[init_index][l_init])][l_init] #Calculate based on the PWM the score of the motif of the current sequence

            seq_dict[k] = score_init #Add the above-calculated score to the sequence

            for i in range(len(k)-kmer+1): #Read all the sequence at length = motif length, at intervals of 1 
                instance = k[i:i+kmer] #Create each motif of the sequence
                score = 0 #Initialize the score of the current motif of the sequence
            
                for l in range(len(instance)):
                    score += pwm[nuc.index(instance[l])][l] #Calculate again based on the PWM currently generated the score of the current motif
                
                inst_score = (instance,score) #Make a tupple of the motif and its score (useful for indexing)
                all_scores.append(inst_score) #and append the tupple to the list
            
            max_instance, max_score = max(all_scores, key = lambda x: x[1]) #Find the maximum score from the list of tupples and return it along with the motif
                
            if max_score >= seq_dict[k]: #I am note sure if i should use = here, since in my mind it might change it alot since we are having multiple max score hits.
            #if max_score > seq_dict[k]:#I chose without equal but maybe both implementations work
                seq_dict[k] = max_score #Now we change the current maximum score of the sequence
                del rand_kmers[init_index] #Remove the motif from our motif list
                rand_kmers.insert(init_index, max_instance) #And replace it with the new motif that had the maximum score
            
            
            
            if counts == 10_000: #In case it gets stuck and cannot go above the certain thershold level, works like a failsafe
                #print(f'Stopped after {counts} counts')
                return (rand_kmers, info, sum_info, mean_info, pwm)
            
            init_index += 1 #Add 1 to the motif list index 
            counts += 1 #and to the repeats
            
        pwm = pwm_get(rand_kmers) #calculate the new pwm based on our current motif list

seqs = readmultifasta("ex2_motifs.fa") #The sequences to be evaluated
motifs = list(range(3,8)) #Create a list with the different motif lengths we are interested in


# %%
# Since i was getting different results alot of time all of which were with high information content,
# i thought maybe i could approach it by doing multiple repeats for each of the kmer, and summing those
# in a new array which will show if there is a most preferred pattern among all those patterns.

summed_list = []

for km in motifs:
    print(f'___Starting search for morif with length = {km}___\n')
    np_sum = np.zeros([4,km]) #re-create a matrix to sum the results of the gibbs and see if at many repeats there is a more clear pattern
    for i in range(50): #We choose how many repeats we want to do for verification
        k_dict = {} #Initialize an empty dictionary to append the results of our gibbs search
        k_dict[km] = gibbs(seqs, km, 1.85) #I left it to 2 so it can run to its fullest and see any changes in results
        np_sum += k_dict[km][4]
        print(f'These are the motifs found: {sorted(dict(Counter(k_dict[km][0])).items(), key = lambda x:x[1],reverse = True)}')
        # The Counter will show as each run goes on the motif chosen and how many times it was found, this could also be summed in a list and check overall motif preferred,
        # although it seems that for k = 3 and k = 4 more randomness is present and many of those motifs seems to exist in all sequences
        print(f'The mean information when kmer length is {km}: {k_dict[km][3]} and the PWM is: \n\n {k_dict[km][4]} \n')
    print(f'>>>>>>>>The summed matrix is<<<<<<<<<<\n\n{np_sum}') #Return the summed matrix to check if there is a pattern within the different gibbs patterns
    summed_list.append(np_sum) #Append each summed result to a list
    print(f'\n========= END OF MOTIF SEARCH (l={km})\n')


# %% We can check all the summed matrixes here to see for a more distinct pattern.
#With this approach i tried to repeat 3 different 100 gibbs functions for each kmer length, and see if there is a pattern.
#Then i divided the matrix by 100 to get a percentile type matrix.
#With my function there does not seem to be a very distinct motif, yet almost all the information content is above 1.9 as mentioned.
for j in range(3):
    
    summed_list = []
    for km in motifs:

        np_sum = np.zeros([4,km]) #re-create a matrix to sum the results of the gibbs and see if at many repeats there is a more clear pattern
        for i in range(100): #We choose how many repeats we want to do for verification
            k_dict = {} #Initialize an empty dictionary to append the results of our gibbs search
            k_dict[km] = gibbs(seqs, km, 1.85) #I left it to 2 so it can run to its fullest and see any changes in results
            np_sum += k_dict[km][4]
        summed_list.append(np_sum/100) #Append each summed result to a list


    for i in summed_list:
        print(f'{i}\n')

#A sample of a run of the above loop can be seen in GibbsRepeats.results


# Overall i think i have done mistakes regarding how the pwm is formed since like mentioned i keep seeing alot of different motifs from each run
# all of them having high information content with different type of motifs each time. Also i dont think i should be getting information = 2 at 
# most of the lower length motifs. I also tried this approach without using the max of the score but doing instant replacements, which seemed to take a longer time.
# I did try to approach it by using the pssm as well, but i was getting very low information which did not make sense.


# %% PSSM APPROCH (as metnioned above)
# This is my pssm approach which did not work. The idea is exactly the same only this time we are using the
# pssm to calculate scores instead of the pwm. Low information content generated from the pssm.
# Even though i used pssm to calculate score i chose to return the pwm.
# The only thing different concerning the function is an added fourth variable that is the nucleotide frequences
import re
import numpy as np
import math

def readfasta(fastafile):
    
    f=open(fastafile, 'r')
    seq = ""
    total = 0
    for line in f:
        x=re.match(">", line)
        if x == None:
            length=len(line)
            total=total+length
            seq=seq+line[0:length-1]
    seq=seq.replace('N','')
    f.close()
    return(seq)

def nuccomp(sequence):
    nucfreq = [0, 0, 0, 0]
    nuc = ['A', 'C', 'G', 'T']
    for i in range(len(nuc)):
        nucfreq[i]=sequence.count(nuc[i])
    nucfreq=np.array(nucfreq)/len(sequence)
    return(nucfreq)


def pssm_get(pwm, nucfreqs):
    import numpy as np
    import math
    pseudocount=0.01
    pssm=[[0 for i in range(len(pwm[0]))] for j in range(len(nucfreqs))]
    for i in range(len(nucfreqs)):
        pssm[i]=(np.array(pwm[i])+pseudocount)/nucfreqs[i]
    for i in range(len(pssm)):
        for k in range(len(pssm[0])):
            pssm[i][k]=math.log(pssm[i][k])/math.log(2)
    return(np.array(pssm))


def gibbs(sequences, kmer, threshold, nuc_frequency):
    
    nuc = ['A', 'C', 'G', 'T']
    rand_kmers = randomizer(seqs,kmer)
    pwm = pwm_get(rand_kmers)
    pssm = pssm_get(pwm, nuc_frequency)
    counts = 0
    while True:

        info, sum_info, mean_info = EntropyInformation(pssm)
        if mean_info >= threshold and counts > 1000:
            return (rand_kmers, info, sum_info, mean_info, pwm)
        
        seq_dict = {}
        all_scores = []
        init_index = 0
        


        for k in sequences:
            score_init = 0    
            
            for l_init in range(len(rand_kmers[score_init])):
                score_init += pssm[nuc.index(rand_kmers[init_index][l_init])][l_init]

            seq_dict[k] = score_init

            for i in range(len(k)-kmer+1):
                instance = k[i:i+kmer]
                score = 0
            
                for l in range(len(instance)):
                    score += pssm[nuc.index(instance[l])][l]
                
                inst_score = (instance,score)
                all_scores.append(inst_score) 
            
            max_instance, max_score = max(all_scores, key = lambda x: x[1])
                
            if max_score > seq_dict[k]:
                seq_dict[k] = max_score
                del rand_kmers[init_index]
                rand_kmers.insert(init_index, max_instance)
            
            init_index += 1
            counts += 1
            
            if counts >= 20_000:
                print(f'Stopped after {counts} counts')
                return (rand_kmers, info, sum_info, mean_info, pwm)
        
        pwm = pwm_get(rand_kmers)
        pssm = pssm_get(pwm, nuc_frequency)

seq_string=readfasta("ex2_motifs.fa")
nucs = nuccomp(seq_string)

seqs = readmultifasta("ex2_motifs.fa")
motifs = list(range(4,8))


# %% 
# Try with the log of the pwm for the nucleotide divided by the log of the expected --> log(pwm[A]/pssm[A])