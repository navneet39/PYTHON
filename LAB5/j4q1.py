# Base class
class Animal:
    def eat(self):
        print("This animal eats food.")

# Derived class
class Dog(Animal):
    def bark(self):
        print("The dog barks.")

def main():
    my_dog = Dog()
    my_dog.eat()  
    my_dog.bark() 

if __name__ == "__main__":
    main()
