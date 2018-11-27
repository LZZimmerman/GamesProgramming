inputCheck = True

while inputCheck == True:
    tempInput = input("Please enter a temperature as a number: ")
    tempInput2 = input("Please enter <C> if the above number is in Celcius or <F> if it is in Fahrenheit: ").lower()
    celsius = 0
    fahrenheit = 0
    try:
        if tempInput2 in ["c"]:
            celsius = int(tempInput)
            fahrenheit = celsius*(9/5)+32
            print(str(celsius) + " Celsius is " + str(fahrenheit) + " Fahrenheit")
            inputCheck = False

        elif tempInput2 in ["f"]:
            fahrenheit = int(tempInput)
            celsius = (fahrenheit-32)*(5/9)
            print(str(fahrenheit) + " Fahrenheit is " + str(celsius) + " Celsius")
            inputCheck = False
        else:
            print("Invalid input for temperature type, please try again")
    except ValueError:
        print("Incorrect input for temperature value, please try again")

