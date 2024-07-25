import math

def geometric_sequence(first_term, common_ratio, num_terms):
    sequence = [first_term * (common_ratio ** i) for i in range(num_terms)]
    return sequence

num_terms = int(input("Enter the number of terms: "))

first_term = 2
common_ratio = 3

sequence = geometric_sequence(first_term, common_ratio, num_terms)

print("The first", num_terms, "terms of the geometric sequence are:", sequence)