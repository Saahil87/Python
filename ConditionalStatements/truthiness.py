animal = input("Enter your favorite animal")

if animal: #empty strings, objects and zero are falsy everything else is truthy!
    print(animal + " is my favorite too!")
else: 
    print("You didn't say anything")
