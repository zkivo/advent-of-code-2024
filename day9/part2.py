# read line file input.txt
with open('input.txt', 'r') as file:
    line = file.readline()

# line = '2333133121414131402'

new_line = []

block = 0
for i, c in enumerate(line):
    if int(c) == 0:
        continue
    if i % 2 == 0:
        temp =[]
        for _ in range(int(c)):
            temp.append(str(block))
        new_line.append(temp)
        block += 1
    else:
        temp = []
        for _ in range(int(c)):
            temp.append('.')
        new_line.append(temp)


for b in range(block - 1, -1, -1):
    for i in range(len(new_line)):
        if new_line[i][0] != str(b):
            continue
        size = len(new_line[i])
        # print(new_line[i], size)
        # print(new_line)
        for j in range(len(new_line)):
            if j == i: break
            if new_line[j][0] == '.':
                free_space = len(new_line[j]) 
                # print(free_space, size)
                if free_space >= size:
                    diff = free_space - size
                    if diff == 0:
                        temp = new_line[i].copy()
                        new_line[i] = ['.' for _ in range(size)]
                        new_line[j] = temp
                    else:
                        temp = new_line[i].copy()
                        new_line[i] = ['.' for _ in range(size)]
                        new_line[j] = temp
                        new_line.insert(j + 1, ['.' for _ in range(diff)])
                    break

# make 
new_line = [item for sublist in new_line for item in sublist]

sum = 0
for i, c in enumerate(new_line):
    if c == '.': continue
    sum += i * int(c)
print(sum)
