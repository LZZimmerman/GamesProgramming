#stringA = "codecode"
stringA = "copecodetreccoe"
count = 0
for i in range(len(stringA)):
    try:
        if stringA[i] == "c" and stringA[i+1] == "o" and stringA[i+3] == "e":
            count += 1
    except IndexError:
       []



print(count)

