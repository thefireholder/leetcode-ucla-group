import random
class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        else: 
            self.list.append(val)
            self.dict[val] = len(self.list)
            return True
            
    def remove(self, val: int) -> bool:
        try: 
            self.dict.pop(val)
            self.list.remove(val)
            return True
        except KeyError:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list)

'''
Runtime: 492 ms, faster than 73.16% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 62 MB, less than 27.00% of Python3 online submissions for Insert Delete GetRandom O(1).
'''