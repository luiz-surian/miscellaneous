# Challenge from: https://skillupper.com/spiral_matrix/outer_layer

matrix = [
    ["A","B","C","D","E"],
    ["F","G","H","I","J"],
    ["K","L","M","N","O"],
    ["P","Q","R","S","T"],
    ["U","V","W","X","Y"]
]
expected = [
    "A","B","C","D","E",
    "J","O","T",
    "Y","X","W","V","U",
    "P","K","F",
    "G","H","I",
    "N",
    "S","R","Q",
    "L",
    "M"
]


def step1_traverse_matrix(matrix):
    result = []
    size = len(matrix)
    x = 0
    y = 0
    result.append(matrix[y][x])
    for _ in range(size-1):
        x += 1
        result.append(matrix[y][x])
    for _ in range(size-1):
        y += 1
        result.append(matrix[y][x])
    for _ in range(size-1):
        x -= 1
        result.append(matrix[y][x])
    for _ in range(size-2):
        y -= 1
        result.append(matrix[y][x])
    return result


def step2_traverse_matrix(matrix):
    result = []
    size = len(matrix)
    x = 0
    y = 0
    result.append(matrix[y][x])
    for _ in range(size-1):
        x += 1
        result.append(matrix[y][x])
    for _ in range(size-1):
        y += 1
        result.append(matrix[y][x])
    for _ in range(size-1):
        x -= 1
        result.append(matrix[y][x])
    for _ in range(size-2):
        y -= 1
        result.append(matrix[y][x])
    for _ in range(size-2):
        x += 1
        result.append(matrix[y][x])
    for _ in range(size-3):
        y += 1
        result.append(matrix[y][x])
    for _ in range(size-3):
        x -= 1
        result.append(matrix[y][x])
    for _ in range(size-4):
        y -= 1
        result.append(matrix[y][x])

    return result


# Final Code
def traverse_matrix(matrix):
    result = []
    size = len(matrix)
    offset = 1
    x = 0
    y = 0
    result.append(matrix[y][x])
    for _ in range(size - offset):
        x += 1
        result.append(matrix[y][x])
    while offset < size:
        for _ in range(size - offset):
            if offset % 2 == 0:
                y -= 1
            else:
                y += 1
            result.append(matrix[y][x])
        for _ in range(size - offset):
            if offset % 2 == 0:
                x += 1
            else:
                x -= 1
            result.append(matrix[y][x])
        offset += 1
    return result


result = traverse_matrix(matrix)
if result == expected:
    print('success')
else:
    print('wrong', result)
