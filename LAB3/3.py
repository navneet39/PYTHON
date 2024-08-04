import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        root1 = (real_part, imaginary_part)
        root2 = (real_part, -imaginary_part)
        return (root1, root2)

try:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    solutions = solve_quadratic_eqn(a, b, c)
    if len(solutions) == 2 and isinstance(solutions[0], tuple):
        print(f"The solutions are complex: {solutions[0][0]} ± {solutions[0][1]}i")
    else:
        print(f"The solutions are: {solutions}")
except ValueError:
    print("Invalid input. Please enter numerical values.")
except ZeroDivisionError:
    print("Coefficient 'a' cannot be zero.")
