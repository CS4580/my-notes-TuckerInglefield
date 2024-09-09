"""Practice some of numpy array identities
"""
import numpy as np

def main():
    """Driven Function
    """
    # create a 2D 3x3 identity matrix
    identity_3x3 = np.eye(3,3)
    print(identity_3x3)
    # 2D diagonal arrays, with given entries
    diagonal_2D = np.diag([2,3,4,5])
    print(diagonal_2D)

    # create a 5x3 2D array of sunigned integers filled with zeros
    arr_5x3_zeros = np.zeros((5,3), dtype=np.uint)
    print(arr_5x3_zeros)
    # create a 5x3 2D array of sunigned integers filled with ones
    arr_5x3_zeros = np.ones((5,3), dtype=np.uint)
    print(arr_5x3_zeros)
    # create a 5x3 2D array of sunigned integers filled with a specific val
    arr_5x3_custom = np.full((5,3), 5, dtype=np.uint)
    print(arr_5x3_custom)

    # create a 5x3 2D array of sunigned integers filled with random numbers
    arr_5x3_random = np.random.random((5,3))
    print(arr_5x3_random)

if __name__ == '__main__':
    main()
