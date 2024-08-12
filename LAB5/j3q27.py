class Assignment:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

def main():
    print("Creating the first object with default values:")
    obj1 = Assignment()
    
    name = input("Enter name for the second object: ")
    print("Creating the second object with the provided name:")
    obj2 = Assignment(name)
    
    name = input("Enter name for the third object: ")
    age = int(input("Enter age for the third object: "))
    print("Creating the third object with the provided name and age:")
    obj3 = Assignment(name, age)
    
    print("\nDetails of obj1:")
    obj1.display_details()
    print("\nDetails of obj2:")
    obj2.display_details()
    print("\nDetails of obj3:")
    obj3.display_details()

if __name__ == "__main__":
    main()
