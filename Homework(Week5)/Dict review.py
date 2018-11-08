# # Exercise 1: Write a Python script to print a dictionary where the
# # keys are numbers between 1 and 20 (both included) and the
# # values are the square of their keys.
#
# excerciseOneDict = {}
# for i in range (1,21):
#     excerciseOneDict[i]=i**2
#
# print(excerciseOneDict.items())

# # Exercise 2: The following Dictionary includes some duplicate value
# # entries (item1 and item3). Write a program to remove them.
# room_items = {"item1":{"Name": "Lamp", "Colour": "Red"},
#               "item2":{"Name": "Table", "Colour": "Brown", "Type": 0},
#               "item3":{"Name": "Lamp", "Colour": "Red"},
#               "item4":{"Name": "Chair", "Colour": "Green", "Type": 1}
#               }
# newDict = {}
#
# for key,value in room_items.items():
#     if value not in newDict.values():
#         newDict[key] = value
# print(newDict)

# Exercise 3: Write a program that uses a dictionary to store a
# number of items in an inventory for an adventure game. The player
# should be able to pick new items for the inventory and use items
# from the inventory. Using an item may affect variables such as
# ‘health’, ‘magic’ or ‘courage’. You may want to use a dictionary to
# store these too. Be sure to check for the correct user input.

#complete
health = 100
courage = 100
magic = 100
gameOver = False
inventory = {"Potions": {"Health": 2, "Mana": 1, "Liquid Courage": 1},
             "Weapons": {"Axe": "no", "Sword": "no", "Longbow": "no"},
             "Armour": {"Helmet": "no", "Breastplate": "Leather", "Boots": "Leather"} #armour system not implemented, would add as goblin loot maybe
             }
#print(inventory)

while not gameOver:
    print("You come across a Goblin!")
    if courage >= 75:
        print("You're feeling pretty good about yourself!")
        fightInput = input("Do you want to fight?\n").lower()
    elif courage >= 50:
        print("You're not sure if you can beat the goblin.")
        fightInput = input("Do you want to fight?\n").lower()
    else:
        print("You don't have enough faith in yourself to fight, consider drinking some liquid courage first!")

    if fightInput in ["y", "yes", "sure", "yes please", "yeah", "ye", "okay", "ok", "fight"]:
        if inventory["Weapons"]["Axe"] == "no" and inventory["Weapons"]["Sword"] == "no" and inventory["Weapons"]["Longbow"] == "no":
            print("You are unarmed! You manage to escape the goblin but you are hurt in the process.")
            health -= 25
            courage -=50
            print("You lost 25 health! You have "+ str(health)+ " remaining!")
            print("You lose faith in your own ability as an adventurer!")
        else:
            print("You managed to kill the goblin!")
            courage += 10
            print("You gain some faith in your ability as an adventurer!")

    chestInput = input("Do you want to open the chest?\n").lower()
    if chestInput in ["y", "yes", "sure", "yes please", "yeah", "ye", "okay", "ok", "open"]:
        if inventory["Potions"]["Health"] >= 5 and inventory["Potions"]["Mana"] >= 5:
            print("Your inventory is full!")
            chestPotion = False
        else:
            chestPotion= True
            while chestPotion == True:
                print("You find some potions at the top of the chest.")
                print("You have " + str(inventory["Potions"]["Health"]) + " Health potion(s) and " + str(inventory["Potions"]["Mana"]) + " Mana potion(s).")
                potionInput = input("Do you want to pick up a health or mana potion?\n").lower()
                if potionInput in ["health", "heal", "healing", "healing potion", "health potion"]:
                    if inventory["Potions"]["Health"] < 5:
                        print("You've picked up a Health potion!")
                        inventory["Potions"]["Health"] += 1
                        chestPotion = False
                    else:
                         print("You can't carry any more Health potions!")
                elif potionInput in ["mana", "mana potion", "manapot", "manapotion"]:
                    if inventory["Potions"]["Mana"] < 5:
                        print("You've picked up a Mana potion!")
                        inventory["Potions"]["Mana"] += 1
                        chestPotion = False
                    else:
                        print("You can't carry any more Mana potions!")
                elif inventory["Potions"]["Health"] >= 5 and inventory["Potions"]["Mana"] >= 5:
                    print("Your inventory is full!")
                    chestPotion = False
                else:
                    print("Sorry, can't find that kind of potion.")
        chestWeapon= True
        while chestWeapon == True:
            if inventory["Weapons"]["Longbow"] == "a" and inventory["Weapons"]["Sword"] == "a" and inventory["Weapons"]["Axe"] == "an":
                print("You have collected all the weapons, but you find a bottle of liquid courage!")
                inventory["Potions"]["Liquid Courage"] += 1
                chestWeapon = False
            else:
                print("You find some weapons at the bottom of the chest.")
                print("You currently have " + str(inventory["Weapons"]["Axe"]) + " axe, " + str(inventory["Weapons"]["Sword"]) + " sword and " + str(inventory["Weapons"]["Longbow"]) +" longbow.")
                weaponInput = input("Do you want to pick up an axe, sword or longbow?\n").lower()
                if weaponInput in ["axe", "and my axe", "axe please"]:
                    if inventory["Weapons"]["Axe"] == "no":
                        print("You picked up an axe.")
                        inventory["Weapons"]["Axe"] = "an"
                        chestWeapon = False
                    else:
                        print("You already have an axe.")
                elif weaponInput in ["sword", "stabby", "stab thingy"]:
                    if inventory["Weapons"]["Sword"] == "no":
                        print("You picked up a sword.")
                        inventory["Weapons"]["Sword"] = "a"
                        chestWeapon = False
                    else:
                        print("You already have a sword.")
                elif weaponInput in ["longbow", "bow", "shooter", "arrow catapult"]:
                    if inventory["Weapons"]["Longbow"] == "no":
                        print("You picked up a longbow.")
                        inventory["Weapons"]["Longbow"] = "a"
                        chestWeapon = False
                    else:
                        print("You already have a longbow.")
                else:
                    print("Invalid weapon.")
    print("You have " + str(health) + " health, and " + str(magic) + " mana and " + str(courage) + " courage remaining")
    drinkInput = input("Do you want to drink something?\n").lower()
    if drinkInput in ["y", "yes", "sure", "yes please", "yeah", "ye", "okay", "ok", "drink"]:
        drinkIng = True
        while drinkIng == True:
            print("You have " + str(inventory["Potions"]["Health"]) + " Health potion(s) and " + str(inventory["Potions"]["Mana"]) + " Mana potion(s) and " + str(inventory["Potions"]["Liquid Courage"]) + " bottles of liquid courage.")
            drinkIngInput = input("Would you like to drink a health potion, a mana potion or a bottle of liquid courage?\n").lower()

            if drinkIngInput in ["health", "heal", "healing", "healing potion", "health potion"]:
                if inventory["Potions"]["Health"] <= 0:
                    print("You don't have any health potions left!")
                else:
                    print("You drink a health potion and regain 50 health!")
                    inventory["Potions"]["Health"] -= 1
                    health += 50
                    print("You now have "+ str(health)+ " health!")
                    drinkIng = False

            elif drinkIngInput in ["mana", "mana potion", "manapot", "manapotion"]:
                if inventory["Potions"]["Mana"] <= 0:
                    print("You don't have any mana potions left!")
                else:
                    print("You drink a mana potion and regain 50 mana!")
                    inventory["Potions"]["mana"] -= 1
                    magic += 50
                    print("You now have " + str(magic) + " mana!")
                    drinkIng = False

            elif drinkIngInput in ["liquid courage", "liquid", "courage", "alcohol", "bottle"]:
                if inventory["Potions"]["Liquid Courage"] <= 0:
                    print("You don't have any bottles of liquid courage left!")
                else:
                    print("You drink a bottle of liquid courage and regain 100 courage!")
                    inventory["Potions"]["Liquid Courage"] -= 1
                    courage += 100
                    print("You now have " + str(courage) + " courage!")
                    drinkIng = False
            elif drinkIngInput in ["no", "cancel", "escape", "don't drink", "stop"]:
                drinkIng = False
            else:
                print("invalid potion to drink")
    if courage > 250:
        print("You've gained enough courage to move on to greater adventures\n The end.")
        gameOver = True






#old code


                # if inventory["Potions"]["Health"] < 5:
        #     print("You've found a Health potion!")
        #     inventory["Potions"]["Health"] += 1
        # else:
        #     print("You can't carry any more Health potions!")
        # if inventory["Potions"]["Mana"] < 5:
        #     print("You've found a Mana potion!")
        #     inventory["Potions"]["Mana"] += 1
        # else:
        #     print("You can't carry any more Mana potions!")



        # if inventory["Weapons"]["Axe"] == "no":
        #     print("You've found an axe!")
        #     inventory["Weapons"]["Axe"] = True
        # else:
        #     if inventory["Weapons"]["Sword"] == "no":
        #         print("You've found a Sword!")
        #         inventory["Weapons"]["Sword"] = True
        #     else:
        #         if inventory["Weapons"]["Longbow"] == "no":
        #             print("You've found a Longbow!")
        #             inventory["Weapons"]["Longbow"] = True
        #         else:
        #             print("You find some bottles of liquid courage at the bottom of the chest!")
        #             inventory["Potions"]["Liquid Courage"] += 1

    #print(inventory)
    # print(inventory.items())
    # print(inventory["Weapons"])
    # print(inventory["Potions"])

# else:
#     if key == "Sword" and value == False:
#         print("You've found a Sword!")
#         inventory["Weapons"]["Sword"] = True
#     else:
#         if key == ""
# for k,v in inventory["Potions"].items():
#     if k =="Health" and v < 5:
#         print("You've found a Health potion!")
#         inventory["Potions"]["Health"] += 1
#     elif k =="Health" and v >= 5:
#         print("You can't carry any more Health potions!")
#     if k =="Mana" and v <5:
#         print("You've found a Mana potion!")
#         inventory["Potions"]["Mana"] += 1
#     elif k == "Mana" and v >= 5:
#         print("You can't carry any more Mana potions!")
# for key,value in inventory["Weapons"].items():

# if key == "Axe" and value == False: