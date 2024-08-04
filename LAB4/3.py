def main():
    print("Enter multiple lines of text (type 'END' to finish):")
    
    lines = []
    while True:
        line = input()
        if line == 'END':
            break
        lines.append(line)

    capitalized_lines = [line.upper() for line in lines]

    print("\nThe capitalized lines are:")
    for line in capitalized_lines:
        print(line)

if __name__ == "__main__":
    main()
