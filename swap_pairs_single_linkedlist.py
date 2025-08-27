## swap pairs in single linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        if self.length == 0:
            print("Empty linked list")

        else:
            values = []
            temp = self.head
            while temp:
                values.append(str(temp.value))
                temp = temp.next
            result = " -> ".join(values) if values else "Empty"
            print(result + " -> None")
        return result
    
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def swap_pairs(self):
        if self.length <= 1:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        first = prev.next

        while first and first.next:
            second = first.next
            # swap the nodes
            first.next = second.next
            prev.next = second
            second.next = first
            # move the pointers forward
            prev = first
            first = first.next

        self.head = dummy.next

if __name__ == "__main__":
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None
    ll.swap_pairs()
    ll.print_list()  # Output: 2 -> 1 -> 4 -> 3 -> 5 -> None