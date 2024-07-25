def is_eligible(m, p, c):
    if m >= 60 and p >= 50 and c >= 40:
        if m + p + c >= 200 or m + p >= 150:
            return True
    return False

n = int(input("Enter the number of students: "))

eligible = []

for i in range(n):
    print("Enter marks for student", i+1, ":")
    m = float(input("Mathematics: "))
    p = float(input("Physics: "))
    c = float(input("Chemistry: "))

    if is_eligible(m, p, c):
        eligible.append(i+1)

if eligible:
    print("The eligible candidates are:", eligible)
else:
    print("No eligible candidates.")