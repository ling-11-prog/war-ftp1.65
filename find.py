a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c="0123456789"

num=800
outstr=""
for i in range(0,26):    
    for j in range(0,26):        
        for k in range(0,10):
            outstr = outstr+a[i]+b[j]+c[k]
            if(len(outstr) > num):
                    break
outstr=outstr[0:800]
str = '32516131'
ostr = ''
for i in range(len(str), 0, -2):
    tmp = int(str[i - 2:i], 16)
    ostr += chr(tmp)
#print(ostr)

print('eip:',outstr.find(ostr))
print('esp:',outstr.find('Q4aQ'))
print('ebp',outstr.find('3aT4'))

