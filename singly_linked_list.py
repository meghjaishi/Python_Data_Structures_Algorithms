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
    
    def bubble_sort(self):
        if self.length < 2:
            return    
        for _ in range(self.length):
            current = self.head
            while current.next is not None:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                current = current.next

    def selection_sort(self):
        if self.length < 2:
            return 
        
        current = self.head
        while current is not None:
            min = current
            inner = current.next
            while inner is not None:
                if inner.value < min.value:
                    min = inner
                inner = inner.next
            
            if min != current:
                current.value, min.value = min.value, current.value
            current = current.next

    def selection_sort_node(self):
        if self.length < 2:
            return
        
        dummy = Node(0)
        dummy.next = self.head

        prev_current = dummy
        while prev_current.next is not None:
            current = prev_current.next
            min_node = current
            prev_min = prev_current

            search_prev = current
            while search_prev.next is not None:
                if search_prev.next.value < min_node.value:
                    min_node = search_prev.next
                    prev_min = search_prev
                search_prev = search_prev.next
            
            if min_node != current:
                if current.next == min_node:
                    current.next = min_node.next
                    min_node.next = current
                    prev_current.next = min_node
                else:
                    temp_next = current.next
                    current.next = min_node.next
                    min_node.next = temp_next
                    prev_current.next = min_node
                    prev_min.next = current

                current = min_node
            
            prev_current = current
        self.head = dummy.next

    def insertion_sort(self):
        if self.length < 2:
            return
        
        sorted_list_head = self.head
        unsorted_list_head = self.head.next
        sorted_list_head.next = None # This breaks the head and creates new linked list

        while unsorted_list_head is not None:
            current = unsorted_list_head
            unsorted_list_head = unsorted_list_head.next
            if current.value < sorted_list_head.value:
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                search_pointer = sorted_list_head
                while search_pointer.next is not None and search_pointer.next.value < current.value:
                    search_pointer = search_pointer.next
                
                current.next = search_pointer.next
                search_pointer.next = current
                
        self.head = sorted_list_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp

    def merge(self, other_list):
        dummy = Node(0)
        current = dummy

        other_head = other_list.head
        while self.head is not None and other_head is not None:
            if self.head.value < other_head.value:
                current.next = self.head
                self.head = self.head.next
            else:
                current.next = other_head
                other_head = other_head.next
            current = current.next
        if self.head is not None:
            current.next = self.head
        else:
            current.next = other_head
            self.tail = other_list.tail
        self.head = dummy.next
        self.length += other_list.length



if __name__ == "__main__":

    # Example usage of the LinkedList class methods
    # my_linked_list = LinkedList(4)
    # my_linked_list.append(5)
    # my_linked_list.append(3)
    # my_linked_list.append(1)
    # my_linked_list.append(2)

    # print(my_linked_list.remove(2), '\n')
    # my_linked_list.insert(1,1)
    # print(my_linked_list.get(-1))
    # my_linked_list.prepend(1)
    # my_linked_list.set_value(1,4)
    # print(my_linked_list.tail.value)
    # my_linked_list.print_list()

    # my_linked_list.bubble_sort()
    # print("Sorted:")
    # my_linked_list.print_list()
    # (2) Items - Returns 2 Node 
    # print(my_linked_list.pop_first())

    # (1) Item - Returns 1 Node
    # print(my_linked_list.pop_first())

    # (0) Items - Returns None
    # print(my_linked_list.pop_first())

    l1 = LinkedList(1)
    l1.append(3)
    l1.append(5)
    l1.append(7)


    l2 = LinkedList(2)
    l2.append(4)
    l2.append(6)
    l2.append(8)

    l1.merge(l2)

    l1.print_list()