def diagonalDifference(arr):
    i = 0
    j = 0
    n = len(arr)
    diagonalR = 0
    diagonalL = 0

    # Right Diagonal
    for i in range(n):
        for j in range(n):
            if i == j:
                diagonalR = diagonalR + arr[i][j]

    # Left Diagonal
    for i in range(n):
        for j in range(n):
            if (i + j) == (n - 1):
                diagonalL = diagonalL + arr[i][j]

    difference = diagonalR - diagonalL
    return abs(difference)


array = [[-10, 3, 0, 5, -4],
         [2, -1, 0, 2, -8],
         [9, -2, -5, 6, 0],
         [9, -7, 4, 8, -2],
         [3, 7, 8, -5, 0]]

result = diagonalDifference(array)
print(result)
