
def SudokuSolver(puzzle):
    """Solves the given 9x9 sudoku and returns the result. 
    Returns 0 if the sudoku is unsolvable"""
    
    def square_index(y, x):
        return (x // 3) + (y // 3)*3
    
    def square_coords(y, x):
        return (y // 3), (x // 3)

    # Defining some values prior to start
    puzzle_3x3_data = [list() for _ in range(9)]
    puzzle_columns = [list() for _ in range(9)]
    
    for y in range(9):
        for x in range(9):
            
            sqi = square_index(y, x)
            puzzle_3x3_data[sqi].append(puzzle[y][x])
            puzzle_columns[x].append(puzzle[y][x])
            
    # Some variables for the main algorithm loop
    mx = my = x = y = 0
    init_val = 0
    past_coords = []

    # Main algorithm loop
    while my < 3:
        
        if puzzle[y][x] == 0:
            
            sqi = square_index(y, x)
            
            squ_list = puzzle_3x3_data[sqi]
            col_list = puzzle_columns[x]
            row_list = puzzle[y]
            
            for num in range(init_val+1, 10):
                if (num not in squ_list) and (num not in col_list) and (num not in row_list):
                    puzzle[y][x] = num
                    break
                
            if puzzle[y][x]:
                squ_list.remove(0)
                squ_list.append(num)
                col_list[y] = num
                
                init_val = 0
                past_coords.append((y, x))
                
            else:
                try:
                    y, x = past_coords.pop()
                except IndexError:
                    return 0
                init_val = puzzle[y][x]
                puzzle[y][x] = 0

                sqi = square_index(y, x)
                squ_list = puzzle_3x3_data[sqi]
                squ_list.remove(init_val)
                squ_list.append(0)
                col_list = puzzle_columns[x]
                col_list[y] = 0
                
                my, mx = square_coords(y, x)
                
                continue
    
    # Movement unit. Change it to alter how coordinates are changed.
        if x < mx*3+2:
            x += 1
        else:
            x -= 2
            y += 1
                
        if y == my*3+3:
            
            if mx < 2:
                mx += 1
            else:
                mx = 0
                my += 1
                
            x = mx*3
            y = my*3
               
    return puzzle
        
# HOW IT WORKS:
# Iterates over each coordinate as defined by movement unit. And if it's 0, then 
# tries to find a number between 1-9, that doesn't exist in its row, column,
# and 3x3 square. If this number exists, algorithm skips to next coordinate. Else, 
# goes to the former numerated coordinate, and tries to find another value for it.
# The code exits when Sudoku gets completed or it finds out it is impossible to complete it.


if __name__ == '__main__':
    
    import time
    
    def sudoku_test(puzzle, solution=False):
        """Test the sudoku algorithm. Print the time it take to solve.
        Also check with solution if given. And print a message by the results."""
        
        start = time.perf_counter()
        result = SudokuSolver(puzzle)
        stop = time.perf_counter()
        
        if result and result == solution:
            print("Sudoku solved right ", end='')
        
        time_ms = int(round(stop-start, 3)*1000)
        print(f"{time_ms}ms")

    # Test case 1: An easy sudoku
    puzzle1 = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]

    solution1 = [[5,3,4,6,7,8,9,1,2],
                [6,7,2,1,9,5,3,4,8],
                [1,9,8,3,4,2,5,6,7],
                [8,5,9,7,6,1,4,2,3],
                [4,2,6,8,5,3,7,9,1],
                [7,1,3,9,2,4,8,5,6],
                [9,6,1,5,3,7,2,8,4],
                [2,8,7,4,1,9,6,3,5],
                [3,4,5,2,8,6,1,7,9]]
    
    sudoku_test(puzzle1, solution=solution1)
    
    # Test case 2: A hard sudoku
    problem = [[9, 0, 0, 0, 8, 0, 0, 0, 1],
               [0, 0, 0, 4, 0, 6, 0, 0, 0],
               [0, 0, 5, 0, 7, 0, 3, 0, 0],
               [0, 6, 0, 0, 0, 0, 0, 4, 0],
               [4, 0, 1, 0, 6, 0, 5, 0, 8],
               [0, 9, 0, 0, 0, 0, 0, 2, 0],
               [0, 0, 7, 0, 3, 0, 2, 0, 0],
               [0, 0, 0, 7, 0, 5, 0, 0, 0],
               [1, 0, 0, 0, 4, 0, 0, 0, 7]]
    
    sudoku_test(problem)
