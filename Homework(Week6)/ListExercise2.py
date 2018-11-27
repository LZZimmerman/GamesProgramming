#2.	Return the sum of the numbers in a given list, returning 0 for an empty list. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count. Use lists to test: [1, 2, 2, 1, 13], [1, 1], [ ]
##each commented listA is a different version of the exercise:

#listA = [1,2,2,1,13]

#listA = [1,1]

listA = []

newListA = []

for i in listA:
    if i == 13:
        break
    elif i != 13:
        newListA.append(i)
    else:
        newListA.append(0)

print(sum(newListA))
