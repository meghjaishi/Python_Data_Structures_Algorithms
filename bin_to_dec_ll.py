## Binary to Decimal Converter
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def print_list(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            values = []
            while temp:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values))
    
    def convert_to_decimal(self):
        current = self.head
        decimal_value = current.value

        while current.next:
            decimal_value = 2*decimal_value + current.next.value
            current = current.next
        return decimal_value
    
## Example usage
if __name__ == "__main__":
    binary_list = LinkedList(1)  # Start with the most significant bit
    binary_list.append(0)
    binary_list.append(1)
    binary_list.append(1)
    
    print("Binary Linked List:")
    binary_list.print_list()
    
    decimal_value = binary_list.convert_to_decimal()
    print(f"Decimal Value: {decimal_value}")