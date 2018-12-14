gameOver = False
callIgnoreCount = 0

while gameOver == False:        ##game loop
    while True:     ##phone call loop
        usrInput = input("Your phone starts ringing, do you wish to answer? [Y/N]")
        if usrInput.lower() in ["y"]:
            ##insert phone message below
            print("<INSERT PHONE MESSAGE HERE")
            break
        elif usrInput.lower() in ["n"] and callIgnoreCount <3:
            print("Einz looks disapprovingly at you\nYou shrug and turn back to the kitchen")
            callIgnoreCount += 1
        elif usrInput.lower() in ["n"] and callIgnoreCount < 5:
            print("Einz growls at you\nYou are unnerved, but turn back to kitchen nonetheless ")
            callIgnoreCount += 1
        elif usrInput.lower() in ["n"] and callIgnoreCount == 5:
            print("Einz jumps on the table and answers your phone with his nose. He nudges it with his nose and a message comes out through the speakers:")
            ## insert phone message below
            print("<INSERT PHONE MESSAGE HERE>")
            break
        else:
            print("Incorrect response, please try again")
        