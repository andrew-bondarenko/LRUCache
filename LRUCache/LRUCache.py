from DoublyLinkedList import DoublyLinkedList
from KVPair import KVPair


class LRUCache(object):
    def __init__(self, max_size=6):
        if max_size <= 0:
            raise Exception('Maximum Cache size must be greater than 0.')
        self.max_size = max_size
        self.dllist = DoublyLinkedList()
        self.cache_nodes = {}

    def put(self, key, value):
        node = self.cache_nodes.get(key, None)
        
        # Check to see if the key already exists, if it does, update the value
        if node != None:
            node.data.value = value 
            self.dllist.move_to_front(node)
            return
         
        # Key did not exist, if the cache is full, remove least recently used key
        if self.dllist.capacity == self.max_size:
            lru_node = self.dllist.remove_tail()
            del self.cache_nodes[lru_node.data.key]

        # Add the key to the front of our cache
        self.cache_nodes[key] = self.dllist.unshift(KVPair(key, value))

    def get(self, key):
        node = self.cache_nodes.get(key, None)

        # Check to see if the key exists, if it doesn't, return None
        if node is None:
            return None

        # Key exists, return the value and move to the front of the DLL
        self.dllist.move_to_front(node)
        return node.data.value

    def delete(self, key):
        node = self.cache_nodes.get(key, None)

        # Check to see if the key exists, it it doesn't, return None
        if node is None:
            return

        # Key exists, remove it from the Cache
        delete_node = self.dllist.isolate(node)
        del self.cache_nodes[delete_node.data.key]
        
        # Now that we removed the node from the cache, update capacity 
        self.dllist.capacity -= 1

    def reset(self):
        self.max_size = 6
        self.dllist = DoublyLinkedList()
        self.cache_nodes = {}