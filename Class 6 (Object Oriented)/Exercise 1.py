# Create a class to represent Enemies in a video game. Each instance of an Enemy
# should have its own name, clan, and special ability. All Enemies share the same
# weapon list. Add damage points to each weapon.
# Create 2 instances of the Enemy class and print out their different fields.
# Add a method to set the description of the enemy and one method to get it
# Print out each instance’s attributes and description. You may want to use the
# string format method:
# print
# (“
# {}
#  blah blah
# {}
# ..”.format(variable0,variable1..))
# Add a method to add weapon to each instance and give a weapon in each of the
# two instances


class Enemy:
    weaponList = {"Pistol": 2, "Knife": 4, "AK-47": 10}

    def __init__(self, name, clan, special_ability):
        self.name = name
        self.clan = clan
        self.special_ability = special_ability

    def descript(self, desc):
        self.desc = desc

    def status(self):
        print(self.desc)

    # def weapon_add(self, x,y):
        # self.weaponList.append(x:y)

enemy1 = Enemy("Bob", "Shadow", "Dashing strike")
enemy1.descript("Bob is healthy")
enemy1.status()
# print("\nName =", enemy1.name,"\nClan =", enemy1.clan,"\nSpecial ability =", enemy1.special_ability)
#     # def
print("%s is a %s clan member and has the special ability %s" % (enemy1.name, enemy1.clan, enemy1.special_ability))
