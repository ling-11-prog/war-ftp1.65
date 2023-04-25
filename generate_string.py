# -*- coding: utf-8 -*-

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
print(outstr[0:800])         

