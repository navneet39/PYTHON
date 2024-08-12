student = {}

student['first_name'] = input("Enter the student's first name: ")
student['last_name'] = input("Enter the student's last name: ")
student['gender'] = input("Enter the student's gender: ")
student['age'] = int(input("Enter the student's age: "))
student['marital_status'] = input("Enter the student's marital status: ")
student['skills'] = input("Enter the student's skills (separated by commas): ").split(',')
student['country'] = input("Enter the student's country: ")
student['city'] = input("Enter the student's city: ")
student['address'] = input("Enter the student's address: ")

# I. Get the length of the student dictionary
print("\nLength of student dictionary:", len(student))

# II. Get the value of skills and check the data type, it should be a list
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))

# III. Modify the skills values by adding one or two skills
new_skills = input("Enter additional skills to add (separated by commas): ").split(',')
student['skills'].extend(new_skills)
print("Updated skills:", student['skills'])

# IV. Get the dictionary keys as a list
keys_list = list(student.keys())
print("Dictionary keys:", keys_list)

# V. Get the dictionary values as a list
values_list = list(student.values())
print("Dictionary values:", values_list)

# VI. Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print("Dictionary as list of tuples:", student_items)

# VII. Delete one of the items in the dictionary
key_to_delete = input("Enter the key of the item to delete from the dictionary: ")
if key_to_delete in student:
    del student[key_to_delete]
    print(f"Item with key '{key_to_delete}' has been deleted.")
else:
    print(f"Key '{key_to_delete}' not found in the dictionary.")

# VIII. Delete the student dictionary completely
delete_dictionary = input("Do you want to delete the entire student dictionary? (yes/no): ").strip().lower()
if delete_dictionary == 'yes':
    del student
    print("The student dictionary has been deleted.")
else:
    print("The student dictionary was not deleted.")
