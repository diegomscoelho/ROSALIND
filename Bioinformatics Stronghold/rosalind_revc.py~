a = open('rosalind_revc.txt', 'r')
f = open('revc_output.txt', 'w')

bases = a.readlines()[0]
Code=""

for i in range(0,len(bases)):
  if bases[i]=="A":
   Code="T"+Code
  elif bases[i]=='T':
   Code='A'+Code
  elif bases[i]=='C':
   Code='G'+Code
  elif bases[i]=='G':
   Code='C'+Code

print >>f, Code
f.close()
