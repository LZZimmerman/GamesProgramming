# # # # import hello
# # # #
# # # # hello.addition(5,6)
# # #
# # # from hello import addition
# # #
# # # addition(5,6)
# # from hello import *
# # addition(5,6)
# # print(a)
#
# import hello as h
#
# h.addition(5,6)

import random
enemyInsults = ["You are not very smart", "You have trouble tying your shoes", "If I was your Father, I would be dissapointed in you", "You fat"]
playerInsults = ["No u", "Sticks and stones may break my bones but words will never hurt me", "Yeah? but at least my shirt's not pink", "What the heck? not cool"]
playerInsultsLength = []

print("You come across a pirate, he walks up to you and says:")
print(random.choice(enemyInsults))

print("How would you like to respond? ")

for i in range(len(playerInsults)):

    print(str(i+1) + ") " + playerInsults[i])
    playerInsultsLength.append(str(i+1))
print(playerInsultsLength)
# print(*playerInsults, sep = "\n")
while True:
    userInput = input("Pick your response: ")
    if userInput not in playerInsultsLength:
        print ("Please enter a valid insult number.")
    elif userInput == "1":
        print("The pirate is aghast, how could you come up with the perfect retort?")
    elif userInput == "2":
        print("Your childish retort fails to have an effect on the pirate, he laughs in response and walks away")
    elif userInput == "3":
        print("The pirate gives you a glare, but is unable to retort.")
    elif userInput == "4":
        print("Everyone around looks at you and start laughing, your future as a pirate is over")
