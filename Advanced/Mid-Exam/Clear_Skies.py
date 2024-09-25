size = int(input())
matrix = []
my_position = []

quantity_of_armor = 0
count = 0

for row in range(size):
    line = list(input())
    matrix.append(line)
    if 'J' in line:
        my_position = [row, matrix[row].index('J')]
        quantity_of_armor += 300
        matrix[my_position[0]][my_position[1]] = '-'


directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

while True:
    other_E = []
    command = input()
    r, c = my_position[0] + directions[command][0], my_position[1] + directions[command][1]
    element = matrix[r][c]
    my_position = [r, c]

    if element == '-':
        continue
    elif element == 'E':
        matrix[r][c] = '-'
        for row in matrix:
            if 'E' in row:
                current_count = 0
                current_count = row.count('E')
                if current_count >= 2:
                    other_E.append('E')
                    other_E.append('E')
                    current_count = 0
                else:
                    other_E.append('E')

        if other_E:
            quantity_of_armor -= 100
            count += 1
            if quantity_of_armor == 0:
                print(f'Mission failed, your jetfighter was shot down! Last coordinates [{r}, {c}]!')
                break
        if not other_E:
            print(f'Mission accomplished, you neutralized the aerial threat!')
            break
    elif element == 'R':
        matrix[r][c] = '-'
        quantity_of_armor = 300


matrix[r][c] = 'J'

for line in matrix:
    print(''.join(line))