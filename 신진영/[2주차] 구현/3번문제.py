n = input()
row = int(n[1])
col = int(ord(n[0])) - int(ord('a')) + 1

moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for m in moves:
    next_row = row + m[0]
    next_col = col + m[1]
    
    if next_row >= 1 and next_row <= 8 and next_col >=1 and next_row <= 8:
        result += 1
    
print(result)