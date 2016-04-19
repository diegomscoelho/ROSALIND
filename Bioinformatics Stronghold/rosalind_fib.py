a = open('rosalind_fib.txt', 'r')
f = open('fib_output.txt', 'w')

bases = a.readlines()[0].split() #bases = ['months' , 'number of litters']
n=int(bases[0]) #months
k=int(bases[1]) #litters

FB=[1,0,k]

for i in range(0, n-1):
  FB[0]+=FB[1]
  FB[1]=FB[2]
  FB[2]=int(bases[1])*FB[0]
  print FB[0], FB[1], FB[2]

print >>f, FB[0]
f.close() 
