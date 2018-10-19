'''
#while loop
count = 0
mohammad_computer_work = False

while count <8:
    print(count)

    if count ==6:
        print ("syke Mohammad")
        break
    else:
        count += 1
        continue
for i in range(20,41,2):
    print(i)

count2 = 0

#ifloop
while mohammad_computer_work == False:
    print ("haha")

    if count2 == 10:
        print (":(")
        break
    else:
        count2+=1
        continue
'''

'''
#ifloop and continue

word = "python"
for i in (word):
    if i == "t":
        continue
    #if i != "t":
    print(i, end="")
'''
#list
'''
elementList = ["earth", "wind", "water", "fire"]
print(elementList)
print(elementList[0:2])
print(elementList[-2])

elementList.append("lumos")
print(elementList)
elementList[0]=("death")
print(elementList)
elementList.append("earth")
print(elementList)
elementList.remove("earth")
elementList.remove("death")
elementList.insert(0, "earth")
print(elementList)
print(elementList.index("fire"))

for i in elementList:
    print(i)
'''
#excercise 1 & 2
words = ["xxx", "aaa", "r5t6yy", "g", "wow"]
count = 0
for i in words:
    if len(i)>1:
        count+=1

print(count)

numbers=[2,3,5,7,66,89,134]
userNumber= int(input("Give me a number: "))
for n in numbers:
    if userNumber>=n:
        continue
    print(n)