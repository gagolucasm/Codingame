import sys

n = int(raw_input()) # the number of temperatures to analyse
temps = raw_input() # the n temperatures expressed as integers ranging from -273 to 5526
if n>0:
    temps=map(int, temps.split(' '))
# Write an action using print
print >> sys.stderr,"La lista es", temps
pmc=9999
nmc=-9999
for i in range (n):
    if temps[i]>=0 and temps[i]<pmc:
        pmc=temps[i]
    elif temps[i]<0 and temps[i]>nmc:
        nmc=temps[i]
#Mostrar resultado
if abs(nmc)>=pmc and pmc!=9999:
    print pmc
elif abs(nmc)<pmc and nmc!=-9999:
    print nmc
else:
    print 0
