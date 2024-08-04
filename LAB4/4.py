def main():
    user_input = input("Enter a sequence of whitespace-separated words: ")
    words = user_input.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    result = ' '.join(sorted_words)
    print(result)

if __name__ == "__main__":
    main()
