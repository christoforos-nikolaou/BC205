#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:46:20 2020

@author: zelda
"""
sequences = []
with open ('files/motifs_in_sequence.fa') as file:
    for line in file:
        sequences.append(line.strip()) # 50 sequences as elements of a list. 100 bases each sequence
    

##Gibbs sampler##
import random
import numpy as np

def Gibbs_sampler(sequences,k): #k is the length of the motif, sequence is a list with the sequences
    
    dictionary = {'A':0,
                  'T':1,
                  'C':2,
                  'G':3}
    
    column_sum = len(sequences) #number of rows (50) or number of sequences
    length = len(sequences[0]) #number of columns or number of nucleotides in seq
    Imax = 1.8*k #threshold of I
    
    pwm = np.zeros([4,k]) # A,T,C,G X len(motif)
    
    for seq in sequences:
        rand_start = random.randint(0, length-k) #pick a random nucleotide from each sequence
        motif = seq[rand_start:rand_start+k] #and take substring as the motif
       
        lst = enumerate(motif) #finding the index of each nucleotide in the motif to access the correct column
                               #and using the dictionary to access the correct row 
        for i in lst: #making the first random pwm
            pwm[dictionary[i[1]],i[0]]+=1
            
    pwm = pwm/column_sum
    
    information = np.zeros([1,k])
    count=0
    while (np.sum(information)) < Imax: #while information_content of the pwm 
        motives=[]                      #is less than the threshold
        
        information_old = np.sum(information) #keeping the previous value of information contect
                                             #to check convergence in case the theshold 
        for row in range (column_sum):                #is never reached
            maxx=0
            rand_seq = random.randint(0, column_sum-1) #pick a random index - sequence
            seq = sequences[rand_seq]               
            for i in range(len(seq)-k):   #take each k-mer from the sequence 
                score = 0
                substring = seq[i:i+k]
                lst = enumerate(substring)
                
                for j in lst:                         #scoring each k-mer based on the pwm
                    score+=pwm[dictionary[j[1]],j[0]]   #keeping the motif with the highest score
                                                         #from each sequence
                if score > maxx:  
                    maxx = score
                    motif = substring
                    
            motives += [motif] #keep all the motifs with the highest score in the list motives
        
        pwm = np.zeros([4,k]) # A,T,C,G X len(motif) 
        
        for elem in motives: 
            lst = enumerate(elem)
            for i in lst:         #making the new pwm
                pwm[dictionary[i[1]],i[0]]+=1
                 
        pwm = pwm/column_sum
        
        information = np.zeros([1,k]) #computing the information of each position
        for i in range(k):
            information[0,i] = 2-abs(sum([elem*np.log2(elem) for elem in pwm[:,i] if elem > 0]))
            

        if abs(information_old - np.sum(information)) <= 0.5: #ckecking convergence 
            count+=1
            if count == 10: #if the difference of the information content is less or equal to 0.5
                break       #for consecutive 10 iterations then break
        else:
            count=0
    
    max_index_col = np.argmax(pwm, axis=0) #extracting the motif according to the   
                                           #highest frequency of each nucleotide in each position
    motif=''
    for values in max_index_col:
        for keys in dictionary.keys():
            if values == dictionary[keys]:
                motif+= keys
        
    return pwm,information,motif


#repeat the algorithmm 100 times for each k (3 to 7) and keep the pwm and motif with the highest infromation_content
#this process takes approximately 4min (in my computer)
    
####100-cycled GIbbs#####
for k in range (3,8):
    highest_info = 0
    for i in range (100):
        summ=0
        pwm, information_content,motif = Gibbs_sampler(sequences,k)
        summ+=np.sum(information_content)
        if summ > highest_info:
            highest_info = summ
            pwm_ret = pwm
            motif_ret = motif
        
    print('\nThe information content of the motif divided by it\'s length is:',highest_info/k) #divide by length to normalize and compare among other k
    print('The pwm of the motif is:\n',pwm_ret)
    print('The motif is:',motif_ret)



#To find the motifs for each k with the highest information content i have to repeat gibbs sampler many times because of the randomness that takes place
#The motif that returns the highest scaled information content is GAT (k = 3, I/k = 1.9528 or 2!) but i think that the motif that we are looking for
#is the motif GATA (k=4, I/k = 1.857) which contains GAT and is contained in all the longer found motifs.
#(Also we know the existence of the GATA transcription factors and indeed GATA is part of these binding sites)
#Sometimes the algorithm returns other 3-mers (eg ATG,GGC,AAG) with high information content as well but it
#is noted that GATA is returned almost in every repetition of the 100-cycled Gibbs which means that it may be the only 4-mer motif with so high information content.
#Finally i have to report that the threshold that i chose for checking convergence may not be the best choice and should be stricter
#Either way i kept this threshold because otherwise i would have made the algorithm a lot slower (is already slow though :P).