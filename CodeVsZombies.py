import sys
import math

# Save humans, destroy zombies!
# game loop
while True:
    x, y = [int(i) for i in raw_input().split()]
    human_count = int(raw_input())
    hx=[]
    hy=[]
    for i in xrange(human_count):
        human_id, human_x, human_y = [int(j) for j in raw_input().split()]
        hx.append(human_x)
        hy.append(human_y)
    
    zombie_count = int(raw_input())
    zx=[]
    zy=[]
    znx=[]
    zny=[]
    for i in xrange(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in raw_input().split()]
        zx.append(zombie_x)
        zy.append(zombie_y)
        znx.append(zombie_xnext)
        zny.append(zombie_ynext)
    diht=9999999
    for i in range(human_count):
        morir=True
        dist=math.sqrt((hx[i]-x)**2+(hy[i]-y)**2)
        print >> sys.stderr, "La distancia a ...",i," es de ...",dist
        for j in range(zombie_count):
            if (((math.sqrt((hx[i]-zx[j])**2+(hy[i]-zy[j])**2))<401)):
                morir=False
        if (dist<diht and morir):
            humx=hx[i]
            humy=hy[i]
            diht=dist
    print >> sys.stderr, "El humano mas cercano esta en...", humx,humy
    dist=99999
    for i in range(zombie_count):
        print >> sys.stderr, "Debug messages...",zx[i],"",human_x,"",zy[i],"",human_y
        dizt=math.sqrt((zx[i]-humx)**2+(zy[i]-humy)**2)
        
        if (dizt<dist):
            ex=zx[i]
            ey=zy[i]
            dist=dizt
    print  ex, ey
