#stringA = "hi Chi a"
stringA = "hihihi"
count = 0
for i in range(len(stringA)-1):
    if stringA[i] == "h" and stringA[i+1]== "i":
        count += 1

print(count)

