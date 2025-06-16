## partition a dll
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
        current = self.head
        while current:
            print(current.value)
            current = current.next
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
    def partition(self, x):
        if not self.head:
            return None
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
        while current:
            if current.value < x:
                prev1.next = current
                current.prev = prev1
                prev1 = current
            else:
                prev2.next = current
                current.prev = prev2
                prev2 = current
            current = current.next

        prev1.next = dummy2.next
        if dummy2.next:
            dummy2.next.prev = prev1
        prev2.next = None
        
        self.head = dummy1.next
        self.head.prev = None

if __name__ == "__main__":
    dll = DoublyLinkedList(3)
    dll.append(5)
    dll.append(8)
    dll.append(5)
    dll.append(10)
    dll.append(2)
    dll.append(1)
    
    print("Original list:")
    dll.print_list()
    
    x = 5
    dll.partition(x)
    
    print(f"\nPartitioned list around {x}:")
    dll.print_list()