class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

def main():
    my_dog = Dog()
    my_dog.sound()  

if __name__ == "__main__":
    main()
