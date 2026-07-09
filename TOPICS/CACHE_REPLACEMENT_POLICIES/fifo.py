# FIFO is the easiest cache replacement policy to implement because it behaves exactly like a queue.

# Idea
# Cache has a fixed size.
# If the item already exists → do nothing (cache hit).
# If the cache has space → insert it at the end.
# If the cache is full → remove the oldest item (front of the queue), then insert the new one.

from collections import deque 

class FIFOcache:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.cache = set()
        self.queue = deque()

    def put(self, key):
        if key in self.cache:
            print("already exists in cache")
            return 
        
        if len(self.cache)==self.capacity:
            old = self.queue.popleft()
            self.cache.remove(old)
            print(f"removed {old}")
        
        self.queue.append(key)
        self.cache.add(key)
        print(f"inserted {key}")

    def display(self):
        print(list(self.queue))


cache = FIFOcache(3)

cache.put('A')
cache.display()

cache.put('B')
cache.display()

cache.put('C')
cache.display()

cache.put('D')
cache.display()

cache.put('E')
cache.display()

cache.put('F')
cache.display()
