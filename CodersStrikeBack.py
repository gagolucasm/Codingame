import sys
import math

once=True

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    maxim=90
    minim=65
    b=-(100/(maxim-minim))
    a=-maxim*b
   
    # Write an action using print
    print("A...",a, file=sys.stderr)
    print("B...",b, file=sys.stderr)
    absangle=abs(next_checkpoint_angle)
    print("Angle...",absangle, file=sys.stderr)
    ex=min(absangle,90.0)
    print("X...",x, file=sys.stderr)
    thrust=a+b*ex
    print("thrust...",thrust, file=sys.stderr)

    
    if(next_checkpoint_angle < 15 and next_checkpoint_angle >-15 and next_checkpoint_dist>7000 and once):
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) +" "+ "BOOST")
        once=False
    else:
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) +" "+ str(int(min(thrust,100))))
