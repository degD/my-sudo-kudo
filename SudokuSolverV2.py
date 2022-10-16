

    
def movement(y, x):
   
    if ((x+1) % 9 == 0) and ((y+1) % 3 == 0):
        x = 0
        y += 1
    
    elif ((x+1) % 3 == 0) and ((y+1) % 3 == 0):
        x += 1
        y -= 2

    elif ((x+1) % 3 != 0):
        x += 1
    
    elif ((x+1) % 3 == 0):
        x -= 2
        y += 1
        
    return y, x

def movementr(y, x):
    
    if (x % 9 == 0) and (y % 3 == 0):
        x = 8
        y -= 1
    
    elif (x % 3 == 0) and (y % 3 == 0):
        x -= 1
        y += 2

    elif (x % 3 != 0):
        x -= 1
    
    elif (x % 3 == 0):
        x += 2
        y -= 1
        
    return y, x

        