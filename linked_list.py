## This is a class to create a node for a linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

## This class creates a data structure called Singly Linked list leveraging the Node class
## It provides data structure operations like print_list, append, prepend, pop, pop_first, get, set_value,
## insert, remove, and reverse with their respective time and space complexities
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # This method prints values of the linked list from head to tail
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Append method adds a new node with the given value to the end of the Linked list
    # with a time complexity of O(1) and space complexity of O(1)
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
        # if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # Pop method removes the last node from the Linked list and returns it 
    # with a time complexity of O(n) and space complexity of O(1)   
    def pop(self):
        if self.length == 0: # If the list is empty, return None
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0: # If the list is now empty, set head and tail to None
            self.head = None
            self.tail = None
        return temp

    # Prepend method adds a new node with the given value to the start of the Linked list
    # with a time complexity of O(1) and space complexity of O(1)
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True # Implemented here to use in this method with other methods
    
    # Pop first method removes the first node from the Linked list and returns it
    # with a time complexity of O(1) and space complexity of O(1)
    def pop_first(self):
        if self.length == 0: # If the list is empty, return None
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0: # If the list is now empty, set head and tail to None
            self.tail = None # Head is already set to None
        return temp
    
    # Get method retrieves the node at the specified index
    # with a time complexity of O(n) and space complexity of O(1)
    def get(self, index):
        if index < 0 or index >= self.length: # If the index is out of bounds, return None
            return None
        temp = self.head 
        for _ in range(index): # This logic works as temp is already at the head i.e. index 0
            temp = temp.next
        return temp
    
    # Set value method updates the value of the node at the specified index
    # with a time complexity of O(n) and space complexity of O(1)
    def set_value(self, index, value):
        temp = self.get(index) # Leverage the get method to find the node
        if temp:
            temp.value = value
            return True
        return False

    # Insert method adds a new node with the given value at the specified index
    # with a time complexity of O(n) and space complexity of O(1)
    def insert(self, index, value):
        if index < 0 or index > self.length: # Here index can be equal to length for appending a new node
            return False
        if index == 0:
            return self.prepend(value) # Leverage the prepend method for index 0
        if index == self.length:
            return self.append(value) # Leverage the append method for index equal to length
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True

    # Remove method removes the node at the specified index
    # with a time complexity of O(n) and space complexity of O(1)    
    def remove(self, index):
        if index < 0 or index >= self.length: # Deals with out of bounds index
            return None # Opposite of return a node if index is valid
        if index == 0:
            return self.pop_first() # Leverage the pop_first method for index 0
        if index == self.length - 1:
            return self.pop() # Leverage the pop method for the last index
        # For all other indices, we need to find the node before and at the index to remove
        prev = self.get(index - 1)
        temp = prev.next # More efficient than using self.get(index) i.e. O(n)
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    

    # Reverse method reverses the linked list in place
    # with a time complexity of O(n) and space complexity of O(1)
    def reverse(self):
        # This part swaps the head and tail pointers using a temp variable
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None # This will be the new tail
        after = temp.next # This will be the next node to process
        # Below loop iterates through the linked list and reverses the pointers 
        # without breaking the chain 
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


if __name__ == "__main__":

    # Example usage of the LinkedList class methods
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)

    # print(my_linked_list.remove(2), '\n')
    # my_linked_list.insert(1,1)
    # print(my_linked_list.get(-1))
    # my_linked_list.prepend(1)
    # my_linked_list.set_value(1,4)
    # print(my_linked_list.tail.value)
    my_linked_list.print_list()

    my_linked_list.reverse()
    print("Reversed:")
    my_linked_list.print_list()
    # (2) Items - Returns 2 Node 
    # print(my_linked_list.pop_first())

    # (1) Item - Returns 1 Node
    # print(my_linked_list.pop_first())

    # (0) Items - Returns None
    # print(my_linked_list.pop_first())