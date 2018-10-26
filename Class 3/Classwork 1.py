g = 50
inventory = ["axe", "dagger", str(g) + " gold"]
gameOver = False

while not gameOver:

##exploring

    fightInput = input("Do you wish to murder the poor goblin orphan?\n").lower()

    if fightInput in ["y", "yes", "sure", "yes please", "yeah", "ye", "okay", "why not", "murder", "ok"]:
        print(inventory)
        userInput = input("Okay! What will you use to murder the orphan?\n").lower()
        if userInput == inventory[inventory.index(str(g) + " gold")]:
            print("You can't murder a goblin with gold, sorry.")
        elif userInput in inventory:
            print(" %s is a great choice" %userInput)
        else:
            print("You don't have this weapon")
    #    print(*inventory, sep= "\r")
    #if (userIn
    chestInput = input("Do you wish to open the chest?\n").lower()
    if chestInput in ["y", "yes", "okay", "sure", "open", "yeah", "yeahhhhhhhhhhhhh", "ok"]:
        if "longbow" not in inventory:
            print("You have found an antique longbow")
            inventory.append("longbow")
        # else:
        #     print("You have found 30 gold coins")
        #     g += 30
        #     #print(g)
        #     inventory[2] = str(g)+ " gold"
        else:
            print("You have found 30 gold coins")
            g += 30
            #print(g)
            inventory[inventory.index(str(g-30) + " gold")] = str(g)+ " gold"
            #str(g) + " gold" = 80 gold
            #str(g-30) = 50 gold