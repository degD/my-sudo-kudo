
def move_f(y, x):
    if x < 8:
        x += 1
    else:
        y += 1
        x = 0
        
    return y, x
        
def move_b(y, x):
    if x > 0:
        x -= 1
    else:
        y -= 1
        x = 8
        
    return y, x

def square_index(y, x):
    return (x // 3) + (y // 3)*3
      
def crt_sqr_list(y, x):
    my, mx = (y // 3), (x // 3)
    l = []
    for iy in range(my, my+3):
        for ix in range(mx, mx+3):
            l.append(puzzle[iy][ix])
    return l

def crt_col_list(x):
    return [puzzle[n][x] for n in range(9)]


puzzle = []
        
puzzle_squares = {}
puzzle_columns = {}
init_val = y = x = 0
while True:

    if puzzle[y][x]:
        y, x = move_f(y, x)
    
    else:
        
        sqi = square_index(y, x)
        try:
            squ_list = puzzle_squares[sqi]
        except IndexError:
            puzzle_squares[sqi] = crt_sqr_list(y, x)
            continue
        
        try:
            column = puzzle_columns[x]
        except IndexError:
            puzzle_columns[x] = crt_col_list(x)
            continue
        
        row = puzzle[y]
        
        found_value = False
        for num in range(init_val+1, 10):
            if (num not in squ_list) and (num not in column) and (num not in row):
                found_value = True
                break
            
        if found_value:
            squ_list.remove(0)
            squ_list.append[num]
            column[y] = num
            puzzle[y][x] = num
            
            init_val = 0        
