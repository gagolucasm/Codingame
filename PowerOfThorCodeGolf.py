x,y,q,w=[int(i) for i in input().split()]
while 1:
 a=int(input())
 s=d=""
 if q>x:s="W";q-=1
 if q<x:s="E";q+=1
 if w<y:d="S";w+=1
 print (d+s)
