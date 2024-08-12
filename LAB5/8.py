person = {}

person['first_name'] = input("Enter the person's first name: ")
person['last_name'] = input("Enter the person's last name: ")
person['age'] = int(input("Enter the person's age: "))
person['country'] = input("Enter the person's country: ")
person['is_married'] = input("Is the person married? (yes/no): ").strip().lower() == 'yes'

# Process skills input
skills_input = input("Enter the person's skills (separated by commas): ")
# Remove quotes from skills input if present and split into list
skills = [skill.strip().replace("'", "") for skill in skills_input.split(',')]
person['skills'] = skills

person['address'] = {
    'street': input("Enter the person's street: "),
    'zipcode': input("Enter the person's zipcode: ")
}

# I. Check if the person dictionary has a skills key, if so print out the middle skill in the skills list
if 'skills' in person and person['skills']:
    skills = person['skills']
    middle_index = len(skills) // 2
    middle_skill = skills[middle_index]
    print("Middle skill:", middle_skill)

# II. Check if the person dictionary has a skills key, if so check if the person has 'Python' skill and print out the result
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("Has Python skill:", has_python)

# III. Determine the person's title based on skills
skills = person.get('skills', [])
skills_set = set(skills)
if skills_set == {'JavaScript', 'React'}:
    print('He is a front end developer')
elif skills_set == {'Node', 'Python', 'MongoDB'}:
    print('He is a backend developer')
elif skills_set == {'React', 'Node', 'MongoDB'}:
    print('He is a fullstack developer')
else:
    print('Unknown title')

# IV. If the person is married and lives in Finland, print the information in the specified format
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
else:
    print(f"{person['first_name']} {person['last_name']} does not live in Finland or is not married.")
