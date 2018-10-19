#excercise 1 & 2
words = ["xxx", "aaa", "r5t6yy", "g", "wow"]
count = 0
for i in words:
    if len(i)>1:
        count+=1

print(count)

numbers=[2,3,5,7,66,89,134]
userNumber= int(input("Give me a number: "))
for n in numbers:
    if userNumber>=n:
        continue
    print(n)