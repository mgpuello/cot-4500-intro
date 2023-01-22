import numpy as np
x = np.random.randint(9)
y = np.random.randint(9)
z = np.random.randint(9)

matrix = np.array([[x, y, z], [x, y, z], [x, y, z]])
#Part 1
for i in range(0, 3):
    for j in range(0, 3):
        if i == j:
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0

print(matrix)
for i in range(0, 3):
    for j in range(0, 3):
        if i == j:
            matrix[i][j] = 1
        else:
            matrix[i][j] += 3

print(matrix)

matrix = np.delete(matrix, 2, 1)

print(matrix)


