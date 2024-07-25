def div(n):
    return n % 7 == 0 and n % 5 != 0

print("Numbers divisible by 7 but not multiples of 5:")
for num in range(1000, 2001):
    if div(num):
        print(num)
