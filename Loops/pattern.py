for i in range(0, 4):
    for j in range(0, i):
        # print("\U0001f600")
        print("\U0001f600", end="")
    print()

k = 1
l = 3
m = 3
for i in range (4):
    print(" " * l, end="")
    l -= 1
    for j in range(1 , m):
        print(k, end=" ")
        k += 1
    print()
    m+=2
 