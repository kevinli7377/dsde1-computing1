grid=[['.','.','.','.','.','.'],
     ['.','o','o','.','.','.'],
     ['o','o','o','o','.','.'],
     ['o','o','o','o','o','.'],
     ['.','o','o','o','o','o'],
     ['o','o','o','o','o','.'],
     ['o','o','o','o','.','.'],
     ['.','o','o','.','.','.'],
     ['.','.','.','.','.','.']]

#def gridp(list):
    #for i in len(len(list)):
        #print (list[i])

for i in range(6):
     for j in range(9): 
         print(grid[j][i], end='') #look carefully that j is before i. [1,0], [2,0], ...
     print('') # the end='' prompts the line not to enter a space after each iteration but a space.
