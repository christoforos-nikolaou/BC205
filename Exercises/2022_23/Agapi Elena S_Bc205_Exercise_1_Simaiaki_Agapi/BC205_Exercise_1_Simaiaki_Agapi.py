#Exercise 2: Identifying non-mers in a bacterial genome. Non-mers are k-mers that don't have a single instance in a greater corpus (e.g. a genome), 
#that is they do not exist in a genome. Search the genome of E. coli for any given 10-mer and report the 10-mers that do not exist in the genome.


#Read file and save the while genome in a string
file = "ecoli.fa.txt"
with open ("files/ecoli.fa") as l:
    l.readline()
    ecolseq =""
    for ln in l:
        lnseq = ln.strip()
        ecolseq += lnseq



#Findind all the possible 10-mers that can be found with the 4 nucleotides
import itertools

k=10
bases = ["A","T","G","C"]
combos = itertools.product(bases, repeat=k)
strcomb = ("".join(y) for y in combos) #generators save memory compared to lists

#Find all k-mers/10-mers in the genome

kmers=[]
for i in range(len(ecolseq)-k+1):
    kmers.append(ecolseq[i:i+k])


#Isolation of all the unique ones (makes the procedure faster)
kmers = set(kmers)

#Calculating how many 10-mers are not included in the E.Coli genome
count=0
nonkmers =[]
allk =0
res =0
for y in strcomb:
    allk += 1     #control to check if the theoritical 4^10 has been produced with the product functional tool 
    if y not in kmers:
        count +=1 #counting the 10-mers not included is same as len(nonkemers)/not necessary / check point
        nonkmers.append(y)
    else:         #not necessary / check point
        res+=1    #counting the included 10-mers / check point

import random

print("The number of non 10-mers is:",count)
print("Some of those non-mers are", random.sample(nonkmers,10))


#Expected non-10-mers/ Theoritical check:
theor = 4**10
obs = len(kmers)
exp = theor - obs
print("According to theory we would expect", exp,"non-mers since all the 10-mers are", theor,"and the observed in E.Coli are", obs)

#NOTE: The theoritical check is not in agreement with the ones found above with comparison. Not quite sure why.


#Another way to avoid for-loops and exhausting search is to immediately produce sets that contain unique 10-mers and calculate their difference:
#The reading of the file is common

kmers2 = {ecolseq[i:i+k] for i in range(len(ecolseq)-k+1) }
combos = itertools.product(bases, repeat=k) 
#must to re-write the command since it's a generator that has been used above and needs to be generated to reused
strcomb2 = {"".join(y) for y in combos} #permuation with replacement we can make it a set as they all uniq
nonmers = strcomb2 - kmers2

print(len(nonmers))
print(random.sample(nonmers, 10)) #demonstartion of some non-mers