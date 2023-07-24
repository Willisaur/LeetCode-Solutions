class RandomizedSet:
    import random 

    def __init__(self):
        self.map = dict()

    def insert(self, val: int) -> bool:
        if (self.map.get(val, 0) == 1):
            # if the element exists already, return false
            return False
        else:
            # if the element doesn't exist, add it and return true
            self.map[val] = 1
            return True

    def remove(self, val: int) -> bool:
        if (self.map.get(val, 0) == 0):
            # if the element doesn't exist, return false
            return False
        else:
            # if the element does exist, remove it and return true
            del self.map[val]
            return True

    def getRandom(self) -> int:
        return list(self.map.keys())[random.randint(0, len(self.map.keys())-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()