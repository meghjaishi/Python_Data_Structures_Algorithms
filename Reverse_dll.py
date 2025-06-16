## Reverse a dll
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
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
    def reverse(self):
        if not self.head or not self.head.next:
            return
        current_node = self.head
        while current_node:
            temp_next = current_node.next
            current_node.next = current_node.prev
            current_node.prev = temp_next
            current_node = temp_next
        self.head, self.tail = self.tail, self.head # Swap head and tail

if __name__ == "__main__":
    dll = DoublyLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    print("Original List:")
    dll.print_list()
    
    dll.reverse()
    
    print("Reversed List:")
    dll.print_list()