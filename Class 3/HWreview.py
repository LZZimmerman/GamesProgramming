# Activity 2: Given the following list of strings, return a list
# with the strings in sorted order, but group all the strings
# that begin with 'x' first. --- Hint: use two new lists
# x = ['mix', 'xyz', 'apple', 'xanadu', ‘rovio’] should return
# ['xanadu', 'xyz', 'apple', 'mix', ‘rovio’]

x = ['mix', 'xyz', 'apple', 'xanadu', 'rovio']
newlist_a=[]  #contains words beginning with x
newlist_b=[]  #contains the rest
for word in x:
    if word[0]== "x":
        newlist_a.append(word)
    else:
        newlist_b.append(word)

print( sorted(newlist_a) + sorted(newlist_b))

numbers= [2, 3, 5, 7, 66, 89, 134]
userinput= int( input("Give me a number: "))
newList = []
for n in numbers:
    if userinput >= n:
        newList.append(n)
print(newList)
