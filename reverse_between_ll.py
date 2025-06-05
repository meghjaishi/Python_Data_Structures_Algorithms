## reverse between method for linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def LinkedList(self, value):
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

if __name__ == "__main__":
    ll = Node(0)
    ll.LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    print("Original List:")
    ll.print_list()

    start = 1
    end = 4
    ll.reverse_between(start, end)

    print(f"List after reversing between positions {start} and {end}:")
    ll.print_list()