a = open('rosalind_cons.txt', 'r')
f = open('cons_output.txt', 'w')

## Create a list with paired (>Rosalind, "RNASeq")
fastas_raw = a.readlines()
fastas_strip =''.join(fastas_raw).split()
fastas=[fastas_strip[0]]
codon=''
for i in range(1,len(fastas_strip)):
  if fastas_strip[i][0]==">":
    fastas.append(codon)
    fastas.append(fastas_strip[i])
    codon=''
  else:
    codon+=fastas_strip[i]
fastas.append(codon)

R=len(fastas)/2
C=len(fastas[1])

## Generate DNA strings matrix
dnamat=[]

for i in range(0,C):
  for j in range(0,2*R,2):
    dnamat.append(fastas[1+j][i])
##

## Generate Profile matrix
profile=[['A:'],['C:'],['G:'],['T:']]

for num in range(0, C):
  profile[0].append(str(dnamat[num*R:num*R+R].count('A')))
  profile[1].append(str(dnamat[num*R:num*R+R].count('C')))
  profile[2].append(str(dnamat[num*R:num*R+R].count('G')))
  profile[3].append(str(dnamat[num*R:num*R+R].count('T')))

##

## Consensus string generator
consensus=""

for i in range(1,C+1):
  T=str(max(int(profile[0][i]),int(profile[1][i]),int(profile[2][i]),int(profile[3][i])))
  if profile[0][i]==T:
   consensus+="A"
  elif profile[1][i]==T:
   consensus+="C"
  elif profile[2][i]==T:
   consensus+="G"
  else:
   consensus+="T"

##

print >>f, consensus+"\n"+" ".join(profile[0])+"\n"+" ".join(profile[1])+"\n"+" ".join(profile[2])+"\n"+" ".join(profile[3])
f.close()
