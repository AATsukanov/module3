
def fucktorial(n : int):
    if n <= 1:
        return 1
    else:
        return n * fucktorial(n - 1)

for j in range(1, 101):
    print(j, '>>', fucktorial(j))