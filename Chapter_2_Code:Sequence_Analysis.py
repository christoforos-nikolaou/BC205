#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BC205: Algorithms in Bioinformatics
Chapter 2: Sequence Analysis (Python Code)

Created on Thu Feb 27 10:23:13 2020
@author: christoforos
"""

#%%
""" Naive GCContent """
import regex as re 
f=open('/home/christoforos/Dropbox/Teaching/BC205/files/ecoli.fa', 'r')

seq = ""
window=1000
total = 0
nG=nC=0
GCCont=0
times=0;
for line in f:
    x=re.match(">", line)
    if x == None:
        length=len(line)
        total=total+length
        seq=seq+line[0:length-1]
        
for k in range(len(seq)):
    if(seq[k]=="G"):
        nG+=1
    elif(seq[k]=="C"):
        nC+=1
GCContent=(nG+nC)/len(seq)
print("GC content =", GCContent)
#%%

#%% 
""" GC Content """

import regex as re 

f=open('/home/christoforos/Dropbox/Teaching/BC205/files/ecoli.fa', 'r')

seq = ""
window=1000
total = 0
A=T=G=C=0
GCCont=0
times=0;

for line in f:
    x=re.match(">", line)
    if x == None:
        length=len(line)
        total=total+length
        seq=seq+line[0:length-1]
f.close()

C=seq.count("C")
G=seq.count("G")
GCCont=(G+C)/len(seq);
print(GCCont)
#%%

#%%
""" GC distance """

f=open('/home/christoforos/Dropbox/Teaching/BC205/files/GCContent.tsv', 'r')

i=0
GCC={}
for line in f:
    i=i+1
    if(i>1):
        species=line.split()[0]
        GC=line.split()[1]
        GCC[species]=float(GC)

gcdistances={}
for genome1 in GCC.keys():
    for genome2 in GCC.keys():
        pair=genome1+":"+genome2
        gcdistances[pair]=abs(float(GCC[genome1])-float(GCC[genome2]))
        gcdistances[pair]=round(gcdistances[pair],2)
        print(pair, round(gcdistances[pair],3))

sorted(gcdistances.items(), key=lambda x: x[1])

#%%

#%%
""" HGT search """
import regex as re
import numpy as np

f=open('/home/christoforos/Dropbox/Teaching/BC205/files/Staaur.fa', 'r')

seq = ""
window=1000
nG=nC=0
GCCont=[]

for line in f:
    x=re.match(">", line)
    if x == None:
        length=len(line)
        seq=seq+line[0:length-1]
f.close()

step=100
times=int(len(seq)/step);

for i in range(times):
    DNA=seq[i*step:i*step+window]
    nC=DNA.count("C")
    nG=DNA.count("G")
    GCCont.append((nG+nC)/window)

# Calculate Z-scores
mGC=np.mean(GCCont)
sdGC=np.std(GCCont)
zGC=(GCCont-mGC)/sdGC
for i in range(len(zGC)):
    if abs(zGC[i])>=3:
        print(i*1000, zGC[i])
        

#%%

#%%
""" k-mer frequencies """

import regex as re

f=open('/home/christoforos/Dropbox/Teaching/BC205/files/Staaur.fa', 'r')

seq = ""
k=2
kmers={}

for line in f:
    x=re.match(">", line)
    if x == None:
        length=len(line)
        seq=seq+line[0:length-1]
f.close()

for i in range(len(seq)-k):
    DNA=seq[i:i+k]
    if DNA not in kmers.keys():
        kmers[DNA]=1
    else:
        kmers[DNA]+=1

{k: float(v) / len(seq) for k, v in kmers.items()} 
        
#%%        

#%%
""" Relative k-mer Frequencies """
import regex as re

f=open('/home/christoforos/Dropbox/Teaching/BC205/files/Staaur.fa', 'r')

seq = ""
k=2
kmers={}

for line in f:
    x=re.match(">", line)
    if x == None:
        length=len(line)
        seq=seq+line[0:length-1]
f.close()

pnuc={}
for i in range(len(seq)):
    nuc=seq[i]
    if nuc not in pnuc.keys():
        pnuc[nuc]=1
    else:
        pnuc[nuc]+=1

pnuc={k: float(v) / len(seq) for k, v in pnuc.items()} 

for i in range(len(seq)-k):
    DNA=seq[i:i+k]
    if DNA not in kmers.keys():
        kmers[DNA]=1
    else:
        kmers[DNA]+=1

kmers={k: float(v) / len(seq) for k, v in kmers.items()} 

rkmers=kmers
for kmer in kmers.keys():
    nuc1=list(kmer)[0]
    nuc2=list(kmer)[1]
    rkmers[kmer]=round(kmers[kmer]/(pnuc[nuc1]*pnuc[nuc2]),3)

print(rkmers)

#%%


#%%
""" Plotting Chargaff """ 

import matplotlib.pyplot as plt 
import regex as re  

f = open('/home/christoforos/Dropbox/Teaching/BC205/files/Staaur.fa', 'r')
seq = ""
total = 0
A=T=G=C=[]
times=0;
for line in f:
	x=re.match(">", line)
	if x == None:
		length=len(line)
		total=total+length
		seq=seq+line[0:length-1]
f.close()

x=[]
ATparity=[]
window=100000
step=10000
times=int(len(seq)/step);
for i in range(times):
    x.append(i)
    DNA=seq[i*step:i*step+window]
    A=DNA.count("A")
    T=DNA.count("T")
    C=DNA.count("C")
    G=DNA.count("G")
    ATparity.append(float(A-T)/float(A+T))

  
# plotting points as a scatter plot 
plt.plot(x, ATparity, color= "green", linewidth=5.0) 
#plt.scatter(x, ATparity, color= "green")
  
# x-axis label 
plt.xlabel('Genome Coordinates') 
# frequency label 
plt.ylabel('(A-T)/(A+T)') 
# plot title 
plt.title('S. aureus AT parity') 
# showing legend 
#plt.legend() 
  
# function to show the plot 
plt.show() 
#%%
