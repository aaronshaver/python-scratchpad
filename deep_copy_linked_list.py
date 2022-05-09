class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

"""
-constructs fresh instance of a node in a linked list
-acts recursively: defines the new object's node.next as coming from
    another call to this function so that all objects in the linked list
    are new instances (deep copy)
"""
def recurse(node):
    if not node:  # went past tail of list, so can exit instead of continuing to recurse
        return None
    return Node(node.value, recurse(node.next))

def deep_copy(node):
    return Node(node.value, recurse(node.next))

def print_linked_list(node):
    while True:
        print(node.value, hash(node))
        node = node.next
        if not node:
            print()
            break

# construct the initial linked list, from tail to head;
# head to tail wouldn't work: e.g. when constructing node1, node2 doesn't exist yet
# so we can't point to it yet
node4 = Node(4, None)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)

# just to show the initial values and hashes
print_linked_list(node1)

# call the method under test
new_list = deep_copy(node1)

# the values should be the same as the first linked list, but the hashes should
# be unique and different for the new list
print_linked_list(new_list)