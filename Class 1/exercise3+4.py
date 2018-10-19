number = int( input("Give me a number: "))
if number <=100:
    print("That's a small number.")
elif number <=1000:
    print("That's not a big number yet.")
else:
    print("That's an adequately huge number!")

if number%2 == 1:
    print ("This is an odd number.")
else:
    print ("This is an even number.")
