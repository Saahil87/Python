for i in range(1, 21):
    if i == 4 or i == 13:
        state = "UNLUCKY!"
    else:
        if i%2 == 0:
            state = "even"
        else:
            state = "odd"
    print(state)
