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
health = 100
courage = 100
magic = 100
gameOver = False
inventory = {"Potions": {"Health": 2, "Mana": 1, "Liquid Courage": 1},
             "Weapons": {"Axe": False, "Sword": False, "Longbow": False},
             "Armour": {"Helmet": False, "Breastplate": "Leather", "Boots": "Leather"}
             }
print(inventory)
# print(inventory.items())
# print(inventory["Weapons"])
# print(inventory["Armour"])
while not gameOver:
    print("You come across a Goblin!")
    if courage >= 75:
        print("You're feeling pretty good about yourself!")
        fightInput = input("Do you want to fight?\n")
    elif courage >= 50:
        print("You're not sure if you can beat the goblin.")
        fightInput = input("Do you want to fight?\n")
    else:
        print("You don't have enough faith in yourself to fight, consider drinking some liquid courage first!")

    if fightInput in ["y", "yes", "sure", "yes please", "yeah", "ye", "okay", "ok", "fight"]:
        if inventory["Weapons"]["Axe"] == False and inventory["Weapons"]["Sword"] == False and inventory["Weapons"]["Longbow"] == False:
            print("You are unarmed! You manage to escape the goblin but you are hurt in the process.")
            health -= 25
            courage -=50
            print("You lost 25 health! You have "+ str(health)+ " remaining!")
            print("You lose faith in your own ability as an adventurer!")
        else:





    chestInput = input("Do you want to open the chest?\n")
    if chestInput in ["y", "yes", "sure", "yes please", "yeah", "ye", "okay", "ok", "open"]:

        if inventory["Potions"]["Health"] < 5:
            print("You've found a Health potion!")
            inventory["Potions"]["Health"] += 1
        else:
            print("You can't carry any more Health potions!")
        if inventory["Potions"]["Mana"] < 5:
            print("You've found a Mana potion!")
            inventory["Potions"]["Mana"] += 1
        else:
            print("You can't carry any more Mana potions!")

        if inventory["Weapons"]["Axe"] == False:
            print("You've found an axe!")
            inventory["Weapons"]["Axe"] = True
        else:
            if inventory["Weapons"]["Sword"] == False:
                print("You've found a Sword!")
                inventory["Weapons"]["Sword"] = True
            else:
                if inventory["Weapons"]["Longbow"] == False:
                    print("You've found a Longbow!")
                    inventory["Weapons"]["Longbow"] = True
                else:
                    print("You find some bottles of liquid courage at the bottom of the chest!")
                    inventory["Potions"]["Liquid Courage"] += 1

    print(inventory)
    print(inventory.items())
    print(inventory["Weapons"])
    print(inventory["Potions"])





#old code
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