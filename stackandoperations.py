#stack and operations on stack
#push, pop, peek, size, if empty, exit
class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack == 0):
            print("Stack is Empty, nothing to pop!")
            return None
        return self.stack.pop()
    
    def peek(self):
        if len (self.stack == 0):
            print("Stack is Empty, nothing to view!")
            return None
        else:
            return self.stack[-1]
    
    def ifempty(self):
        if len (self.stack == 0):
            print("Stack is empty!")
        else:
            print("Stack is NOT empty.")
    
    def size(self):
        return len(self.stack)
    

while True:
    print("\n1. Push\n2. Pop\n3. Peek\n4. Is Empty\n5. Size\n6. Exit")

    choice = (int(input("Enter your choice: ")))
    if choice == 1:
        item = int(input("Enter Element to push: "))
        stack.push(item)
        print (f"stack after push: {stack.stack}")

    elif choice == 2:
        print (f"Element popped: {stack.pop()}")
        print (f"stack after pop: {stack.stack}")

    elif choice == 3:
        print (f"Element at top of stack: {stack.peek()}")

    elif choice == 4:
        print (stack.ifempty())

    elif choice == 5:
        print (f"Size of stack: {stack.size()}")

    elif choice == 6:
        print ("Exiting program.")
        break
    else:
        print ("Invalid choice, try again!")