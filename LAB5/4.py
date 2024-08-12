it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# I. Find the length of the set it_companies
print("Length of it_companies:", len(it_companies))

# II. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("It_companies after adding 'Twitter':", it_companies)

# III. Insert multiple IT companies at once to the set it_companies
new_companies = set(input("Enter IT companies to add (separated by commas): ").split(','))
it_companies.update(new_companies)
print("It_companies after adding new companies:", it_companies)

# IV. Remove one of the companies from the set it_companies
company_to_remove = input("Enter the IT company to remove: ")
it_companies.remove(company_to_remove) if company_to_remove in it_companies else print(f"{company_to_remove} not found in the set")
print("It_companies after removal:", it_companies)

# V. What is the difference between remove and discard
print("\nDifference between remove and discard:")
print("- 'remove()' will raise a KeyError if the item does not exist in the set.")
print("- 'discard()' will not raise an error if the item does not exist in the set.")
