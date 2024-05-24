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

    ARG MAX
        arr = np.array([1, 3, 7, 6, 2])
        result = np.argmax(arr)
        print(result)
        # Output: 2 
        
        The np.argmax function returns the indices of the maximum values along an axis.
