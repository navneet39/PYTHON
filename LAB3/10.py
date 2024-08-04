def print_segment_display(n, num):
    segments = [
        [" _ ", "| |", "|_|"],  # 0
        ["   ", "  |", "  |"],  # 1
        [" _ ", " _|", "|_ "],  # 2
        [" _ ", " _|", " _|"],  # 3
        ["   ", "|_|", "  |"],  # 4
        [" _ ", "|_ ", " _|"],  # 5
        [" _ ", "|_ ", "|_|"],  # 6
        [" _ ", "  |", "  |"],  # 7
        [" _ ", "|_|", "|_|"],  # 8
        [" _ ", "|_|", " _|"]  # 9
    ]

    num_str = str(num)
    for i in range(3):
        for digit in num_str:
            print(segments[int(digit)][i], end=" ")
        print()

n = int(input("Enter the number of lines (N): "))
num = int(input("Enter the number to display: "))

if n <= 0:
    print("Please enter a positive integer for N.")
else:
    print_segment_display(n, num)