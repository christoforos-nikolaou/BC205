# %% Exercise 2 : Identifying non-mers in a bacterial genome (For grading)

#I could not download the sequence so i used Ctrl + A to copy the contents and pasted them in a nano file.

import itertools, re, time

start_time = time.time()
def get_lines(fl): #First we make a function to find the total number of rows in our file so we can use it later to read the file
    with open(f'{fl}') as get_lines:
        line_number = list(enumerate(get_lines))[-1][0]+1
    return line_number

whole_seq = '' #Make an empty string
with open('e_coli.fa') as e_col:
    for i in range(get_lines('e_coli.fa')): #Here we use the function to get all the lines of the genome
        one_line = e_col.readline() #We read the file line by line, which we also need to do before skiping the first line as seen below
        if i == 0: #since the first line is always the name of the organism as well as extra information, we skip this using continue
            continue 
        whole_seq = ''.join([whole_seq,one_line]) #We use the empty string to start adding each line of the sequence

# I know this implementation takes longer to read the file but instead of copy pasting the provided code to read it faster as seen in chapter 1, i tried to do it another way

whole_seq = re.sub(r'\n','',whole_seq) #We remove the new lines so we have the whole sequence in a single row string which will be useful to use the "10-mer in string"
whole_seq = re.sub('N','',whole_seq) #Since we have unidentified bases characterized by the letter N, we could remove those, although this will give us altered results in the given position of N. I checked in the sequence provided and we have 2 different occurences of Ns that are both consecutive with a total of about ~100 Ns split in ~50 and ~50.
tenmers = itertools.product(*itertools.repeat(['A','T','G','C'], 10)) #We get permuation with replacement for 10-mers. 
dict_mers = {} #Create an empty dictionary to use later for the existence / non-existence of k-mers (in our case 10-mers)

for rnd in tenmers:
    dict_mers[''.join(list(rnd))] = 0 #create a dictionary with all 1_048_576 possible combinations and initialize its value to 0
    #We use this since the permuation with replacement returns tuples with the nucleotides and we join them into a single 10-mer


for j in range(len(whole_seq)-10+1): #we assign each time we find an 10-mer to the dictionary, moving at a pace of 1 nucleotide (from left to right) at a time.
#We use the above range since the possible positions for a kmer are (n - k + 1), where n is the length of our sequence and k is the kmer
    motif = j+10 #We set the end-position for the motif to use as index later
    e_mer = whole_seq[j:motif] #Here we use the starting position for the motif (j) and the end-position (motif) as seen above to check existence
    dict_mers[e_mer] += 1 #We add a count to the 10-mer found in the dictionary

#This aproach takes a bit more time but we now have not only what 10-mers dont exist but we can also check what kmer is over-represented and so on
#By using the dictionary we can now filter the 10-mers that were not found which is:
non_existing_kmers = [k for k,v in dict_mers.items() if v == 0]#With this we only take the 10-mers that do not exist

print(f'{len(non_existing_kmers)} 10-mers were not found from the total of {len(dict_mers)} possible 10-mers in the genome of ecoli.') #A total of 223_320 10-mers not found from the total of 1_048_576 possible 10-mers, so about 21.3% of the possible 10-mers are not found in the 3_101_253 nucleotide long sequence.
end_time = time.time()
print(end_time - start_time)




# %% Different faster approach for exercise 2:
#Using the provided in Chapter 1 code to read the genome
import itertools, time

start_time = time.time()

file = open('e_coli.fa', 'r')
ecoli = ''
count = 0
k = 10
for line in file:

    count += 1
    if (count > 1): #Skips the first line (header)
        ecoli += line.replace("\n", "") #Removing the new lines
kmers = [ecoli[i:i+k] for i in range(len(ecoli)-k+1)] #All the 10-mer subsequences
kmers.sort()
setkmers = set(kmers)#All the unique 10-mer subsequences

tenmers = set([''.join(list(motf)) for motf in itertools.product(*itertools.repeat(['A','T','G','C'], 10))]) #Here we convert all the possible 10-mers by permuation with replacement to a set so we can use the difference 
non_existing = list(tenmers - setkmers) #Since using the set format we can do union difference etc fast, we use the difference to see how many of the kmers dont exist in the unique 10-mers of the ecoli genome

#We can now check the non existing kmer from the list

print(len(non_existing))  #Show the number of non existing kmers (223321)

#Below i did an extra check since i had 1 more non-existing kmer with this method (223321 instead of 223320)

non_existing_kmers_set = set(non_existing_kmers) 


extra_motif = list(set(non_existing) - non_existing_kmers_set) #With my approach i get 1 less k-mer which is CAGAAGTTCG and as i noticed, it comes from removing the Ns which concatenates CAGA with AGTTCG (inbetween there are unspecified bases)
print(extra_motif) #Here we can see the motif that does not exist, as explained above

#I suppose this method is the better way to approach the problem, more specific and with less time requirement. We could also apply to this the dictionary approach but since our question here is 

end_time = time.time()
print(end_time - start_time)

