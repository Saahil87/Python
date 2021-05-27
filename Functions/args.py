def sum(*args):
    total = 0
    for i in args:
        total += i
    return total

print(sum(1,2,3,4,5))
print(sum(1,2))