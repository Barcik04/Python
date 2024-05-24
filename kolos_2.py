NUMPY
        WHERE
            import numpy as np
            
            arr = np.array([1, 2, 3, 4, 5])
            result = np.where(arr > 2, arr * 2, arr - 2)
            print(result)
            # Output: [-1  0  6  8 10]
            
            The np.where function works as follows: np.where(condition, x, y) returns elements chosen from x or y depending on the condition. 
            If the condition is True for an element, the corresponding element from x is taken; otherwise, the element from y is taken.
    
        SUM
            arr = np.array([[1, 2, 3], [4, 5, 6]])
            result = np.sum(arr, axis=0)
            print(result)
            # Output: [5 7 9]
            
            axis=0: This means we want to sum the elements along the vertical axis (i.e., column-wise summation).
    
        MEAN
            arr = np.array([1, 2, 3, 4, 5])
            result = np.mean(arr)
            print(result)
            # Output: 3.0
            
            The np.mean function computes the arithmetic mean along the specified axis.
    
        MEDIAN
            arr = np.array([1, 3, 5, 7, 9])
            result = np.median(arr)
            print(result)
            # Output: 5.0
            
            The np.median function computes the median of array elements along the specified axis.
    
        ARG MAX/MIN
            arr = np.array([1, 3, 7, 6, 2])
            result = np.argmax(arr)
            result2 = np.argmin(arr)
            print(result)
            # Output: 2 
            
            The np.argmax function returns the indices of the maximum values along an axis.
    
        RESHAPE
            arr = np.array([1, 2, 3, 4, 5, 6])
            result = np.reshape(arr, (2, 3))
            print(result)
            # Output:
            # [[1 2 3]
            #  [4 5 6]]
    
        CONCATENATE
            arr1 = np.array([1, 2, 3])
            arr2 = np.array([4, 5, 6])
            result = np.concatenate((arr1, arr2))
            print(result)
            # Output: [1 2 3 4 5 6]
    
        UNIQUE
            arr = np.array([1, 2, 2, 3, 4, 4, 5])
            result = np.unique(arr)
            print(result)
            # Output: [1 2 3 4 5]
    
        LINESPACE
            result = np.linspace(0, 10, 5)
            print(result)
            # Output: [ 0.   2.5  5.   7.5 10. ]
    
        ARRANGE
            result = np.arange(0, 10, 2)
            print(result)
            # Output: [0 2 4 6 8]
    
        DOT
            arr1 = np.array([1, 2, 3])
            arr2 = np.array([3, 4, 2])
            result = np.dot(arr1, arr2)
            print(result)
            # Output: 17 (1*3) + (2*4) + (3*2)
    
        RANDOM.RANDINT
            result = np.random.randint(1, 10, size=(3, 2))
            print(result)
            # Output:
            # [[3 6]
            #  [4 7]
            #  [2 9]]
    
            The np.random.randint function returns random integers from low (inclusive) to high (exclusive).





    
