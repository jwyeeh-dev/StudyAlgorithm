
coordinate = input()
row = int(coordinate[1])
column = int(ord(coordinate[0])) - int(ord('a')) + 1

result = 0

move_types = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


for move in move_types:
    next_row = row + move[0]
    next_column = column + move[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)