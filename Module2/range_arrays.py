"""Practice creating arrays from ranges
"""
import numpy as np

def main():
    """Driven Function
    """
    # generate 1D arrays from 0 to 8
    array = np.arange(9)
    print(array)
    # you may have negative numbers
    array = np.arange(-4,4)
    print(array)
    # add a step to each increment
    array = np.arange(-8,8,2)
    print(array)

    # generate an array with values from 0 to 5 in steps of 0.1
    array = np.arange(0,5,0.1)
    print(array)


if __name__ == '__main__':
    main()
