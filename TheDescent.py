import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

# game loop

while True:
    mountains=[]
    for i in xrange(8):
        mountains.append(int(raw_input()))  # represents the height of one mountain.

    # The index of the mountain to fire on.
    print mountains.index(max(mountains))
