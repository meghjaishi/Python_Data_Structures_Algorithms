## Find kth node from the end of a linked list
from linked_list import LinkedList

def find_kth_from_end(ll, k):
    if k <= 0:
        return None
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        if fast == None:
            return None
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow

# Example usage:
linkedlist = LinkedList(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)
linkedlist.append(5)
linkedlist.append(6)
linkedlist.append(7)

k = 3
kth_node = find_kth_from_end(linkedlist, k)

print(f"The {k}th node from the end is: {kth_node.value}")