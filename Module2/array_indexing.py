"""Array Indexing
"""
import numpy as np

def main():
    """Driven Function
    """
    # 1D Arrays
    arr_1d = np.arange(10)
    # access the second element
    print(arr_1d[1])
    # access the last element
    print(arr_1d[-1])

    # 2D Arrays
    arr_2d = np.array([[21,22,23,24], [31, 32, 34, 34], [41, 42, 43, 44]])
    print(arr_2d[0][0]) # 21
    print(arr_2d[2][-2]) # 43
    print(arr_2d[1]) # full 2nd row

    # Slicing
    arr_1d = np.arange(10)
    print(arr_1d) # all elements
    print(arr_1d[:2]) # up to an index
    print(arr_1d[2:]) # from an index
    print(arr_1d[1:5]) # between two index's
    

if __name__ == '__main__':
    main()