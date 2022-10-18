# Telepathy

Solution to question given in Telepathy labs.
install all requirements
Run solution_bfs.py

Do you want to enter manually enter 1 or otherwise default matrice will be used

if 1:
Enter matrice and time accordingly will be computed


if any other number
default matrix initialized in main will be used


**************To run unit test************



Run test_solutio.py
pytest test_solutio.py


Solution described :
The problem is a traversal problem hence using graph algorithm ,choosing bfs since its best when sources closer to given source and will give optimal time for given problem and using multisource since at a single unit of time multiple infected patients can infect others.

Approach:
1.Initialize the number of time to 0.
2.Declare a queue  and push all the cells containing infected patientss into it one by one.
3.While the queue is not empty, pop the cell from the front of the queue, and try to go all its neighbors in 4 directions, keeping check that they lie within the boundary of the matrix, and changing their values to 2(infected). Push all these adjacent into the queue, and continue the algorithm until the next iteration.
4.Keep updating the time passed variable , and continue the algorithm till all the cells are visited.
5.Iterate through the matrix again and if any uninfected patient is found, return -1.
6.Else return the time passed.
