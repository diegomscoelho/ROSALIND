#Sum all odd number from a to b
#4556 9028

a=4556
b=9028
soma=0
lis=[]
for i in range(a+1,b,2):
	soma+=i
	lis.append(i)
print soma
#print lis[0]
#print lis[len(lis)-1]
#print lis
