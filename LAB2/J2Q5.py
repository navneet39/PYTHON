def multiples(start, end):
    for i in range(start, end + 1):
        if i % 10 == 0:
            print(i)

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

if start > end:
    print("Invalid interval. Start should be less than or equal to end.")
else:
    print("Multiples of 10 between", start, "and", end, "are:")
    multiples(start, end)