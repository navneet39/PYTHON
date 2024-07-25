n = 4

for i in range(1, n + 1):
    for j in range(1, i):
        print(" ", end="")
    print(i, end="")
    for k in range(1, 2 * (n - i) + 1):
        print(" ", end="")
    if i < n:
        print(i, end="")
    print()