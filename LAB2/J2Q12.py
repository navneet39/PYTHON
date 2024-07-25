def generate_combinations(n):
    for i in range(1, 4):
        if n == 1:
            print(i)
        else:
            for j in range(1, 4):
                if n == 2:
                    print(i, j)
                else:
                    for k in range(1, 4):
                        if n == 3:
                            print(i, j, k)

n = int(input("Enter the length of the combinations: "))
print("All combinations of 1, 2, or 3 of length", n, ":")
generate_combinations(n)