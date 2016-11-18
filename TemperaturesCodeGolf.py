import sys;n=int(input());t=input()
if not t:print("0");sys.exit()
r=[int(i)for i in t.split()];m=min(r,key=lambda x:abs(x));print((abs(int(m)))if(abs(int(m))in r)else m)
