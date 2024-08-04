def main():
    user_input = input("Enter a sentence: ")

    letter_count = 0
    digit_count = 0

    for char in user_input:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1

    print(f"LETTERS {letter_count}")
    print(f"DIGITS {digit_count}")

if __name__ == "__main__":
    main()
