# ----------------------------------------------------------------------------------------------------------------------
# Class 5 -  Peer Programming
# ----------------------------------------------------------------------------------------------------------------------

# Player stats ---------------------------------------------------------------------------------------------------------

import random

FlyAbility = 0
StealthAbility = 0

invPlayer = {"Daggers": 0, "BluePotions": 0, "GoldenFeathers": 0, "Manuscripts": 0}

items = ["Daggers", "BluePotions", "GoldenFeathers", "Manuscripts", "Twig", "Bag of holding", "Sack of gold", "Elixir of eternal life"]
allowedItems = ["Daggers", "BluePotions" ,"GoldenFeathers", "Manuscripts"]

while True:
    while True:
        userInput = input ("\nWhich direction to travel (n,s,e,w)?").lower()
        if userInput not in ["n","s","e","w"]:
            print("You can't go that way.")
            continue
        else:
            break
    randomItem = items[(random.randint (0,len(items)-1))]
    if randomItem not in ["Twig", "Bag of holding", "Sack of gold"]:
        print("\nYou find " + str(randomItem))
    elif randomItem  in ["Elixir"]:
        print("\nYou find an " + str(randomItem))
    else:
        print("\nYou find a " + str(randomItem))


    if randomItem not in allowedItems:
        print("You don't think it's valuable and toss it aside.")

# Permitted items ------------------------------------------------------------------------------------------------------
    else:
        userInput = input("Do you wish to pick it up? ").lower()
        if userInput in ["y", "yes", "yeah"]:
            print("\nYou stash it in your inventory.")
            for key, value in invPlayer.items():
                if key == randomItem:
                    invPlayer[key] += 1

# Print player inventory -----------------------------------------------------------------------------------------------
                    print("\n===== Player inventory: =====")
                    for k, v in invPlayer.items():  # to access the values of the nested dictionary (details is your second dictionary so you can do details.items())
                        print(k + "\t", v)

            if randomItem in ["BluePotions"]:
                if StealthAbility < 5:
                    StealthAbility += 1
                    print("\nYour stealth ability has increased by +1.")
                    print("Stealth ability: " + str(StealthAbility))
                else:
                    print("\nYour stealth ability is already maxed.")
                    print("Stealth ability: " + str(StealthAbility))

            if randomItem in ["GoldenFeathers"]:
                if FlyAbility < 5:
                    FlyAbility += 1
                    print("\nYour fly ability has increased by +1.")
                    print("Fly ability: " + str(FlyAbility))
                else:
                    print("\nYour fly ability is already maxed.")
                    print("Fly ability: " + str(FlyAbility))
        else:
print("\nYou toss it aside.")