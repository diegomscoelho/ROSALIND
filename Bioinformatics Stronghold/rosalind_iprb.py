a = open('rosalind_iprb.txt', 'r')
f = open('iprb_output.txt', 'w')

integers= a.readlines()[0].split()
k=int(integers[0])
m=int(integers[1])
n=int(integers[2])
orgn=float(k+m+n)

a1= (n*(n-1))/(orgn*(orgn-1)) 	# case1: 2n
a2= (m*n)/(orgn*(orgn-1)) 		# case2: 1n + 1m
a3= (.25*m*(m-1))/(orgn*(orgn-1))	# case3: 2m
d= a1+a2+a3

ip = 1-d

print ip

print >>f, ip
f.close()
