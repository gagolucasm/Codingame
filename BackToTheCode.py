import sys
import math
import random
import time
from collections import Counter
yy=xx2=1
mindis=999
punto='0 0'
yo=xo=pxa=pya=pxa2=pya2=pya3=pxa3=xfut=yfut=ya=l=subiendo=uno=xx=0
cuentaaa=enemx=enemy=goto=ar=ab=count=cuentap=cuentapant=yy2=en1an=0
mapa=[None]*99999
opponent_count = int(raw_input()) # Opponent count
activ=-1

def buscar():
    yo=-1
    xo=-1
    mindis=99999
    for i in range(20):
        for j in range(35):
            if mapa[game_round-1][i][j]=='.':
                dis=abs(x-j)+abs(y-i)
                if dis<mindis:
                    mindis=dis
                    yo=i
                    xo=j
    px=xo
    py=yo
    return px ,py;
def up(n):
    an=0
    if y-n>-1 and mapa[game_round-1][y-n][x]=='.' :
        an=1 
    return an;
def down(n):
    an=0
    if y+n<20 and mapa[game_round-1][y+n][x]=='.' :
        an=1
    return an;
def right(n):
    an=0
    if x+n<35 and mapa[game_round-1][y][x+n]=='.' :
        an=1 
    return an;
def left(n):
    an=0
    if y-n>-1 and mapa[game_round-1][y][x-n]=='.' :
        an=1
    return an;
    
         
while 1:
    mapar=[]
    start= time.time()
    game_round = int(raw_input())
    
     # x: Your x position
     # y: Your y position
     # back_in_time_left: Remaining back in time
    x, y, back_in_time_left = [int(i) for i in raw_input().split()]
    px=x
    print >> sys.stderr, 'es el turno' ,game_round-1
    py=y
    for i in xrange(opponent_count):
         # opponent_x: X position of the opponent
         # opponent_y: Y position of the opponent
         # opponent_back_in_time_left: Remaining back in time of the opponent
        opponent_x, opponent_y, opponent_back_in_time_left = [int(j) for j in raw_input().split()]
    
    for i in xrange(20):
        mapar.append( list(raw_input()) )# One line of the map ('.' = free, '0' = you, otherwise the id of the opponent)
    mapa[game_round-1]=mapar
    disten=(abs(opponent_x-x))+(abs(opponent_y-y))
    punto=0
    py=0
    en1=0
    for i in range(20):
            punto=punto+mapa[game_round-1][i].count('.')
            en1=en1+mapa[game_round-1][i].count('1')
            py=py+mapa[game_round-1][i].count('0')
            
    
    # dist=l*2+2*(l-2)  l es lado de cuadrado a partir de 2
    # dist=2l+2l-4
    # dist=4l-4  --> l=dist-4/4 asi l es el lado del cuadrado mas grande que puedo hacer antes de que llegue el enemigo
    py=y
    px=x
    if goto>0:
        print enemx,' ',enemy
        if x==enemx and y==enemy:
            goto=0
    elif right(1) and ar==0 and ab==0 and l==0:
        px=x+1
        print>> sys.stderr,'right'
    elif left(1) and ar==0 and l and x-1>-1:
        px=x-1
        print>> sys.stderr,'left'
    elif up(1) and (l==0 or ar==1):
        py=y-1
        ar=not(ar)
        l=1
        print>> sys.stderr,'up'
    
    elif down(1):
        ab=not(ab)
        py=y+1
        l=0
        print>> sys.stderr,'down'
    else :
        
        px,py=buscar()
    if py==y+1:
        ar=0
        
    if py==y-1:
        ab=0
    if px==x+1:
        l=0
        
    if px==x-1:
        l=1
    if px<0 or py<0 or punto==0:
        px=x
        py=y
    if punto==0:
        uno+=1
    if en1>en1an+15 and back_in_time_left and 0:
        print 'BACK 25'
        goto=25
        enemx=opponent_x
        enemy=opponent_y
    if punto ==0 and uno==2 and en1>py and back_in_time_left:
        uno==6
        print 'BACK 25'
        
    """py=up(1)
    py=y
    py=down(1)
    px=left(1)
    px,py=buscar()
    """
    mapar=[]
    if (pxa2==px and pya2==py)and(pxa3==pxa and pya3==pya)and (xx2==x and yy2==y):    
        print int(random.random()*34), ' ',int(random.random()*19)
        print>> sys.stderr,'Elegi aleatorio'
    else:
        
        print '%d %d' % (px,py)
    mindis=999
    punto='0 0'
    mapar=[]
    cuentapant=cuentap
    cuentap=0
    end = time.time()
    #print>> sys.stderr, end - start
    if activ>0:
        activ-=1
    if goto>0:
        goto-=1
    cuentaaa+=1
    pxa=px
    pya=py
    pxa2=pxa
    pya2=pya
    pxa3=pxa2
    pya3=pya2
    xx=x
    yy=y
    xx2=xx
    yy2=yy
    en1an=en1

           
