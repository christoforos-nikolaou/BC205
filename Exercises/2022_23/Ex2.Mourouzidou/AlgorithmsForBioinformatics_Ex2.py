import random

#define a function that will take th filename as an input and return a list of all the sequences in it
def load_sequence(filename):
    with open(filename) as f:
        #initialize an empty list
        seq = []
        #append every sequence in this list without \n
        for l in f:
            seq.append(l.strip())
    return seq

#print(load_sequence('motifs_in_sequence.fa'))


def gibbs_sampler_pwm(sequences, k):
    motifs = []
    for seq in sequences:
        #choose a nucleotide position as the starting point of the motif
        start = random.randint(0, len(seq)-k)
        #extract a substring motif of length k of the sequence with a random starting point
        motif = seq[start:start+k]
        motifs.append(motif)

    best_motifs = motifs.copy()
    while True:
        prof_matrix = []
        #iterate over a loop of number equal to all the possible positions of the k-mers
        for pos in range(k):
            #create a dictionary with the nucleotides as keys
            # and the frequency of their occurrences as values
            freq = {'A':1, 'C':1, 'T':1, 'G':1}
            for m in range(len(motifs)):
                freq[motifs[m][pos]] +=1
            prof_matrix.append(freq)

        pwm = []
        for freq_dict in prof_matrix:
            total_freq = sum(freq_dict.values())
            pwm.append({base: freq_dict[base] / total_freq for base in 'ACGT'})

        new_motifs = []
        for s in sequences:
            score = 0
            best_motif = ''
            for i in range(len(seq) +1-k):
                kmer = seq[i:i+k]
                kmer_score = 1
                for j in range(k):
                    kmer_score *= pwm[j][kmer[j]]
                if kmer_score > score:
                    score = kmer_score
                    best_motif = kmer
            new_motifs.append(best_motif)

        new_unique_cols = sum([len(set(col)) for col in zip(*new_motifs)])
        best_unique_cols = sum([len(set(col)) for col in zip(*best_motifs)])

        if new_unique_cols > best_unique_cols:
            best_motifs = new_motifs.copy()
            prof_matrix = []
            for pos in range(k):
                freq = {'A':1, 'C':1, 'T':1, 'G':1}
                for m in range(len(best_motifs)):
                    freq[best_motifs[m][pos]] +=1
                prof_matrix.append(freq)

            pwm = []
            for freq_dict in prof_matrix:
                total_freq = sum(freq_dict.values())
                pwm.append({base: freq_dict[base] / total_freq for base in 'ACGT'})
        if best_motifs == motifs:
            return pwm
        motifs = new_motifs.copy()




k_values = range(3, 9)

for k in k_values:
    print(gibbs_sampler_pwm(load_sequence('motifs_in_sequence.fa'), k))
