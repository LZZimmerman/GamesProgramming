#exercise 1
#hey = "Hey, it's Jo!"
#there = "there"

# 1. hey[:4] = Hey,
# 2. hey[-1] = !
# 3. hey*2 = Hey, it's Jo!Hey, it's Jo!
# 4. hey[:-1] + there + hey[-1] = Hey, it's Jothere!
# 5. hey[:-1] + " " + there + hey[-1] = Hey, it's Jo there!
# 6. there[1] = h
# 7. hey[4] = " "
# 8.  hey *2 + there [:-1] + there + hey [-1] = Hey, it's Jo!Hey, it's Jo!therthere!
# 9. hey[-2:1] = " "
#print(hey[-2:1])

#exercise 2 (complete version)
dateInput = input("Please enter a date in the following format (dd/mm/yyyy), for example (1/5/2013): ")
date = dateInput.split("/")

inputCheck = True
while inputCheck == True:   #check if the input are numbers or not
    if date[0].isdigit() != True or date[1].isdigit() != True or date[2].isdigit() != True:
        print("Invalid format.")
        dateInput = input("Please enter a date in the following format (dd/mm/yyyy), for example (1/5/2013): ")
        date = dateInput.split("/")
    else:
        inputCheck = False

day = int(date[0])
month = int(date[1])
year = int(date[2])
dayCheck = True
monthCheck = True
while dayCheck == True:
    if day > 31 or day < 1: #checking for invalid day entry
        print("Incorrect entry for days")
        dateInput = input("Please enter a date in the following format (dd/mm/yyyy), for example (1/5/2013): ")
        date = dateInput.split("/")
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
    else:
        dayCheck = False
while monthCheck == True:
    if month > 12 or month < 1: #checking for invalid month entry
        print("Incorrect entry for months")
        dateInput = input("Please enter a date in the following format (dd/mm/yyyy), for example (1/5/2013): ")
        date = dateInput.split("/")
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
    else:
        monthCheck = False

if month == 1:
    print("The date is January " + str(day) + ", " + str(year))
elif month == 2:
    print("The date is February " + str(day) + ", " + str(year))
elif month == 3:
    print("The date is March " + str(day) + ", " + str(year))
elif month == 4:
    print("The date is April " + str(day) + ", " + str(year))
elif month == 5:
    print("The date is May " + str(day) + ", " + str(year))
elif month == 6:
    print("The date is June " + str(day) + ", " + str(year))
elif month == 7:
    print("The date is July " + str(day) + ", " + str(year))
elif month == 8:
    print("The date is August " + str(day) + ", " + str(year))
elif month == 9:
    print("The date is September " + str(day) + ", " + str(year))
elif month == 10:
    print("The date is October " + str(day) + ", " + str(year))
elif month == 11:
    print("The date is November " + str(day) + ", " + str(year))
elif month == 12:
    print("The date is December " + str(day) + ", " + str(year))







#print(date)
# day, month, year = (int(date) for date in dateInput.split("/"))
#print(day)
#print(month)
#print(year)



#exercise 2 failures below:





# day = int(dateInput[:2])
# month = int(dateInput[3:5])
# year = dateInput[6:10]
# while loopOn == True:
#     if type(day) == int:
#         if int(day) > 31 or int(day) < 1:
#             print("Incorrect entry for days")
#             dateInput = input("Please enter a date in the following format (dd/mm/yyyy): ")
#             day = int(dateInput[:2])
#             month = int(dateInput[3:5])
#             year = int(dateInput[6:10])
#     else:
#         print("Incorrect format")
#         dateInput = input("Please enter a date in the following format (dd/mm/yyyy): ")
#         day = int(dateInput[:2])
#         month = int(dateInput[3:5])
#         year = int(dateInput[6:10])
#
#     if type(month) == int:
#         if int(month) > 12 or int(month) < 1:
#             print("Incorrect entry for months")
#             dateInput = input("Please enter a date in the following format (dd/mm/yyyy): ")
#             day = int(dateInput[:2])
#             month = int(dateInput[3:5])
#             year = int(dateInput[6:10])
#     else:
#         print("Incorrect format")
#         dateInput = input("Please enter a date in the following format (dd/mm/yyyy): ")
#         day = int(dateInput[:2])
#         month = int(dateInput[3:5])
#         year = int(dateInput[6:10])
#
#     # if type(year) != int:
#     #     print("Incorrect format")
#     #     dateInput = input("Please enter a date in the following format (dd/mm/yyyy): ")
#     #     day = int(dateInput[:2])
#     #     month = int(dateInput[3:5])
#     #     year = int(dateInput[6:10])
#
#
# # if int(day) > 31 or int(day) < 1:
# #     print("Incorrect entry for days")
# #     dateInput = input("Please enter a date in the following format (dd/mm/yyyy): ")
# #     day = int(dateInput[:2])
# #     month = int(dateInput[3:5])
# #     year = int(dateInput[6:10])
# # elif int(day) < 0:
# #     print("Incorrect entry for days")
# #     dateInput = input("Please enter a date in the following format (dd/mm/yyyy): ")
# #     day = int(dateInput[:2])
# #     month = int(dateInput[3:5])
# #     year = int(dateInput[6:10])
# #
# # if int(month) > 12:
# #     print("Incorrect entry for months")
# #     dateInput = input("Please enter a date in the following format (dd/mm/yyyy): ")
# #     day = int(dateInput[:2])
# #     month = int(dateInput[3:5])
# #     year = int(dateInput[6:10])
# # elif int(month) < 1:
# #     print("Incorrect entry for months")
# #     dateInput = input("Please enter a date in the following format (dd/mm/yyyy): ")
# #     day = int(dateInput[:2])
# #     month = int(dateInput[3:5])
# #     year = int(dateInput[6:10])
#
#
#
#
# print(day)
# print(month)
# print(year)
