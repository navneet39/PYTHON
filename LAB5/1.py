# List of student ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# I. Sort the list and find the min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)
print("Sorted ages:", ages)
print("Min age:", min_age)
print("Max age:", max_age)

# II. Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print("Ages after adding min and max again:", ages)

# III. Find the median age
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]
print("Median age:", median_age)

# IV. Find the average age
average_age = sum(ages) / len(ages)
print("Average age:", average_age)

# V. Find the range of the ages (max minus min)
age_range = max_age - min_age
print("Age range:", age_range)

# VI. Compare the value of (min - average) and (max - average), use abs() method
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print("Difference between min and average:", min_diff)
print("Difference between max and average:", max_diff)
