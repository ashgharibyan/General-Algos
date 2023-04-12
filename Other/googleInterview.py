# Given a Roomba Vacuum that only knows how to rotate right
# * by 90 degrees but will stay in the same position, and attempt
# * to move forward one unit (returns a status if it was successful), come up with an algorithm that traverses an entire rectangularly shaped room with no obstacles
# * Feel free to add more capabilities to the vacuum using what it already knows how to do: 
# public void rotateRight90();
# public boolean attemptToMoveForwardOne();

# [[-,-,-]
#  [-,-,-]
#  [-,-,-]]

class Roomba:
    directions = {
                    "r":"d",
                    "d":"l",
                    "l":"u",
                    "u":"r"
                }

    def __init__(self, room):
        self.room = room
        # [y,x]
        self.currPosition = [0,0]
        self.direction = "r"

    def rotateRight90(self):
        self.direction = Roomba.directions[self.direction]        
        print("Rotating Right, now facing: ", self.direction)

    def attemptToMoveForwardOne(self):
        tempPos = list(self.currPosition)

        if self.direction == "r":
            tempPos[1] += 1
        elif self.direction == "d":
            tempPos[0] += 1
        elif self.direction == "l":
            tempPos[1] -= 1
        elif self.direction == "u":
            tempPos[0] -= 1

        if tempPos[0] >= len(self.room) or tempPos[1] >= len(self.room[0]) or tempPos[0] < 0 or tempPos[1] < 0:
            print("Inside attempt if", tempPos)
            return False
        
        self.currPosition[0] = tempPos[0]
        self.currPosition[1] = tempPos[1]

        print("Moving forward", self.currPosition)
        return True
        
    

    def turn270(self):
        self.rotateRight90()
        self.rotateRight90()
        self.rotateRight90()
        print("Rotating Left, now facing: ", self.direction)



    # assume the robot starts facing right

    def traverseRoom(self, isRight = True):

        # flag for left or right

        #go one line until there is an obstacle, turn moveOne, and turn
        canMove = True
        while canMove:
            canMove = self.attemptToMoveForwardOne()
        
        # Turn
        if isRight:
            self.rotateRight90()
        else:
            self.turn270()

        # Check if it reached the finish
        isSpaceToMove = self.attemptToMoveForwardOne()
        if not isSpaceToMove:
            return True

        # Turn
        if isRight:
            self.rotateRight90()
            isRight = False
        else:
            self.turn270()
            isRight = True
        print("======== DONE ONE TRAVERSE")
        return self.traverseRoom(isRight)


if __name__ == "__main__":
    
    room = [["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]]
    
    print(room)
    roomba1 = Roomba(room)
    result = roomba1.traverseRoom()
    if result==True:
        print("True")
    else:
        print("False")


