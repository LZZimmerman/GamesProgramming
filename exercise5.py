#Problem solving V: Given a string, if its length is at least 3,
#add 'ing' to its end. Unless it already ends in 'ing', in which
#case add 'ly' instead. If the string length is less than 3,
#leave it unchanged. Print the resulting string.
word = input("Pick a random word: ")
#print (word[-3:])
#print (word + "ly")

#old code
#if (len(word) >=3 and word[-3:] != "ing"):
#    print (word + "ing")
#elif (len(word) >=3 and word[-3:] == "ing"):
#    print (word + "ly")
#else:
#    print (word)

#or
#elif (len(word) <3):
#    print (word)
#else:
#    print (word + "ly")

#revised
if len(word) >=3 and word[-3:] != "ing":
    print (word + "ing")
elif len(word) >=3:
    print (word + "ly")
else:
    print (word)
    
