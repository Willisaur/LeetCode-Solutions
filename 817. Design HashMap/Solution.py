class MyHashMap:
    def __init__(self):
        self.store = list()

    def put(self, key: int, value: int) -> None:
        flag = False
        for i in range(len(self.store)):
            if self.store[i][0] == key:
                self.store[i][1] = value
                flag = True
                break
        if not flag:
            self.store.append([key, value])

    def get(self, key: int) -> int:
        for i in range(len(self.store)):
            if self.store[i][0] == key:
                return self.store[i][1]
        return -1

    def remove(self, key: int) -> None:
        flag = False
        for i in range(len(self.store)):
            if self.store[i][0] == key:
                self.store.pop(i)
                break

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)