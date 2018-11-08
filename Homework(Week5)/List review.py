# Exercise 1: For the following, given the first line write the line(s) of
# code that will give you the output in bold. For each one there may
# be more than one correct answer; just give one.

# #1
# a_list = [3, 5, 6, 12]
# print(a_list[0])
#
# #2
# print(a_list[1:])
#
# #3
# #a_list.reverse()
# #print(a_list)
#
# #4
# b_list = []
# for i in a_list:
#     b_list.append(i*3)
# print(b_list)
#
# #5
# c_list = []
# for n in a_list:
#     if n <6:
#         c_list.append(False)
#     else:
#         c_list.append(True)
# print(c_list)


#Exercise 2
# Write a Python program to print the numbers of a
# specified list after removing even numbers from it. Create the
# specified list by asking the user to give a few numbers in one go (
# check if user has used spaces and use string functions to remove
# them). Then construct the list and solve the problem.

# numberInput = input("Please give me multiple numbers, separated by a space (e.g. 1 3 6 7): ")
# spaceCheck = True
# while spaceCheck == True:
#     if " " in numberInput:
#         numberList = numberInput.split(" ")
#         spaceCheck = False
#     else:
#         print("Incorrect entry, please try again.")
#         numberInput = input("Please give me multiple numbers, separated by a space (e.g. 1 3 6 7): ")
#
#
# oddList = []
# for i in numberList:
#     if int(i)%2 == 1:
#         oddList.append(i)
# print(oddList)

#Exercise 3:
# Given the list myList = [“axe”, “dagger”, “oranges”]
# write a Python program to insert a “*” before each element of the
# list. There are many ways to solve this. Solve it using list
# comprehension to create the new list (output: [“*”, “axe”, “*”,
# “dagger”, “*”, “oranges”])

myList = ["axe", "dagger", "oranges"]
newList = []

for i in range(3):
    newList.append("*")
    newList.append(myList[i])
print(newList)
