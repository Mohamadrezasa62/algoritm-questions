# get input
n = input()
loc = []
# create 2D matrix for location of snake
for i in range(2):
    location = []
    for j in range(8):
        location.append(0)
    loc.append(location)
# set first state of location
x = 1
y = 0
loc[x][y] = 1

# set default of dead to False that means the snake is alive now
dead = False
# check movements and change location of snake
for i in n:
    if i == 'F':
        x, y = [x, y+1]
        if x > 1 or y > 7 or x < 0 or y < 0:
            dead = True
            break
        loc[x][y] = 1
    elif i == 'L':
        x, y = [x-1, y+1]
        if x > 1 or y > 7 or x < 0 or y < 0:
            dead = True
            break
        loc[x][y] = 1
    elif i == 'R':
        x, y = [x+1, y+1]
        if x > 1 or y > 7 or x < 0 or y < 0:
            dead = True
            break
        loc[x][y] = 1

# check that the snake is dead or not
if dead:
    print('DEATH')
# print location 2D matrix when the snake isn't dead
else:
    for i in range(2):
        for j in range(8):
            print(loc[i][j], end='')
        print()
