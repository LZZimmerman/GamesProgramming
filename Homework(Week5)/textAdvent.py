weapons = ["sword", "dagger"]
fightMode = False

while True:

	usr=input("Where to? ").lower()

	if usr in ["n", "north"]:
		print("Oh this looks like trouble!")

		 
		usr = input("Will you fight?").lower()
		if usr in ["yes", "y", "hell yeah"]:
			fightMode = True
		else:
			continue

		if fightMode:
			weaponCheck = True  # exercise 2
			while weaponCheck == True: #exercise2
				usr = input("which weapon you want to use: ")

				usrp = usr.split(" ") #list

				for word in usrp:
					if word in weapons:
						if word == "sword":
							print("With this you do 5 damage. On we go!")
							weaponCheck = False
						elif word == "dagger":
							print("With this you do 3 damage. On we go!")
							weaponCheck = False
					else:
						print("please choose a weapon you actually have")


		# Further code for the fight ...
	# exercise 1
	elif usr in ["s", "south", "w", "west", "e", "east"]:
		print("Nothing there")
	else:
		print("This is not a valid direction")
	 


		 