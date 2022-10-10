from collections import Counter

def getUnique(lis):
    return[k for k, v in Counter(lis).items() if v == 1]

print("Enter Values Separated By Spaces: ",end)
testList = map(int, input().split)
uniqueList = getUnique(testList)
print("Unique Elements:",uniqueList)
