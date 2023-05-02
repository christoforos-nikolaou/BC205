# 3. Use odds-ratio k-mers (k=2) to detect possible (Horizontal Gene Transfer) HGT events in a bacterial genome.
import regex as re
import numpy as np

def kmers(genomefile, k):

    file = open(genomefile, 'r')

    seq = ""
    kmer_table = {} 

    count = 0
    for line in file:
        count +=1
        if (count > 1) :
            length=len(line)
            seq=seq+line[0:length-1]
            
    file.close()

    seq = re.sub("[^AGCT]", "", seq)

    for i in range(len(seq)-k):
        DNA=seq[i:i+k]
        if DNA not in kmer_table.keys():
            kmer_table[DNA]=1
        else:
            kmer_table[DNA]+=1

    kmer_table = {k: v for k, v in kmer_table.items()}

    return(kmer_table)



amount_pairs = kmers('Staaur.fa', 2)

# Calculate the 16-kmer signature frequencies
freq_seq = np.array(list(amount_pairs.values()))

# Calculate mean frequency vector of all possible nucleotide pairs
mean_freq = np.mean(freq_seq)

# Calculate Euclidean distance between signature and mean signature
euclidean_distance = np.sqrt(np.sum((freq_seq - mean_freq)**2))

# Apply Z-transformation to distance
z_distance = (euclidean_distance - mean_freq) / np.std(freq_seq)

print('Euclidean distance with Z-transformation application is',z_distance)