# reverse between two indexes in a dll
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
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result
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
    def reverse_between(self, start, end):
        if self.length <= 1 or start == end:
            return 
        
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
        previous = dummy

        for _ in range(start):
            previous = previous.next
        current = previous.next
        for _ in range(end - start):
            node_to_move = current.next
            current.next = node_to_move.next
            if node_to_move.next:
                node_to_move.next.prev = current
            
            node_to_move.next = previous.next
            previous.next.prev = node_to_move

            previous.next = node_to_move
            node_to_move.prev = previous

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
    dll.append(8)
    
    print("Original List:")
    dll.print_list()
    
    start_index = 1  # 0-based index
    end_index = 4   # 0-based index
    dll.reverse_between(start_index, end_index)
    
    print(f"List after reversing between indexes {start_index} and {end_index}:")
    dll.print_list()