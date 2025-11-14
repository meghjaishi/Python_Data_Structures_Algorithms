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



def reverse_string(string):
    forward_stack = Stack()
    reversed_string = ""
    for i in string:
        forward_stack.push(i)
        
    length = forward_stack.size()
    while length > 0:
        reversed_string += forward_stack.pop()
        length -= 1 
    return reversed_string




my_string = 'Michael'

print ( reverse_string(my_string) )