## swap pairs in dll
class Node:
    def __init__(self, value_):
        self.value = value_
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(values) if values else "Empty")
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
    def swap_pairs(self):
        if self.length <= 1:
            return
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
        previous = dummy
        first = previous.next

        while first and first.next:
            second = first.next

            first.next = second.next
            if second.next:
                second.next.prev = first
            
            second.next = previous.next
            previous.next.prev = second

            previous.next = second
            second.prev = previous

            previous = first
            first = first.next

        self.head = dummy.next
        self.head.prev = None

if __name__ == "__main__":
    dll = DoublyLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.append(7)
    
    print("Original List:")
    dll.print_list()
    
    dll.swap_pairs()
    
    print("After Swapping Pairs:")
    dll.print_list()