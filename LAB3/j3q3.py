class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} to the queue.")

    def dequeue(self):
        if len(self.queue) < 1:
            return "Queue is empty."
        item = self.queue.pop(0)
        print(f"Dequeued {item} from the queue.")
        return item

    def display(self):
        if len(self.queue) < 1:
            print("Queue is empty.")
        else:
            print("Queue:", self.queue)

def main():
    q = Queue()
    while True:
        print("\nChoose an operation:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Exit")

        choice = int(input("Enter choice: "))
        if choice == 1:
            item = input("Enter item to enqueue: ")
            q.enqueue(item)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.display()
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
