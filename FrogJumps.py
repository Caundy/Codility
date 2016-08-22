from __future__ import division
import math

def solution(X,Y,D):
    if(X,Y,D > 0) and (Y > X):
        jumps = int(math.ceil((Y-X)/D))
    elif (X >= Y):
        jumps = 0
    return jumps



solution(5, 105, 3)

print math.ceil(100/3)
