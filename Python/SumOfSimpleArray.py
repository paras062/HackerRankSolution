def simpleArraySum(ar):
    temp=0
    for i in ar:
        temp = temp + i
    return temp


array = [1,2,3]
result = simpleArraySum(array)
print(result)