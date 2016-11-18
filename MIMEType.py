fname=[]
D = {}
n = int(raw_input()) # Number of elements which make up the association table.
q = int(raw_input()) # Number Q of file names to be analyzed.
for i in xrange(n):
    a=raw_input().split()
    D[a[0].lower()]=a[1]
for i in xrange(q):
    fname.append( raw_input().split('.')) # One file name per line.
    if len(fname[i])>1 and fname[i][len(fname[i])-1].lower() in D :
        print D[fname[i][len(fname[i])-1].lower()]
    else :
        print "UNKNOWN"
