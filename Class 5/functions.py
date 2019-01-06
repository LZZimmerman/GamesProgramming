# def print_hello():
#
#     print("hello")
#
# print("This is not inside the function")
#
# print_hello()
#
#--------------------------------------------------
#
# def print_hello(a):
#     print(a + " this is an addition to the code")
#
# print_hello("gotcha")
#
#--------------------------------------------------
#
# def addition(a,b = 3):
#
#     print(a+b)
#
# addition(5)
#
#
#--------------------------------------------------
# listA = [2,4,5,6,7,8]
# LotteryList = [1,23,3,4]
#
# def multiply(a):
#     listB = []
#     for i in a:
#         listB.append(i*2)
#     return(listB)
#
# multiply(listA)
# multiply(LotteryList)
#
# newListA = multiply(listA)
# print(newListA)

a=4


def valueInsideFunction():

    global a
    a = 17
    print("Value of an inside function:", a)


valueInsideFunction()
print("Value of a outside function", a)