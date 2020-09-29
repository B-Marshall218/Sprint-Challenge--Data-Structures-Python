class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # set this node variable as current
        current = self.head
        # If there is no head return nothing
        if self.head is None:
            return
        # If there is a node on the head
        if self.head.next_node:
            # while something exists in the head
            while current is not None:
                # next is going to be what the current node is
                # plus the next node
                next = current.next_node
                # set the new node to = prev
                current.next_node = prev
                # Set prev to actually be the current node
                prev = current
                # Since the current node is now heading to previous
                # calling the next node will go to the prev one
                current = next
            # declaring the new head to be the previous node
            self.head = prev
            # ?? Im a little confused as to why this failed as self.head = next
        else:
            # return the current head if there is a current node
            return self.head

        # if self.previous = current node
        # then current node = next
        # next = current node
"""
if node is None: 
    return None
if node.get_next() == None:
    self.head = node
    self.head.next_node = prev 
    return 
self.reverse_list(node.get_next(), node) 
node.next_node = prev 
"""
