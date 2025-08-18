class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.cache.move_to_end(key, last=True)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #print(self.cache)
        self.cache[key] = value
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
        if len(self.cache.keys()) > self.capacity:
            a = self.cache.popitem(last=False)
            #print(a)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)