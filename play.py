import random

def create_maze(height, width):
    maze = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        maze.append(row)
    return maze

def move(direction):
    if direction == 0:
        print("Moving up")
    elif direction == 1:
        print("Moving right")
    elif direction == 2:
        print("Moving down")
    elif direction == 3:
        print("Moving left")

def print_maze(maze):
    for row in maze:
        print(" ".join(str(cell) for cell in row))

height = 7
width = 7
maze = create_maze(height, width)

for i in range(height):
    row = []
    for j in range(width):
        row.append(0)
    maze.append(row)

print_maze(maze)

direction = random.randint(0, 3)
print(direction)

