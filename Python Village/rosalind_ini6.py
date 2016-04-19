a = open('rosalind_ini6.txt', 'r')
f = open('output_ini6.txt', 'w')

frase=a.readlines()
sep=frase[0].split()
lis=""
check=[]
for i in range(0,len(sep)):
   if (sep[i] in check) == False:
    lis+=sep[i]+" "+str(sep.count(sep[i]))+"\n"
    check.append(sep[i])
print >>f, lis

f.close()
