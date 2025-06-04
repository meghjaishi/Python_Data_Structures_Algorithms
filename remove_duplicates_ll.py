## remove duplicates from linkedlist
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
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def print_list(self):
        if self.head is None:
            print("List is empty")

        else:
            temp = self.head
            values = []
            while temp:
                values.append(temp.value)
                temp = temp.next
            print(" -> ".join(map(str, values)))

    def remove_duplicates_on2(self):
        
        current = self.head

        while current:
            runner = current
            while runner.next:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                    self.length -= 1
                else:
                    runner = runner.next
            
            current = current.next

    def remove_duplicates(self):
        values = set()

        previous = None
        current = self.head
        while current:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = current
            current = current.next

if __name__ == "__main__":
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(2)
    ll.append(4)
    ll.append(3)

    print("Original List:")
    ll.print_list()

    ll.remove_duplicates()

    print("List after removing duplicates:")
    ll.print_list()
    # Output should be: 1 -> 2 -> 3 -> 4
    