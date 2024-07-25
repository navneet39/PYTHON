import math

def compute_e(n):
    e = 1.0
    for i in range(1, n + 1):
        e += 1.0 / math.factorial(i)
    return e

n = int(input("Enter the number of terms: "))
e = compute_e(n)
print("The approximate value of Euler's number (e) is:", e)