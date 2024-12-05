import sys
import numpy as np
from scipy.signal import convolve2d
from scipy.ndimage import rotate

char_to_num = {'X': 0, 'M': 2, 'A': 3, 'S': 5}
count_67 = 0
kernel = np.array([[5, 0, 5],
               [0, 3, 0],
               [2, 0, 2]])
matrix = None

while True:
    row = sys.stdin.readline().strip()
    if not row:
        break
    array = np.array([char_to_num[char] for char in row])
    if matrix is None:
        matrix = array
    else:
        matrix = np.vstack([matrix, array])
    if matrix.shape[0] == 4:
        matrix = np.delete(matrix, (0), axis=0)
    if matrix.shape[0] != 3: continue
    for i in range(4):
        conv = convolve2d(matrix, kernel, mode='valid')
        count_67 += (conv == 67).sum()
        kernel = rotate(kernel, 90)
print(count_67)