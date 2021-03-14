# This file contains the function to be optimized by the genetic algorithm
# as well as the definition of the accepted ranges for each variable and 
# any result restrictions that might exist.
from math import *
import numpy as np

#===== Definition of variables and their accepted ranges =====
ranges = [
    ["x",[-20.,20.]],
    ["y",[-20.,20.]]
]

def get_ranges():
    return(ranges)


#===== Definition of result restrictions =====






#===== Definition of function to be optimized =====
def main(x,y):
    #f1 = x * np.sin(4*x) + 1.1 * y * np.sin(2*y)
    f2 = -x * np.sin(np.sqrt(np.abs(x - (y + 9)))) - (y + 9) * np.sin(np.sqrt(np.abs(y + 0.5*x + 9)))
    return(np.reshape(f2,(-1,1)))


if __name__ == "__main__":
    main()