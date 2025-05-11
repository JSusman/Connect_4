import numpy as np

grid = np.zeros((6,7))

for i in range(0,len(grid)):
  grid[i] = i
  for j in range(0,7):
    for k in range(0,6):
     n = j + (7*i)
      
    grid[i,j] = n
    

print(grid)