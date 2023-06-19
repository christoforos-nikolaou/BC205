
# create a function that will take a sequence string as input and return
# True or False depending on whether it contains a palindrome substring and if so,
# will also return the longest substring

def palindrome_subsequence(sequence):
   #scan the sequence string with step = 2 to exclude 2-mers
   pal_list = [sequence[i:j+1] for i in range(len(sequence))
        for j in range(i+2, len(sequence))

        if sequence[i:j+1] == sequence[i:j+1][::-1]]

   # if palindrome substrings were found, return True and the biggest one
   if pal_list:
       p = max(pal_list, key=len)
       return True, p # pal_list
   else:
   # if pal_list is empty, sequence has no palindrome substrings, return False

       return False


# check for palindromes in the sequence 'TTCAGGTGG'

print(palindrome_subsequence('TTCAGGTGG'))        # output True, GGTGG

#check for palindromes in the sequence 'CTGTTATTAATTATTGCAT'

print(palindrome_subsequence('CTGTTATTAATTATTGCAT')) # ouput TRUE TTATTAATTATT

#check for palindromes in the sequence 'GGCATCGGATTCGT'
print(palindrome_subsequence('GGCATCGGATTCGT'))     # output False





