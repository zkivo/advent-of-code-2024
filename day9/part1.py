# read line file input.txt
with open('input.txt', 'r') as file:
    line = file.readline()

# line = '2333133121414131402'

new_line = []

block = 0
for i, c in enumerate(line):
    if i % 2 == 0: 
        for _ in range(int(c)):
            new_line.append(str(block))
        block += 1
    else:
        for _ in range(int(c)):
            new_line.append('.') 

for i in range(len(new_line) - 1, -1, -1):
    if new_line[i] != '.':
        punto = new_line.index('.')
        if punto >= i:
            break
        new_line[punto] = new_line[i]
        new_line[i] = '.'

sum = 0
for i, c in enumerate(new_line):
    if c == '.': break
    sum += i * int(c)
print(sum)
