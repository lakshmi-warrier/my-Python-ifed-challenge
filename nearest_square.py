import math

def nearest_square(num):
    if num<0:
        return 0
    return(math.floor(math.sqrt(num))**2)


