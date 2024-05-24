NUMPY
    WHERE
        import numpy as np
        
        arr = np.array([1, 2, 3, 4, 5])
        result = np.where(arr > 2, arr * 2, arr - 2)
        print(result)
        # Output: [-1  0  6  8 10] explain
        
        The np.where function works as follows: np.where(condition, x, y) returns elements chosen from x or y depending on the condition. 
        If the condition is True for an element, the corresponding element from x is taken; otherwise, the element from y is taken.
