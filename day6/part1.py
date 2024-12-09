import sys
import os
import time

def read_map(file_path):
    """Reads a map from a text file and returns it as a 2D list of characters."""
    with open(file_path, 'r') as file:
        map_data = [list(line.strip()) for line in file]
    return map_data

def print_green_number(number):
    """Prints a number in green below the map."""
    sys.stdout.write(f"\033[32m{number}\033[0m\n")  # Print the number in green
    sys.stdout.flush()  # Force the output to be displayed

def find_character_coordinates(map_data, char):
    """Finds the 2D coordinates of the first occurrence of a character in the map."""
    for row_idx, row in enumerate(map_data):
        if char in row:
            col_idx = row.index(char)
            return (row_idx, col_idx)  # Return as (row, column) coordinates
    return None  # Return None if character is not found

def print_map(map_data):
    """Prints the map in the terminal without new lines and updates it in place."""
    sys.stdout.write("\033[H")  # Move cursor to the top-left corner of the terminal
    for row in map_data:
        sys.stdout.write(''.join(row) + '\n')
    sys.stdout.flush()  # Force the output to be displayed

# Clear the terminal (OS-dependent)
if os.name == 'nt':  # Windows
    os.system('cls')
else:  # Unix-based systems
    os.system('clear')

file_path = 'input.txt'  # Path to the input file
map = read_map(file_path)
character = '^'  # Replace with the character you want to find
row_idx, col_idx = find_character_coordinates(map, character)
sum = 0
direction = 'up'
while row_idx >= 0 and row_idx < len(map) and col_idx >= 0 and col_idx < len(map[0]):
    time.sleep(0.001)  # Slow down the execution to make the movement visible
    print_map(map)
    print_green_number(f"Path: {sum}")  # Print the sum of the visited cells
    current_char = map[row_idx][col_idx]
    if current_char == '.' or current_char == '^':
        sum += 1
        map[row_idx][col_idx] = 'X'
    elif current_char == '#':
        if direction == 'up':
            row_idx += 1
            col_idx += 1
            direction = 'right'
        elif direction == 'right':
            row_idx += 1
            col_idx -= 1
            direction = 'down'
        elif direction == 'down':
            row_idx -= 1
            col_idx -= 1
            direction = 'left'
        elif direction == 'left':
            row_idx -= 1
            col_idx += 1
            direction = 'up'
        continue
    if direction == 'up':
        row_idx -= 1 
    elif direction == 'right':
        col_idx += 1
    elif direction == 'down':
        row_idx += 1
    elif direction == 'left':
        col_idx -= 1
print_map(map)
print_green_number(f"Path: {sum}")  # Print the sum of the visited cells