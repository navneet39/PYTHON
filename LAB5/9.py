season_dict = {
    1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Fall', 10: 'Fall',
    11: 'Fall', 12: 'Winter'
}

month_number = int(input("Enter the month number (1-12): "))

if 1 <= month_number <= 12:
    season = season_dict[month_number]
    print(f"The season for month {month_number} is {season}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
