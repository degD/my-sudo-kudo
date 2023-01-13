
puzzle = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]]

def solve(puzzle):
    
    # Solution matrix
    
    solution = [list([0 for _ in range(9)]) for _ in range(9)]
    
    # Test functions
    
    def row_test(irow, num):
        if num in solution[irow]:
            return True
        return False
    
    def col_test(jcol, num):
        for i in range(9):
            if solution[i][jcol] == num:
                return True
        return False
    
    def box_test(i, j, num):
        itop = ((i)//3)*3
        jtop = ((j)//3)*3
        for i in range(itop, itop+3):
            for j in range(jtop, jtop+3):
                if num == solution[i][j]:
                    return True
        return False
    
    def general_test(i, j, num):
        if row_test(i, num):
            return True 
        if col_test(j, num):
            return True 
        if box_test(i, j, num):
            return True
        return False
    
    
    # Movement algorithms
    
    def move(i, j):
        if i < 8 and j < 8:
            j += 1
        elif i < 8:
            i += 1
            j = 0
        else:
            return False
        
        return i, j
    
    def rmove(i, j):
        if i > 0 and j > 0:
            j -= 1
        elif i > 0:
            i -= 1
            j = 8
        else:
            return False
        
        return i, j
        
        
    # Main algorithm
    
    i = j = 0
    while i < 8 and j < 8:
        
        if puzzle[i][j] == 0:
            number_found = 0
            for num in range(1, 10):
                if not general_test(i, j, num):
                    solution[i][j] = num
                    number_found = 1
                    break         
        else:
            number_found = 1
            solution[i][j] = puzzle[i][j]
            
        if number_found == 1:
            i, j = move(i, j)
        else:
            i, j = rmove(i, j)
            while puzzle[i][j] != 0:
                i, j = rmove(i, j)
                
    
    return solution


print(solve(puzzle))
        