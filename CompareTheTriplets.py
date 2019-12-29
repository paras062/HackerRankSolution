def compareTriplets(arrA, arrB):
    scoreA = 0  # Alice Score
    scoreB = 0  # Bob Score
    for i in range(len(arrA)):
        if arrA[i] > arrB[i]:
            scoreA = scoreA + 1
        elif arrA[i] < arrB[i]:
            scoreB = scoreB + 1
        elif arrA == arrB:
            temp = 0
    return scoreA, scoreB


arrayA = [1, 2, 3]
arrayB = [3, 2, 1]
result = compareTriplets(arrayA, arrayB)
print(result)
