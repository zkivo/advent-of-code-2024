# Read the input from the file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Parse the first couple of numbers into a matrix with two columns
order = []
for line in lines:
    if '|' in line:
        num1, num2 = map(int, line.strip().split('|'))
        order.append([num1, num2])
    else:
        break  # Stop processing after reading the first segment

# Process the last lines, assuming they contain comma-separated values
middles = []
last_lines_start = len(order) + 1
for line in lines[last_lines_start:]:
    numbers = list(map(int, line.strip().split(',')))
    prev = None
    fail = False
    for i, number in enumerate(numbers):
        if i == 0:
            prev = number
            continue
        filtered_order = [row[0] for row in order if row[1] == number]
        if prev not in filtered_order:
            fail = True
            break
        prev = number
    if not fail:
        print(numbers)
        middles.append(numbers[len(numbers) // 2])

# sum of all middle numbers
print(sum(middles))