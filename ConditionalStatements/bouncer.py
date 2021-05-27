age = input("How old are you: \n")
if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but need a wristband!")
    elif age >= 21:
        print("You can enter and drink!")
    else: 
        print("Sorry!")
else:
    print("Please enter an age")