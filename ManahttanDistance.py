"""
For the following exercise I am  going to subtract the cartesian points given.
It will follow the simple algorithm of Destination - Initial Position = Distance

e.g. Destination      = (2,2)
     Initial Position = (-1,1)

     Distance = (2-(-1)) + (2 - 1) = 4
"""


choice = 0
routes = []
arr = [[2,34,5],[1234,4,3],[3,4,3,3]]
print(arr)


def distance(destination, start):
    dist = (destination[0] - start[0]) + (destination[1] - start[1])
    return dist

# Choose if you want to input your own coordinates
while choice != 1 and choice != 2:
    choice = int(input("Do you want to upload from a file (1) or input coordinates (2)"))

if choice == 1:
    # Make sure that examples.txt is in the same directory as ManhattanDistance.py, if you are receiving errors
    examples = open("paths.txt", 'r')
    routes = examples.read()
    length = int(len(routes) // 8)
    print(type(routes))
    for i in range(0, length, 2):
        answer = distance(int(routes[i]), int(routes[i + 1]))

    examples.close()

elif choice == 2:
    # Input from user and make sure the input fits the correct format
    pass

