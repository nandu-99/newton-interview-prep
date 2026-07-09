# LRU (Least Recently Used)

# The idea
# Instead of asking:
# "Who came first?"

# LRU asks:
# "Who hasn't been used for the longest time?"

# Every time you access or insert an item, it becomes the most recently used.
# When the cache is full, remove the item that hasn't been touched for the longest time.

##SETUP 

class Node:
    def __init__(self, key, value):
        self.key = key 
        self.value = value 
        self.next = None 
        self.prev = None 
    
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail 
        self.tail.prev = self.head 
    
    def remove(self, node):
        prv = node.prev 
        nxt = node.next 

        prv.next = nxt 
        nxt.prev = prv 

    def insert(self, node):
        prv = self.tail.prev 

        prv.next = node 
        node.prev = prv 

        node.next = self.tail 
        self.tail.prev = node 
    
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node 

        if(len(self.cache)  > self.capacity):
            lru = self.head.next 
            self.remove(lru)
            del self.cache[lru.key]
        
    def get(self, key):
        if key not in self.cache:
            return -1 
        
        node = self.cache[key]

        self.remove(node)
        self.insert(node)
        
        print(f"Get, {node.value}")
    
    def display(self):
        curr = self.head.next 

        while curr!=self.tail:
            print(curr.value, end=" ")
            curr = curr.next 
        
        print()
    

cache = LRUCache(3)

cache.put(1, 10)
cache.put(2, 20)
cache.put(3, 30)
cache.display()

cache.get(1)
cache.display()

cache.put(4, 40)
cache.display()

cache.get(2)
cache.display()

cache.put(5, 50)
cache.display()

