## reverse between method for linked list
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
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start, end):
        if self.length <=1:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for _ in range(start):
            prev = prev.next

        current = prev.next

        for _ in range(end - start):
            to_move = current.next
            current.next = to_move.next
            to_move.next = prev.next
            prev.next = to_move

        self.head = dummy.next

    def swap_pairs(self): 
        if self.length <=  1:
            return 
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        first = prev.next
        
        while (first and first.next):
            second = first.next
            # swap the pair
            first.next = second.next
            prev.next = second
            second.next = first
            # move to the next pair
            prev = first 
            first = first.next
            
        self.head = dummy.next

if __name__ == "__main__":
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    # ll.append(6)

    print("Original List:")
    ll.print_list()

    
    ll.swap_pairs()
    print(f"List after swapping pairs:")
    ll.print_list()

    