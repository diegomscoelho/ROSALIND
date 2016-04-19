a = open('rosalind_dna.txt', 'r') #Open and read input file
f = open('dna_output.txt', 'w') #Open and write in output file
bases= a.readlines()[0] #Turn nucleotides in a single string

print >>f, str(bases.count('A'))+" "+str(bases.count('C'))+" "+str(bases.count('G'))+" "+str(bases.count('T')) #print and save answer

f.close()
