import numpy as np

def infect(grid):

    r = len(grid)
    c = len(grid[0])
    uninfected = 0
    queue = []
    vis = set()
    #push all infected patients into a queue
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
                vis.add((i, j))
            elif grid[i][j] == 1:
                uninfected += 1
    if not uninfected:
        return 0
    #pop queue and checking neighbors if infected 
    while queue:
        size = len(queue)
        #visiting neighbours
        while size:
            x, y, days = queue.pop(0)
            if x < r - 1 and (x + 1, y) not in vis and grid[x + 1][y] == 1:
                queue.append((x + 1, y, days + 1))
                vis.add((x + 1, y))
                uninfected -= 1
            if x > 0 and (x - 1, y) not in vis and grid[x - 1][y] == 1:
                queue.append((x - 1, y, days + 1))
                vis.add((x - 1, y))
                uninfected -= 1
            if y < c - 1 and (x, y + 1) not in vis and grid[x][y + 1] == 1:
                queue.append((x, y + 1, days + 1))
                vis.add((x, y + 1))
                uninfected -= 1
            if y > 0 and (x, y - 1) not in vis and grid[x][y - 1] == 1:
                queue.append((x, y - 1, days + 1))
                vis.add((x, y - 1))
                uninfected -= 1
            size -= 1
    return -1 if uninfected else days

def checksize():
    global v
    return(np.shape(v))

def take_input():
	

#Take dimension of matrix
	global r
	global c
	r = int(input("Enter the number of rows:"))
	c = int(input("Enter the number of columns:"))

# Initializing empty matrix
	A = []


# Matrix A user input
	print (" \n Enter matrix elements(row wise): \n")
	for i in range(r):		 
		a =[]
		for j in range(c):	
			a.append(int(input()))
		A.append(a)


# Print matrix A
	print (" \nYou have entered the given matrix  \n")
	for i in range(r):
		for j in range(c):
			#print(A[i][j], end = " ")
			v=A
	return(v)
	print(A)

if __name__ == "__main__":

	v = [[2, 2, 2, 2, 2],
		[2, 2, 2, 2, 2],
		[2, 2, 2, 2, 2]]
	i=int(input("Do you want to enter manually enter 1 or otherwise default matrice will be used"))

	if(i==1):
		v=take_input()
		print(v)
		print("Max time incurred to infect: ",
		infect(v))

	else:
		print("Max time incurred to infect: ",
		infect(v))