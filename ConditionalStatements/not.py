age = int(input())

if not ((age >= 2 and age <= 8) or age >= 65):
    print("You are not a child or senior")
else:
    print("You are a child or senior")
