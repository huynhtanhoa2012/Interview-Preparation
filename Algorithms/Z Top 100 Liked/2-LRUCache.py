"""
+ Keep track capacity
+ Double Linked List to insert and remove O(1)
    + Left: dummy node store LRU
    + Right: dummy node store the most recently used
+ Hashmap to get in O(1)
    + key: the same key from input
    + value: the pointer to the node
+ Node:
    + next pointer
    + prev pointer
"""


class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}     # map key to nodes

        # dummy pointers to store LRU and MRU
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right  # connect 2 dummy nodes
        self.right.next = self.left

    # remove from the list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    # insert at right
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete from the hashmap
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]

        return 0