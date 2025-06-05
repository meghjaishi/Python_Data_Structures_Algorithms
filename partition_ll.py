## partitioning the linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1
        
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def partition_ll(self, x):
        if not self.head:
            return None
        
        else:
            dummy_1 = Node(0)
            dummy_2 = Node(0)

            prev_1 = dummy_1
            prev_2 = dummy_2

            current = self.head
            while current:
                if current.value < x:
                    prev_1.next = current
                    prev_1 = prev_1.next
                else:
                    prev_2.next = current
                    prev_2 = prev_2.next
                current = current.next
            
            prev_2.next = None # Terminate the linked list
            prev_1.next = dummy_2.next
            self.head = dummy_1.next

if __name__ == "__main__":
    ll = LinkedList(3)
    ll.append(5)
    ll.append(8)
    ll.append(5)
    ll.append(10)
    ll.append(2)
    ll.append(1)

    print("Original List:")
    ll.print_list()

    x = 5
    ll.partition_ll(x)

    print(f"Partitioned List around {x}:")
    ll.print_list()
