import numpy as np
print('Array data type conversion :-\n')
array = np.array([9.2, 5.6])
print(f'actuall data type {array.dtype}')
array = array.astype(np.int64)
print(f'After changing data type {array.dtype}')