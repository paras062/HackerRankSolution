# Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking.
# The game uses Dense Ranking, so its leaderboard works like this:

# The player with the highest score is ranked number  on the leaderboard.
# Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
# For example, the four players on the leaderboard have high scores of 100, 90, 90, and 80. Those players will have ranks 1,2 ,2 , and 3 , respectively.
# If Alice's scores are 70,80  and 105, her rankings after each game are 4,3  and 1.

# URL - https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

import math


def ClimbingLeaderBoard(score, alice):
    n = len(score)
    m = len(alice)
    rank = [1]  # rank of first element is 1
    res = [None]*m
    index = 0

    for i in range(1, n):
        if(score[i] == score[i-1]):
            rank.append(rank[i-1])
        else:
            rank.append(rank[i-1]+1)
    # print(rank)

    for j in range(0, m):
        aliceScore = alice[j]
        if(aliceScore > score[0]):
            res[j] = 1
        elif (aliceScore < score[n-1]):
            res[j] = rank[n-1]+1
        else:
            index = BinarySearch(score, aliceScore)
            res[j] = rank[index]

    return res


# def BinarySearch(score, aliceScore, start, end):
#     start = start
#     end = end
#     totalItems = end - start
#     mid = math.floor(((totalItems)/2)+start)
#     if (score[mid] == aliceScore):
#         return mid
#     if (score[mid] < aliceScore and aliceScore < score[mid-1]):
#         return mid
#     if (score[mid] > aliceScore and aliceScore >= score[mid+1]):
#         return mid+1
#     if(score[mid] < aliceScore):
#         # move to left/start side of the list
#         return BinarySearch(score, aliceScore, start, (mid-1))
#     elif(score[mid] > aliceScore):
#         # move to right/end side of the list
#         return BinarySearch(score, aliceScore, (mid+1), end)

#     return mid

def BinarySearch(scores, aliceScore):
    start = 0
    end = len(scores) - 1
    while(start <= end):
        mid = math.floor(start + (end - start)/2)
        if(scores[mid] == aliceScore):
            return mid
        elif(scores[mid] < aliceScore and aliceScore < scores[mid-1]):
            return mid
        elif(scores[mid] > aliceScore and aliceScore >= scores[mid+1]):
            return mid + 1
        elif (scores[mid] < aliceScore):
            end = mid-1
        elif(scores[mid] > aliceScore):
            start = mid+1

    return -1


# score = [100, 100, 50, 40, 40, 20, 10]
# alice = [5, 25, 50, 120]
# output - 6,4,2,1


scores = [100, 90, 90, 80, 75, 60]
alice = [50, 65, 77, 90, 102]
#output = 6,5,4,2,1

result = ClimbingLeaderBoard(scores, alice)
print(result)
