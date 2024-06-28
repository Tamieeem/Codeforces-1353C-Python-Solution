t = int(input())
for i in range(t):
    min_moves = 0
    n = int(input())
    if n == 1:
        print(0)
    elif n == 3:
        print(8)
    else:
        formula = ((n+1)//2)
        temp = n
        mid = (temp+1)//2
        for j in range(n-formula):
            min_moves+=((temp**2) - ((temp-2)**2))*(temp - mid)
            temp = (temp-2)
            mid = (temp+1)//2
        print(min_moves)
        
        
        
                    