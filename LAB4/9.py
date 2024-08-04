def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == reverse_string(s)

def ends_with(s, substring):
    return s.endswith(substring)

def capitalize_words(s):
    return s.title()

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in s if char not in vowels)

def longest_word_length(sentence):
    words = sentence.split()
    if not words:
        return 0
    return len(max(words, key=len))

def main():
    user_input = input("Enter a string: ")

    # I. Reverse the string
    reversed_string = reverse_string(user_input)
    print(f"Reversed string: {reversed_string}")

    # II. Check whether the string is a palindrome
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

    # III. Check whether the string ends with a specific substring
    substring = input("Enter a substring to check if the string ends with it: ")
    if ends_with(user_input, substring):
        print(f"The string ends with '{substring}'.")
    else:
        print(f"The string does not end with '{substring}'.")

    # IV. Capitalize the first letter of each word in the string
    capitalized_string = capitalize_words(user_input)
    print(f"Capitalized string: {capitalized_string}")

    # V. Check if the string is an anagram of another string
    another_string = input("Enter another string to check for anagram: ")
    if is_anagram(user_input, another_string):
        print(f"The string is an anagram of '{another_string}'.")
    else:
        print(f"The string is not an anagram of '{another_string}'.")

    # VI. Remove vowels from the string
    string_without_vowels = remove_vowels(user_input)
    print(f"String without vowels: {string_without_vowels}")

    # VII. Find the length of the longest word in a sentence
    sentence = input("Enter a sentence to find the length of the longest word: ")
    longest_length = longest_word_length(sentence)
    print(f"The length of the longest word is: {longest_length}")

if __name__ == "__main__":
    main()
