a = open('rosalind_gc.txt', 'r')
f = open('gc_output.txt', 'w')

fastas_raw = a.readlines()
fastas_join =''.join(fastas_raw).split('\n')
fastas = ''.join(fastas_join).split('>')[1:]

print fastas

maior=[0,0]
prob=[0,0]

for i in range(0,len(fastas)):
  prob=[fastas[i][:13],(fastas[i][13:].count('C') + fastas[i][13:].count('G'))/float(len(fastas[i][13:]))]
  if prob[1]>maior[1]:
   maior=prob

print >>f, maior[0]+"\n"+str(100*maior[1])
f.close()
