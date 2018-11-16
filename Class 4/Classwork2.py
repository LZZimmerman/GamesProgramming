while True:
    try:
        a= int(input("Give me a number: "))
        b= int(input("Give me another number: "))
        print(a/b)
    except ValueError:
        print("That is not a number!")
    except ZeroDivisionError:
        print("Can't divide by 0!")
    except:
        print("something unexpected happened!")