a = open('rosalind_prot.txt', 'r')
b = open('codon_lib.txt', 'r')
f = open('prot_output.txt', 'w')

bases = a.readlines()[0]	#input

## Creating Library of codons
pat = b.readlines()
pat2=''

for i in range(0,len(pat)):
  pat2+=pat[i]

biblio=pat2.split()
##

protein=""

for i in range(0,len(bases)-1,3):
  if bases[i:i+3] in ["UAA","UAG","UGA"]:
    break
  else:
    protein+= biblio[biblio.index(bases[i:i+3])+1]

print >>f, protein
f.close()
