import math

def leftmost(arr):
    if len(arr) == 1:
        return [min(arr[0])]
    return leftmost(arr[0:math.floor(len(arr)/2)]) + leftmost(arr[math.floor(len(arr)/2):len(arr)])


arr = [[10, 17, 13], 
     [17, 25, 16],
     [24, 28, 22]]

print(leftmost(arr))