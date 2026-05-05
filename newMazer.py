import random

def hasValidPaths(maze, curX, curY):
    validPaths = []
    if(curX < width-1 and maze[curX+1][curY] == 0):
        validPaths.append((curX+1, curY))
    if(curX > 0 and maze[curX-1][curY] == 0):
        validPaths.append((curX-1, curY))
    if(curY < height-1 and maze[curX][curY+1] == 0):
        validPaths.append((curX, curY+1))
    if(curY > 0 and maze[curX][curY-1] == 0):
        validPaths.append((curX, curY-1))
        
    return validPaths

def createMaze(maze,curX,curY):
    maze[curX][curY] = 1
    print(f"Now at {curX},{curY}")
    
    if(curX == finish[0] and curY==finish[1]):
        print ("YAY!!!")
    
    while True:
        paths = hasValidPaths(maze, curX, curY)
        if(len(paths) == 0):
            return
        else:
            path = random.choice(paths)
            createMaze(maze, path[0], path[1])
            
            
def printMaze(maze):
    for y in range(height):
        for x in range(width):
            print(maze[x][y], end=" ")
        print() # Print a newline after printing the row.

def printPrettyMaze(maze, markX=None, markY=None):
    """Displays the maze data structure in the maze argument. The
    markX and markY arguments are coordinates of the current
    '@' location of the algorithm as it generates the maze."""

    for y in range(height):
        for x in range(width):
            if markX == x and markY == y:
                # Display the '@' mark here:
                print(MARK, end='')
            else:
                # Display the wall or empty space:
                print(maze[(x, y)], end='')
        print() # Print a newline after printing the row.

height = 19
width = 23
start = (0,0)
finish = (random.randint(start[0], width), height -1)

print(f"start is {start} and finish is {finish}")

maze = [[0 for _ in range(height)] for _ in range(width)]
printMaze(maze)
createMaze(maze, start[0], start[1])
printMaze(maze)

# Use these characters for displaying the maze:
EMPTY = ' '
MARK = '@'
WALL = chr(9608) # Character 9608 is '█'
NORTH, SOUTH, EAST, WEST = 'n', 's', 'e', 'w'

prettyMaze = {}
for x in range(width):
    for y in range(height):
        prettyMaze[(x, y)] = WALL # Every space is a wall at first.

printPrettyMaze(prettyMaze)