''' ==========================================
== Written by..: Manuel Puello            ====
== Date Written: Jan 19                   ====
== Purpose.....: INTRO PYTHON / GITHUB    ====
==============================================
'''

def main():

    import numpy as np
    x = np.random.randint(9)
    y = np.random.randint(9)
    z = np.random.randint(9)

    matrix = np.array([[x, y, z], [x, y, z], [x, y, z]])

    #Part 1 Print a specific 3x3 matrix where a cell is 1 if i == j, else 0
    for i in range(0, 3):
        for j in range(0, 3):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

    print(matrix)
    print("\n")

    #Part 2 Print the 3x3 matrix from #1 and then add 3 to every cell where i ≠j
    for i in range(0, 3):
        for j in range(0, 3):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] += 3

    print(matrix)
    print("\n")

    #Part 3 Print the 3x3 matrix from #2 as a 3x2 by deleting the last column from the matrix created
    matrix = np.delete(matrix, 2, 1)
    print(matrix)
    print("\n")


main()
