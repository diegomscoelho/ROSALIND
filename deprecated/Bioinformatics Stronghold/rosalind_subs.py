a = open('rosalind_subs.txt', 'r')
f = open('subs_output.txt', 'w')

mat=a.readlines()
S=mat[0]
T=mat[1].split()[0]
start=""

for i in range(0,len(S)-len(T)):
  if S[i:len(T)+i]==T:
    start+=str(i+1)+" "

print >>f, start[:-1]
f.close()
