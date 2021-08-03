from Node import Node


class DoublyLinkedList(object):
    def __init__(self):
        self.root = Node(None)
        self.length = 0

        self.root.next = self.root
        self.root.previous = self.root

    # Add a new node and move it to the front
    def add_head(self, data):
        node = Node(data)

        # New Node, add it to the front
        self.move_to_front(node)

        # Increase length by 1
        self.length += 1

        return node 

    # Move the node to the front
    def move_to_front(self, node):
        if node is None:
            return None 
        elif node.previous is not None and node.next is not None:
            # Remove previous/next pointers of this node so we can move it
            self.isolate(node)
        
        # Set the previous node of the node we're moving to the root
        node.previous = self.root

        # Set the next node of the node we're moving to the root's next node
        node.next = self.root.next

        # Update the root pointers 
        self.root.next.previous = node 
        self.root.next = node 

        return node 

    @staticmethod
    # Isolate the node and remove pointers
    def isolate(node):
        if node is None:
            return None 

        # Set the previous node to the next node
        node.previous.next = node.next
        # Set the next node to the prvious node
        node.next.previous = node.previous 

        # Remove pointers of our node
        node.next = None
        node.previous = None

        return node

    # Remove the last node in the list
    def remove_tail(self):
        if self.length == 0:
            return None 
        
        # Isolate the least recently used item
        remove_node = self.isolate(self.root.previous)

        # Reduce length by 1 now that we removed the tail node
        self.length -= 1
        
        return remove_node

    def remove_node(self, node):
        # Isolate the node
        remove_node = self.isolate(node)

        # Now that we removed the node, update length 
        self.length -= 1
        
        return remove_node