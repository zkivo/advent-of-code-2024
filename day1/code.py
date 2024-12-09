import numpy as np

# Read the file and extract the numbers
file_path = 'input.txt'

# Read and process the file
with open(file_path, 'r') as file:
    # Split each line into two integers and store them as tuples in a list
    numbers = [list(map(int, line.split())) for line in file]

numbers = np.array(numbers)
numbers = np.sort(numbers, axis=0)
differences = np.abs(numbers[:, 1] - numbers[:, 0])
total_difference = sum(differences)

sum = 0
for number in np.unique(numbers[:, 0]):
    # get rows where number appear in second column
    indices = np.where(numbers[:, 1] == number)[0]
    sum += np.sum(number * len(indices))

# Print the results
print(f'Sum of differences: {total_difference}')
print(f'Second part: {sum}')