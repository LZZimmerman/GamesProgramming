asterisk="*"
nestedAsteriskList=[asterisk]
#nestedAsteriskList.extend(nestedAsteriskList)
count=0
for i in nestedAsteriskList:
    print(*nestedAsteriskList)
    if count < 10:
        count+=1
        if len(nestedAsteriskList) <10:
            nestedAsteriskList.extend(asterisk)

