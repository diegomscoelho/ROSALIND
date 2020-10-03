a = open('rosalind_rna.txt', 'r')
f = open('rna_output.txt', 'w')

bases = a.readlines()[0]
RNA=""

for i in range(0,len(bases)):
   if bases[i]=="T":
    RNA+="U"
   else:
    RNA+=bases[i]

print >>f, RNA

f.close()
