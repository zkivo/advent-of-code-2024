import sys
rows = []
sum = 0
j = 0
while True:
    row = sys.stdin.readline().strip()
    if not row:
        break
    rows.append(row)
    if len(rows) == 5:
        rows.pop(0)
    for i in range(len(rows[-1])):
        try:
            if rows[-1][i] == 'X' and rows[-1][i+1] == 'M' and rows[-1][i+2] == 'A' and rows[-1][i+3] == 'S': 
                sum += 1 # go right
        except: pass
        try:
            if rows[-1][i] == 'X' and rows[-1][i-1 if i-1 >= 0 else None] == 'M' and \
                    rows[-1][i-2 if i-2 >= 0 else None] == 'A' and rows[-1][i-3 if i-3 >= 0 else None] == 'S': 
                sum += 1 # go left
        except: pass
        try:
            if rows[3][i] == 'X' and rows[2][i] == 'M' and rows[1][i] == 'A' and rows[0][i] == 'S': 
                sum += 1 # go up
        except: pass
        try:
            if rows[0][i] == 'X' and rows[1][i] == 'M' and rows[2][i] == 'A' and rows[3][i] == 'S': 
                sum += 1 # go down
        except: pass
        try:
            if rows[0][i] == 'X' and rows[1][i+1] == 'M' and rows[2][i+2] == 'A' and rows[3][i+3] == 'S': 
                sum += 1 # go down-right
        except: pass
        try:
            if rows[0][i] == 'X' and rows[1][i-1 if i-1 >= 0 else None] == 'M' and \
                    rows[2][i-2 if i-2 >= 0 else None] == 'A' and rows[3][i-3 if i-3 >= 0 else None] == 'S': 
                sum += 1 # go down-left
        except: pass
        try:
            if rows[3][i] == 'X' and rows[2][i+1] == 'M' and rows[1][i+2] == 'A' and rows[0][i+3] == 'S': 
                sum += 1 # go up-right
        except: pass
        try:
            if rows[3][i] == 'X' and rows[2][i-1 if i-1 >= 0 else None] == 'M' and \
                    rows[1][i-2 if i-2 >= 0 else None] == 'A' and rows[0][i-3 if i-3 >= 0 else None] == 'S': 
                sum += 1 # go up-left
        except: pass
    j += 1
print(sum)