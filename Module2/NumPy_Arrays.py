"""NumPy Arrays
"""
import numpy as np

def main():
    """Driven Function
    """
    # 1D Arrays
    # Create an array
    print('1D Arrays:')
    array = np.array([-2,1,-5, 10])
    print(array, type(array))

    numbers = [-2,1,5,10]
    print(numbers, type(numbers))
    # convert list into arrays
    new_array = np.array(numbers)
    print(new_array, type(new_array))
    print()

    # 2D Arrays
    print('2D Arrays:')
    matrix = np.array([[-1,0,4],[-3,6,9]])
    print(matrix)
    print()

    # 3D Arrays
    print('3D Arrays:')
    array3d = np.array([[[-1,2,3],[3,5,7]], [[4,6,8],[3,2,5]]])
    print(array3d)
    print()

    # use the dytpe optional argument to call the type of the array
    numbers = [-2,1,5,10]
    new_array = np.array(numbers, dtype=np.short)
    print(new_array, new_array.dtype)
    # unsigned data
    numbers = [2,1,5,10]
    new_array = np.array(numbers, dtype=np.ushort)
    print(new_array, new_array.dtype)
    # Float Data
    new_array = np.array(numbers, dtype=np.float32)
    print(new_array, new_array.dtype)

if __name__ == '__main__':
    main()
