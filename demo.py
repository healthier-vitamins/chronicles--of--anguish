# if 
x = int(input("x: "))

if x < 10:
    print("x is less than 10")
else:
    print("x is more than equals 10")

y = int(input("y: "))

if y >= 10:
    print("y is more than equal 10")
else:
    print("yay")

# switch
user_input = input("enter a number between 1 to 5: ")

match user_input:
    case "1":
        print("1")
    case "2":
        print("2")
    case "3":
        print("3")
    case "4":
        print("4")
    case "5":
        print("5")
    case _:
        print("only numbers 1 - 5")

day_input = input("monday - friday: ")
lowered = day_input.lower()

match lowered:
    case "monday":
        print("monday")
    case "tuesday":
        print("tuesdat")
    case "wednesday":
        print("wednesday")
    case "thursday":
        print("thursday")
    case "friday":
        print("friday")
    case _:
        print("only monday - friday")
