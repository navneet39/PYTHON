class Parent:
    def show():
        print("Parent's static method")

class Child(Parent):
    def show():
        print("Child's static method")

def main():
    Parent.show()  
    Child.show()   

if __name__ == "__main__":
    main()
