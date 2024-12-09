import numpy as np

# File path to the input file
file_path = 'input.txt'

with open('input.txt', 'r') as file:
    lines = file.readlines()

def get_index(row):
    asc = None
    for i, number in enumerate(row):
        if i == len(row) - 1: continue
        left, right = row[i], row[i + 1]
        if i == 0: # ascending or descending
            if right - left > 0:
                asc = 1
            else:
                asc = -1
        diff = right - left
        if diff * asc < 0:
            return i
        diff = abs(diff)
        if diff < 1 or diff > 3:
            return i
    return None

sum = 0
for row in lines:
    row = np.array([int(x) for x in row.split()])
    ret = get_index(row)
    if ret is None:
        sum += 1
        continue
    for i in range(len(row)):
        new_row = np.delete(row, i)
        if get_index(new_row) is None:
            sum += 1
            print(new_row, 'safe')
            break
    print(row, 'unsafe')
print(sum)

