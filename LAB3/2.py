def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return "Undefined (the line is vertical)"
    else:
        slope = (y2 - y1) / (x2 - x1)
        return slope

try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    
    slope = calculate_slope(x1, y1, x2, y2)
    print(f"The slope of the line is: {slope}")
except ValueError:
    print("Invalid input. Please enter numerical values.")
