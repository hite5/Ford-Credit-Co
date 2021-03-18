"""
For the following exercise I am  going to subtract the cartesian points given.
It will follow the simple algorithm of Destination - Initial Position = Distance

e.g. Destination      = (2,2)
     Initial Position = (-1,1)

     Distance = (2-(-1)) + (2 - 1) = 4
"""

# function that makes sure the user wants to do the task again
def proceed_again(i):
    output = ['continue', 'input coordinates']
    while True:
        print("Do you wish to", output[i], "again?")
        again = input("(Y/N): ")
        if again == 'y' or again == 'Y':
            return True
        elif again == 'n' or again == 'N':
            return False
        else:
            print("You did not input a valid answer.")


# function that gives the answer to the problem
def distance(startX, startY, destX, destY):
    dist = (destX - startX) + (destY - startY)
    return dist

# this function decides which path the user wants to go down.
# If he/she wants to input her own data or use data from a .txt file
def engine():
    routes = []
    choice = 0
    # Choose if you want to input your own coordinates
    while choice != 1 and choice != 2:
        choice = int(input("Do you want to upload from a file (1) or input coordinates (2): "))
        if choice != 1 and choice != 2:
            print("You inputted a invalid number. Please try again.")

    if choice == 1:
        # Make sure that examples.txt is in the same directory as ManhattanDistance.py, if you are receiving errors
        # Go through the text file and retrieve the data in there and assign it to a 2D array.
        # Iterate through the 2D array and send the data to the distance function
        # Function returns an int. The int must be a positive value, because distance isn't a vector.
        examples = open("paths.txt", 'r')
        for line in examples.readlines():
            routes.append(line.strip('\n').split(','))
        length = len(routes)
        for i in range(0, length, 2):
            answer = abs(distance(int(routes[i][0]), int(routes[i][1]), int(routes[i+1][0]), int(routes[i+1][1])))
            print("Your total distance between", routes[i], "and", routes[i+1], "is =", answer, "\n\n")

        examples.close()

    elif choice == 2:
        # Input from user and make sure the input fits the correct format
        # The input is going to ask for a single value for each of the 4 position start(x,y) destination(x,y)
        proceed = True
        while proceed:
            try:
                startx = int(input("Enter the starting x position: "))
                starty = int(input("Enter the starting y position: "))
                destx = int(input("Enter the destination x position: "))
                desty = int(input("Enter the destination y position: "))
            except:
                print("You did not enter a valid entry.")
                continue
            answer = distance(startx, starty, destx, desty)
            print("Your total distance between (",startx,",",starty,') and (',startx,",",starty,') is =', answer, "\n\n")
            proceed = proceed_again(1)

allowed = True

while allowed:
    engine()
    allowed = proceed_again(0)