class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

def main():
    person_name = input("Enter the name: ")
    person_age = int(input("Enter the age: "))
    
    person = Person(person_name, person_age)
    
    person.display_info()

if __name__ == "__main__":
    main()
