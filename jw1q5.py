import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * (radius ** 2)

perimeter = 2 * math.pi * radius

print(f"The area of the circle is: {area:.2f}")
print(f"The perimeter (circumference) of the circle is: {perimeter:.2f}")
