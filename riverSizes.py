#-------------------------------------------------------------
def riverSizes(matrix):
    marked = set()
    rivers = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1 and (row, col) not in marked:
                current_river_length = 1
                marked.add((row, col))
                stack = [(row, col)]

                while stack:
                    current = stack.pop()
                    neighbors = get_neighbors(current, matrix)
                    for n in neighbors:
                        y, x = n
                        if matrix[y][x] == 1 and (y, x) not in marked:
                            marked.add((y, x))
                            current_river_length += 1
                            stack.append((y, x))
                rivers.append(current_river_length)
    return rivers
#-------------------------------------------------------------
def get_neighbors(position, matrix):
    y, x = position
    list_of_neighbors = []
    if x >= 1: #left neighbor
        list_of_neighbors.append((y, x-1))
    if x < len(matrix[0]) - 1: #right neighbor
        list_of_neighbors.append((y, x+1))
    if y >= 1: #top neighbor
        list_of_neighbors.append((y-1, x))
    if y < len(matrix) - 1: #bottom neighbor
        list_of_neighbors.append((y+1, x))
    return list_of_neighbors
#-------------------------------------------------------------
test_board = [
            [1, 1, 0, 1, 0, 0, 1, 1, 0],
            [1, 0, 0, 0, 1, 1, 0, 0, 1],
            [0, 0, 0, 1, 0, 1, 0, 1, 1],
            [0, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 0, 1]
]
print(riverSizes(test_board))
#-------------------------------------------------------------
test_board1 = [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0]
]
print(riverSizes(test_board1))
#-------------------------------------------------------------
test_board2 = [
            [1, 0, 0, 0, 1],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1]
]
print(riverSizes(test_board2))
