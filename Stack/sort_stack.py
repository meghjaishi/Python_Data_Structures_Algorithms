class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

def sort_stack(stack):
    sorting_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()

        while not sorting_stack.is_empty() and sorting_stack.peek() > temp:
            stack.push(sorting_stack.pop())

        sorting_stack.push(temp)
    
    while not sorting_stack.is_empty():
        stack.push(sorting_stack.pop())

if __name__ == "__main__":
    stack = Stack()
    stack.push(34)
    stack.push(3)
    stack.push(31)
    stack.push(98)
    stack.push(92)
    stack.push(23)

    print("Original Stack:")
    stack.print_stack()

    sort_stack(stack)

    print("\nSorted Stack:")
    stack.print_stack()
