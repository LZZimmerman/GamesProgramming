asterisk="*"
nestedAsteriskLoop=[asterisk]
#nestedAsteriskLoop.extend(nestedAsteriskLoop)
count=0
for i in nestedAsteriskLoop:
    print(*nestedAsteriskLoop)
    if count < 10:
        count+=1
        if len(nestedAsteriskLoop) <10:
            nestedAsteriskLoop.extend(asterisk)

