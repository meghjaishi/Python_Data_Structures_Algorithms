class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True ## returning True to indicate successful insertion
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False ## returning False to indicate value already exists
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        # if self.root is None: # redundant check as while loop handles it
        #     return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

if __name__ == "__main__":
    bst = BinarySearchTree()
    print(bst.insert(10))  # True
    print(bst.insert(5))   # True
    print(bst.insert(15))  # True
    print(bst.insert(10))  # False, duplicate value

    print(bst.root.value)
    print(bst.root.left.value)
    print(bst.root.right.value)

    print(bst.contains(15))  # True
    print(bst.contains(99))  # False