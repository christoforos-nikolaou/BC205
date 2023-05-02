#Exercise 4: Implement the Gibbs Sampler for motif discovery in the language of your choice (Python)

#Part 1
#1. Implement the Gibbs Sampler in Python  
#2. Use a free parameter for the size k of the motif you will be searching for   
#3. Repeat the search for various values of k (e.g. from k=3 to k=7) 



import numpy as np
import regex as re
import random



#Read the fasta file and save the sequence in a string
file = "./motifs_in_sequence.fa"

def readfile(file):
    with open(file) as f:
        seq = []
        for line in f:
            l = re.match(">", line)
            if l == None:
                seq.append(line.strip())
    return seq

seq = readfile(file)



#Break sequences in list with k-mers per each seq. That will set the pool for the random selection of kmers/seq later
def kmer(seq,k):
    k_mers = []
    for i in seq:
        k_mers.append([i[x:x+k] for x in range(len(i)-k+1)])
    return k_mers



#Construct a PWM function
def pwm(sequences):
    nuc = ['A', 'C', 'G', 'T']
    profile=[[0 for i in range(len(sequences[0]))] for j in range(len(nuc))]
    #
    for instance in sequences:
        for j in range(len(instance)):
            residue=instance[j]
            profile[nuc.index(residue)][j]+=1
            profile[nuc.index(residue)][j]=float(profile[nuc.index(residue)][j])
    pwm = np.array(profile)
    pwm = pwm/len(sequences)
    return(pwm)



#Searching a sequence and calculate the probability of each kmer in that based on the provided PWM
#Here for each kmer I calculate the product of each probability per position and nucleotide and "normalize" it to get a percentage
#of each kmer per sequence
def pwmprobs(pwm, seq):
    nuc = ['A', 'C', 'G', 'T']
    allscores = []   
    for i in range(len(seq)):
        score=1
        instance=seq[i]
        for l in range(len(instance)):
            score *= pwm[nuc.index(instance[l])][l]  
        allscores.append(score)
    allscores = np.array(allscores) 
    allscores /= np.sum(allscores) #convert each kmer's in a percentage
    return(allscores)



#Selection of random a random kmer for each sequence
def kmer_random(kmers_in_seqs):
    random_kmers = [random.sample(y,1)[0] for y in kmers_in_seqs] 
    return (random_kmers)



#Gibbs sampling: Randomly selecting  
def Gibbs(file, k):
    sequences = readfile(file) #Read the data
    kmers_in_seqs = kmer(sequences, k) #Find all kmers per sequence
    random_kmers = kmer_random(kmers_in_seqs)
    rand_pwm = pwm(random_kmers)
    randprobs = pwmprobs(rand_pwm, random_kmers)
    i=0
    new_kmers =[]  
    for kmr in kmers_in_seqs:
        maxprobrand= randprobs[i]
        #Remove the random kmer used to create the PWM so that later I can select the one with min prob without considering the initially randomly used.
        kmr.remove(random_kmers[i])
        #Calculate the prob of the rest kmers. Since the step is equal to the removed seq there should be no problem here.
        prob = list(pwmprobs(rand_pwm, kmr))
        #The best kmer is that with the smallest prob since we multiply the prob per position
        maxprob_new = min(prob)
        #Keeping the kmer with min prob based on the random PWM but without the initially used being considered
        #The indices should be the same in the updated kmr (without the random one) and the prob list
        if maxprob_new >= maxprobrand:
            new_kmers.append(random_kmers[i])
        else:
            new_kmers.append(kmr[prob.index(maxprob_new)])
        i+=1
    rand_pwm = pwm(new_kmers)
    return (rand_pwm)

#Another approach I tested was to simply keep each time the motif with min prob and skip the comparison part:
#for kmr in kmers_in_seqs:
#   prob = list(pwmprobs(rand_pwm, kmr))
#   maxprob_new = min(prob)
#   new_kmers.append(kmr[prob.index(maxprob_new)])



#Part 2
#1. Calculate the Information Content of the discovered PWMs for each k



#The function for calculating the Info content with the Shannon Entropy formula
def pwmEntropyInformation(pwm):
    k = pwm.shape[1]
    information = np.zeros([1,k]) #computing the information of each position
    for i in range(k):
        information[0,i] = 2-abs(sum([elem*np.log2(elem) for elem in pwm[:,i] if elem > 0]))
    sumInfo = np.sum(information)
    scaledSumInfo = sumInfo/k
    return(information, sumInfo, scaledSumInfo)



#Performing Gibbs Sampling for kmers of differenct length until a PWM with Entropy Info>=1.5++
for k in range(3,8):
    while True:
        
        k_pwm = Gibbs(file,k)
        check = pwmEntropyInformation(k_pwm)[2]
        if check >= 1.0:
            result= k_pwm
            print(check,result)
            break



#NOTES:
#Unfortunately the algorythm works ONLY for k=3,4 but not more than. I seperately tested it for k=5,6 and 7 and the code never returned a result
# which means that the check variable could not overpass the I= 1.6++.
#I speculate that the problem is the probability calculation and the selection of the kmer that fits the best the PWM produced
