import numpy as np

# File path to the input file
file_path = 'input.txt'

with open(file_path, 'r') as file:
    matrix = np.loadtxt(file, dtype=int)

sum = 0
for i, row in enumerate(matrix):
    print(row)
    asc = None
    redo = False
    valid = True
    while valid:
        for j, number in enumerate(row):
            if j == len(row) - 1: continue
            left, right = row[j], row[j + 1]
            if j == 0: # ascending or descending
                if right - left > 0:
                    asc = True
                else:
                    asc = False
            diff = right - left
            if diff * asc < 0:
                print(f"{row[j]}, {row[j+1]}: not monotone")
                # remove the right element
                row = np.delete(row, j + 1)
                if redo == True:
                    redo = False
                    valid = False
                    break
                redo = True
                break
            else:
                diff = abs(diff)
                if diff < 1 or diff > 3:
                    print(f"diff({row[j]}, {row[j+1]})= {diff}, not in range")
                    row = np.delete(row, j + 1)
                    if redo == True:
                        redo = False
                        valid = False
                        break
                    redo = True
                    break
        if redo:
            continue
        if valid:
            sum += 1
            break
print(sum)

