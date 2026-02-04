# Binary Search Tree Implementation in Python
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

    def contains(self, value): # iterative approach
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
    
    def __r_contains(self, current_node, value): # recursive contains helper method
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
    
    def r_contains(self, value): # public method for recursive contains
        return self.__r_contains(self.root, value)
    
    def __r_insert(self, current_node, value): # recursive insert helper method
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    
    def r_insert(self, value): # public method for recursive insert
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
    
    def min_value(self, current_node):
        while current_node.left != None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left,value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right,value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node
    
    def delete(self, value):
        self.__delete_node(self.root, value)

    # Breadth first search method:
    def bfs(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    # depth first search methods preorder
    def dfs_pre_order(self):
        results = []
        
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return results
    
    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results
    
    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results


if __name__ == "__main__":
    bst = BinarySearchTree()
    print(bst.insert(47))  # True
    print(bst.insert(21))  # True
    print(bst.insert(76))  # True
    print(bst.insert(18))  # True
    print(bst.insert(27))  # True
    print(bst.insert(52))  # True
    print(bst.insert(82))  # True

    # print(bst.min_value(bst.root))  # 18
    # print(bst.min_value(bst.root.right))  # 52


    # print(bst.root.value)
    # print(bst.root.left.value)
    # print(bst.root.right.value)

    # print(bst.contains(27))  # True
    # print(bst.contains(17))  # False

    # print(bst.r_contains(27))
    # print(bst.r_contains(17))
    # bst.r_insert(2)
    # bst.r_insert(1)
    # bst.r_insert(3)
    # print(bst.root.value)
    # print(bst.root.left.value)
    # print(bst.root.right.value)

    # bst.delete(2)
    # print(bst.root.value)
    # print(bst.root.left.value)
    # print(bst.root.right)
    # print(bst.bfs())
    print(bst.dfs_in_order()) 