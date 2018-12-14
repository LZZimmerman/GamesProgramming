gameOver = False
callIgnoreCount = 0

#while gameOver == False:        ##game loop
while True:     ##phone call loop
    usrInput = input("Your phone starts ringing, do you wish to answer? [Y/N]").lower()
    if usrInput in ["y"]:
        ##insert phone message below
        print("\"Our newest attraction has suspiciously gone missing, we will require some expert assistance on this matter.\"")
        break
    elif usrInput in ["n"] and callIgnoreCount <3:
        print("Einz looks disapprovingly at you\nYou shrug and turn back to the kitchen")
        callIgnoreCount += 1
    elif usrInput in ["n"] and callIgnoreCount < 5:
        print("Einz growls at you\nYou are unnerved, but turn back to kitchen nonetheless ")
        callIgnoreCount += 1
    elif usrInput in ["n"] and callIgnoreCount == 5:
        print("Einz jumps on the table and answers your phone with his nose. He nudges it with his nose and a message comes out through the speakers:")
        ## insert phone message below
        print("\"Thank you for finally answering; our newest attraction has suspiciously gone missing, we will require some expert assistance on this matter.\"")
        break
    else:
        print("Incorrect response, please try again")

#end

while True:         ##answer phone loop
    usrInput = input("\"Can we rely on you for help, Dr DoMuch?\" [Y/N]").lower()
    if usrInput in ["y"]:
        ##insert phone message below
        print("\"Very well, we'll see you at the zoo Dr DoMuch\"")
        print("You grab your briefcase and shoes, open the door and head to the zoo\nEinz chooses to come with you")
        break
    elif usrInput in ["n"]:
        print("You hang up and turn back to the kitchen\nSuddenly there's a knock on the door")
        print("As you open the door, a man in a suit and black glasses is standing there with a briefcase\n")
        print("\"Please come to the zoo Dr DoMuch, it's an urgent matter\"")
        print("Afraid of what the man might do if you refuse, you grab your own briefcase and shoes and head to the zoo\nEinz chooses to come with you")
        break
    else:
        print("Incorrect response, please try again")