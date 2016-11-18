import sys
import math
import binascii

def toBin(n):
    return toBin(n/2) + str(n%2) if n else ""

count1,count0=[0 ,0]
message = raw_input()
largo=len(message)
l1=l0=0
message=list(message)

for i in range(len(message)):
    bn=bin(ord(message[i]))
    if len(bn)==9:
        message[i]=bn  
    elif len(bn)==8:
        message[i]='0'+bn
    elif len(bn)==10:
        message[i]=bn[:-1]
    

message = ''.join(message)
message = message.replace("0b", "")
print >> sys.stderr, message
ml=list(message)
salida=''
for i in range(len(ml)):
    if i+1<=len(ml)-1 and  ml[i]=='0' and ml[i+1]=='0':
        l0+=1
    elif ml[i]=='0':
        l0+=1
        ceros=l0*[0]
        ceros=''.join((str(e) for e in ceros))
        salida=salida,'00 ', ceros ,' '
        salida=''.join(salida)
        l0=0
    elif i+1<=len(ml)-1 and ml[i]=='1' and ml[i+1]=='1':
        l1+=1
    elif ml[i]=='1':
        l1+=1
        unos=l1*[0]
        unos=''.join((str(e) for e in unos))
        salida=salida+'0 '+ (unos)+' '
        salida=''.join(salida)
        l1=0
salida = salida[:-1]

print salida

