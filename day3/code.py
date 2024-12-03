import re
import sys

regex = r"mul\((\d+),(\d+)\)"

total_sum = 0

if len(sys.argv) < 2:
    print("Usage: python script.py <input_file>")
    sys.exit(1)
input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            for match in re.finditer(regex, line):
                first_number = int(match.group(1))
                second_number = int(match.group(2))
                total_sum += first_number * second_number
                print(f"Full match: {match.group(0)}")
                print(f"First number: {first_number}")
                print(f"Second number: {second_number}")
                print(f"Current Sum: {total_sum}")

    # Print the final sum
    print(f"Final Sum: {total_sum}")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)
