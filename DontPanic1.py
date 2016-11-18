import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

 # nb_floors: number of floors
 # width: width of the area
 # nb_rounds: maximum number of rounds
 # exit_floor: floor on which the exit is found
 # exit_pos: position of the exit on its floor
 # nb_total_clones: number of generated clones
 # nb_additional_elevators: ignore (always zero)
 # nb_elevators: number of elevators
elv={}
elva=[]
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in raw_input().split()]
for i in xrange(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    #elevator_floor, elevator_pos = [int(j) for j in raw_input().split()]
    elva.append([int(j) for j in raw_input().split()])
    elv[elva[i][0]]=elva[i][1]
# game loop
while 1:
     # clone_floor: floor of the leading clone
     # clone_pos: position of the leading clone on its floor
     # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = raw_input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    if clone_floor==exit_floor or clone_floor==-1 :
        if clone_pos>exit_pos and direction=='RIGHT':
            print 'BLOCK'
        elif clone_pos<exit_pos and direction=='LEFT':
            print 'BLOCK'
        else:
            print "WAIT"
    else:
        if nb_floors>0:
            
            posi=elv[clone_floor]
            if clone_pos>posi and direction=='RIGHT':
                print 'BLOCK'
            elif clone_pos<posi and direction=='LEFT':
                print 'BLOCK'
            else:
                print "WAIT"
        
