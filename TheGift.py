import sys

bud=[]
n = int(raw_input())
c = int(raw_input())
for i in xrange(n):
    bud.append(int(raw_input()))
if sum(bud)<c:
    print "IMPOSSIBLE"
else:
    bud.sort()
    for i in bud:
        div=int(c/n)
        if i<div:
            print i
            c=c-i
        else:
            print div
            c=c-div
        n=n-1
