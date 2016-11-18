import sys
import math
from decimal import Decimal 
defib=[]
da=di=9999.0
lon = Decimal(raw_input().replace(',','.'))
lat = Decimal(raw_input().replace(',','.'))
n = int(raw_input())
for i in xrange(n):
    defib.append( raw_input().split(';'))

for i in range(n):
    defib[i][4]=Decimal(defib[i][4].replace(',','.'))
    defib[i][5]=Decimal(defib[i][5].replace(',','.'))
    x=defib[i][4]-lon*Decimal(math.cos((defib[i][5]+lat)/2))
    y=defib[i][5]-lat
    d=math.sqrt((x**2)+(y**2))*6371
    dn=math.sqrt(((defib[i][5]-lat)**2) +(defib[i][4]-lon)**2)
    if di>dn:
        di=dn
        salida=defib[i][1]
        
print salida
