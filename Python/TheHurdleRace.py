def hurdleRace(k, height):
    maxHeight = 0
    doses = 0
    # n = len(height)
    # for i in range(0, n):
    #     if height[i] > maxHeight:
    #         maxHeight = height[i]

    for items in height:
        if items > maxHeight:
            maxHeight = items

    if maxHeight > k:
        doses = maxHeight-k

    print(doses)


# height = [2, 5, 4, 5, 2]
# k = 7
height = [1, 2, 3, 3, 2]
k = 1
hurdleRace(k, height)
