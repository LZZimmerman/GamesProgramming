nameInput = input("Please type your name: ")
ageInput = input("Please type your age: ")
heightInput = input("Please type your height: ")
weightInput = input("Please type your weight: ")

my_dict = {'Name':str(nameInput), 'Age':str(ageInput), 'Height':str(heightInput), 'Weight':str(weightInput)}
print("your name is " + my_dict['Name'])

my_dict.pop('Weight')
print(my_dict.items())
for k,val in my_dict.items():
    print(k,":",val)

print(my_dict['Height'])