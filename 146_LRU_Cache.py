from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
        
'''
Runtime: 1159 ms, faster than 31.75% of Python3 online submissions for LRU Cache.
Memory Usage: 74.9 MB, less than 97.51% of Python3 online submissions for LRU Cache.
'''