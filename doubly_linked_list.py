## doubly linked list implementation
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head 
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    def set_Value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.prev = None
        temp.next = None
        self.length -= 1
        return temp

if __name__ == "__main__":
    dll = DoublyLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.print_list()
    print("\n")  # Output: 1, 2, 3
    dll.prepend(0)
    dll.print_list()  # Output: Popped node value: 3
    dll.pop_first()
    dll.print_list()  # Output: 0, 1, 2
    print("\n")  # Output: 0, 1, 2
    print(dll.get(2).value)  # Output: Node with value 2
    dll.set_Value(1, 5)
    dll.print_list()  # Output: 0, 5, 2
    dll.insert(1, 4)
    dll.print_list()  # Output: 0, 4, 5, 2
    print("\n")  # Output: 0, 4, 5, 2
    dll.remove(2)
    dll.print_list()  # Output: 0, 4, 2