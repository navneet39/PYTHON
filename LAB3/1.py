def check_season(month):
    month = month.lower()
    if month in ["december", "january", "february"]:
        return "Winter"
    elif month in ["march", "april", "may"]:
        return "Spring"
    elif month in ["june", "july", "august"]:
        return "Summer"
    elif month in ["september", "october", "november"]:
        return "Autumn"
    else:
        return "Invalid month"


user_input = input("Enter a month: ")
season = check_season(user_input)
print(f"The season is: {season}")
