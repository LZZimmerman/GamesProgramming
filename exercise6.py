print ("You open your eyes and find yourself in the middle of a square. To the west you see a graveyard. A path to the east leads to a bridge. In front of you, to the north, you see a large tower looming.")
print ("A) Go to the graveyard")
print ("B) Go to the bridge")
print ("C) Go to the tower")
stepuno = input("Choose A, B or C: ")
if stepuno[0] == "A":
    print ("You enter the graveyard; there are rows of graves within. All are nameless. A church building lies on the far end of the graveyard. A path leads off to a forest.")
elif stepuno[0] == "B":
    print ("You follow the path to a bridge. A dark river rushes below you. On the far end, you see a small cottage. A path diverts towards the forest.")
elif stepuno[0] == "C":
    print ("You head towards a tower. It looms over 30 meters tall and has a small wooden door at the bottom. To your left, a path leads towards a forest.")
else:
    print ("incorrect choice, please choose either A, B or C")
    stepuno = input("Choose A, B or C: ")
    if stepuno[0] == "A":
        print ("You enter the graveyard; there are rows of graves within. All are nameless. A church building lies on the far end of the graveyard. A path leads off to a forest.")
    elif stepuno[0] == "B":
        print ("You follow the path to a bridge. A dark river rushes below you. On the far end, you see a small cottage. A path diverts towards the forest.")
    elif stepuno[0] == "C":
        print ("You head towards a tower. It looms over 30 meters tall and has a small wooden door at the bottom. To your left, a path leads towards a forest.")
    else:
        print ("incorrect choice, please choose either A, B or C")
print ("Suddenly, bells begin to chime from the square that you had left.")
print ("A) Enter the nearby building")
print ("B) Go to the forest")
print ("C) Return to the square")
stepdos = input("Choose A, B or C: ")
if stepdos[0] == "A":
    print ("As you enter the building and close the door behind you, you hear heavy footsteps outside. You hear something scratch at the door with large claws.")
elif stepdos[0] == "B":
    print ("As you enter the forest, you see that the trees are dead and the forest is devoid of life. Suddenly, you hear encroaching hoof-like footsteps approach. You hear the sound of claws scratching the trees.")
elif stepdos[0] == "C":
    print ("You return to the town square. The bells are ringing above you. Suddenly, the floor begins to open up. As you retreat into an alleyway, you hear the sound of hooves on cobblestone. The steps begin to head in your direction.")
else:
    print ("incorrect choice, please choose either A, B or C")
    stepdos = input("Choose A, B or C: ")
    if stepdos[0] == "A":
        print ("As you enter the building and close the door behind you, you hear heavy footsteps outside. You hear something scratch at the door with large claws.")
    elif stepdos[0] == "B":
        print ("As you enter the forest, you see that the trees are dead and the forest is devoid of life. Suddenly, you hear encroaching hoof-like footsteps approach. You hear the sound of claws scratching the trees.")
    elif stepdos[0] == "C":
        print ("You return to the town square. The bells are ringing above you. Suddenly, the floor begins to open up. As you retreat into an alleyway, you hear the sound of hooves on cobblestone. The steps begin to head in your direction.")
    else:
        print ("incorrect choice, please choose either A, B or C")
print("A) Try and fight")
print("B) Attempt to escape")
steptres = input("Choose A or B: ")
if steptres[0] == "A":
    print ("You wait for the creature to appear. It’s over 3 meters long from head to hoof and appears to be wearing a mask with eyes painted upon it. It has 2 arms, one leading down to a large claw, with talons over 1 meter in width. You are unarmed. The creature flexes it’s claw and sprints towards you, impaling you upon its talons.")
    print ("The End")
elif steptres[0] == "B":
    print ("You turn to run, but as the creature comes into view, your legs feel extremely heavy and you stumble. The creature is over 3 meters tall and has hooves for feet. It is two armed, one with a large claw with talons over a meter in length. You are unarmed and attempt to crawl away. It reaches over and grabs your leg. It twists its claw and you lose all feeling your leg.")
    print ("The End")
else:
    print ("incorrect choice, please choose either A or B")
    steptres = input("Choose A or B: ")
    if steptres[0] == "A":
        print ("You wait for the creature to appear. It’s over 3 meters long from head to hoof and appears to be wearing a mask with eyes painted upon it. It has 2 arms, one leading down to a large claw, with talons over 1 meter in width. You are unarmed. The creature flexes it’s claw and sprints towards you, impaling you upon its talons.")
        print ("The End")
    elif steptres[0] == "B":
        print ("You turn to run, but as the creature comes into view, your legs feel extremely heavy and you stumble. The creature is over 3 meters tall and has hooves for feet. It is two armed, one with a large claw with talons over a meter in length. You are unarmed and attempt to crawl away. It reaches over and grabs your leg. It twists its claw and you lose all feeling your leg.")
        print ("The End")
