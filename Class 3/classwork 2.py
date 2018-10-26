# a = [x**2 for x in range(5)]
# print(*a)
# b=[]
# for i in range(5):
#     b.append(i**2)
# print(b)
# #
tupleList = [ (), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d') ]
newList = []
for a in tupleList:
    if len(a) > 0:
        newList.append(a)
print(newList)

