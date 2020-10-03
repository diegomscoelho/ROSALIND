a = open('rosalind_hamm.txt', 'r')
f = open('hamm_output.txt', 'w')

linhas = a.readlines()
s = linhas[0]
t = linhas[1]
hamm=0

for i in range(0,len(s)-1):
  if s[i]!=t[i]:
   hamm+=1

print >>f, hamm
f.close()
