def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

input_num = int(input("Enter a number: "))
multiplication_table(input_num)