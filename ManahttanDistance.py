"""
For the following exercise I am  going to subtract the cartesian points given.
It will follow the simple algorithm of Destination - Initial Position = Distance

e.g. Destination      = (2,2)
     Initial Position = (-1,1)

     Distance = (2-(-1)) + (2 - 1) = 4
"""


routes = []


def distance(destination, start):
    dist = (destination[0] - start[0]) + (destination[1] - start[1])
    return dist


# Make sure that examples.txt is in the same directory as ManhattanDistance.py, if you are receiving errors
examples = open("examples.txt", 'r')




examples.close()