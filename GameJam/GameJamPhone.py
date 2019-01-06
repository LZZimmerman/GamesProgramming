gameOver = False
callIgnoreCount = 0
wakeUpCheck = True
#mohammad input start
print("\n****************************************************************************************************************\n****************************\tDR DO-MUCH - THE LEGEND OF THE SINISTER SASQUATCH\t****************************\n****************************************************************************************************************")

print("\nYou are Dr. DoMuch, head of the Animal Alliance and famous detective.You awake in your bed with light streaming\nthrough your bedbroom curtains and the chirping of birds outside. You look at the clock next to your bed, it \nreads, '6:58 AM'.")
while True:
    userInput = input("\nWould you like to get up?").lower()
    if userInput not in ["yes", "y"] and userInput not in ["no", "n"]:
        print("You can't do that.")
    elif userInput in ["yes", "y"]:
        print("You get up and do your morning routine before heading down to the kitchen")
        wakeUpCheck = False
        break
    if userInput in ["no", "n"]:
        print("You lay back to relax a little longer but it isn't long before your alarm begins to ring loudly.")
        break

while wakeUpCheck == True:
    print("You are unable to sleep. What do you do?")
    userInput = input("1) Turn off the alarm\n2) Get up.\n")
    if userInput not in ["1", "2"]:
            print("You can't do that.")
    elif userInput in ["1"]:
        print("Reaching over you to switch off the alarm and lean lie back down again. Just as you eyes begin to close, your \nbedroom door slowly creaks open and you hear the pitter-patter of paws on the floor. A black and white \nborder collie jumps on to your bed and begins nudging you incessantly. Sighing you get up do you morning \nroutine before heading down to the kitchen")
        break
    elif userInput in ["2"]:
        print("You get up and do your morning routine before heading down to the kitchen")
        break


#"You receive information that the local zoo has lost one of it's newest additions.")

##mohammad  input end
##Lucas input
#while gameOver == False:        ##game loop
while True:     ##phone call loop
    usrInput = input("Your phone starts ringing, do you wish to answer? [Y/N]").lower()
    if usrInput in ["y"]:
        ##insert phone message below
        print("\"Hello Dr DoMuch, thank you for answering so quickly: It's John Wick from the local zoo. Our newest attraction has suspiciously gone missing, we will require some expert assistance on this matter.\"")
        break
    elif usrInput in ["n"] and callIgnoreCount == 0:
        print("Einz looks disapprovingly at you.\nYou shrug and turn back to the kitchen.")
        callIgnoreCount += 1
    elif usrInput in ["n"] and callIgnoreCount == 1:
        print("Einz lets out a whine.\nYou look over briefly but return to the kitchen to prepare your Frosty Flakes.")
        callIgnoreCount += 1
    elif usrInput in ["n"] and callIgnoreCount == 2:
        print("Einz growls at you.\nYou ignore him and finish your delicious Frosty Flakes.")
        callIgnoreCount += 1
    elif usrInput in ["n"] and callIgnoreCount == 3:
        print("Einz jumps on the table and answers your mobile phone with his nose, changing it to speakerphone.")
        ## insert phone message below
        print("\"Thank you for finally answering Dr. DoMuch; It's John Wick from the local zoo, what on earth took you so long? Nevermind, our newest attraction has suspiciously gone missing, we will require some expert assistance on this matter.\"")
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
        print("You hang up and turn back to the kitchen\nThere's frantic knocking at the door")
        print("As you open the door, a man in a suit and black glasses is standing there with a briefcase\n")
        print("\"Please come to the zoo Dr DoMuch, it's an urgent matter\"")
        print("Afraid of what the man might do if you refuse, you grab your own briefcase and shoes and head to the zoo\nEinz chooses to come with you")
        break
    else:
        print("Incorrect response, please try again")

print("\nSo begins the tale of Dr DoMuch and the Sinister Sasquatch")