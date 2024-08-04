def main():
    user_input = input("Enter a string: ")

    string_length = len(user_input)
    print(f"The length of the string is: {string_length}")

    substring = "country"
    if substring in user_input:
        print(f'The substring "{substring}" is found in the string.')
    else:
        print(f'The substring "{substring}" is not found in the string.')

    word_counts = {}
    words = user_input.split()
    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalnum()).lower()
        if cleaned_word in word_counts:
            word_counts[cleaned_word] += 1
        else:
            word_counts[cleaned_word] = 1

    print("\nWord occurrences in the given string:")
    for word, count in word_counts.items():
        print(f"'{word}': {count}")

if __name__ == "__main__":
    main()
