class MethodOverloading:
    def display(self, num):
        if isinstance(num, int):
            print(f"Integer: {num}")
        elif isinstance(num, float):
            print(f"Double: {num}")
        else:
            print("Unsupported type")

def main():
    m1 = MethodOverloading()
    m1.display(10)    
    m1.display(10.5)  

if __name__ == "__main__":
    main()
