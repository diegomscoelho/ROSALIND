a = open('rosalind_fibd.txt', 'r')
f = open('fibd_output.txt', 'w')

bases = a.readlines()[0].split() #bases = ['months' , 'number of litters']
n=int(bases[0]) #Final month
m=int(bases[1]) #How many months they live?

FB=[1,0,1]
M=m*[0]
#M[m-1]=1
count=1

for i in range(0, n-1):
  M[m-1]=FB[2]
  FB[0]+=FB[1]-M[0]
  FB[1]=FB[2]
  FB[2]=FB[0]
  for j in range(0,m-1):
    M[j]=M[j+1]
  #M[m-1]=FB[1]
  print i+2 ,FB[0], M[0]

print >>f, FB[0]
f.close()
