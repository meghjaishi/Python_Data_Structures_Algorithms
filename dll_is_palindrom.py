## check if dll is palindrome
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    def is_palindrome(self):
        if self.length <= 1:
            return True
        forward = self.head
        backward = self.tail
        for _ in range(self.length // 2):
            if forward.value != backward.value:
                return False
            forward = forward.next
            backward = backward.prev
        return True
if __name__ == "__main__":
    dll = DoublyLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.append(2)
    dll.append(1)
    dll.print_list()
    print("Is palindrome:", dll.is_palindrome())  # Output: True
    dll.append(4)
    print("Is palindrome:", dll.is_palindrome())  # Output: False