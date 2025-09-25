canDrive = True
if canDrive == True:
    print("You can drive!")

age = 25
if age >= 18:
    print("You can vote!")

age = 15
if age >= 16:
    print("You can get a license!")
else:
    print("Sorry, you can't get a license.")

money = 15.00
if money >= 15.00:
    print("You can afford the item!")
elif money >= 14.00:
    print("Just a little more money and you'll be able to buy the item!")
else:
    print("Sorry, you can't afford this item.")

age = int(input("How old are you?"))
if age >= 21:
    print("You can drink!")
else:
    print("Sorry, you can't drink.")