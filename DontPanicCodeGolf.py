a={};c,d,e,f,g,h,i,j=[int(i)for i in raw_input().split()]
for i in range(j):z,o=([int(j)for j in raw_input().split()]);a[z]=o
while 1:k,l,m=raw_input().split();k=int(k);l=int(l);x=g if(k==f or k==-1)else a[k];print'BLOCK'if((l>x and m=='RIGHT')or(l<x and m=='LEFT'))else"WAIT"
