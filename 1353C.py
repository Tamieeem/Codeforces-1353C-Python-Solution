t = int(input())
for i in range(t):
    min_moves = 0
    n = int(input())
    if n == 1:
        print(0)
    elif n == 3:
        print(8)
    else:
        formula = ((n+1)//2)   #this simply gives us the center position(consider the center as that one cell where we want to move all the items/cells.
        temp = n               #storing in in a temporary variable as we need to use it in the loop and manipulate it to reach our final output.
        mid = (temp+1)//2      #the variable says what it really means, the middle position of n*n matrix.
        for j in range(n-formula):      #loop should run untill you have 3*3 matrix cause this has only one outer cell. That's why we considered it as base case
            min_moves+=((temp**2) - ((temp-2)**2))*(temp - mid)    #this is basically the algorithm to get the number of outer cell in a matrix. Do some work on paper, you will understand.
            temp = (temp-2)                          #temp-2 because, our n is odd. so 7-2 is 5, 5-2 is 3, this is how the odd matrix continues in case you have larger matrix.
            mid = (temp+1)//2                        #you need to get new mid each time you finish one outer cell 
        print(min_moves)
        
        
        
        
                    
