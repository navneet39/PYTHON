def main():
    user_input = input("Enter a comma-separated sequence of words: ")
    words = user_input.split(',')
    words.sort()
    sorted_words = ','.join(words)
    print(sorted_words)

if __name__ == "__main__":
    main()
