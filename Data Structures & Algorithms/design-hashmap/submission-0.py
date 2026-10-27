class MyHashMap:

    def __init__(self):
        self.hashmap = [[]] * 1000

    def put(self, key: int, value: int) -> None:
        index = int(key % len(self.hashmap))
        for i in range(len(self.hashmap[index])):
            k, v = self.hashmap[index][i][0], self.hashmap[index][i][1]
            if k == key:
                self.hashmap[index][i][1] = value
                return
        self.hashmap[index].append([key,value])

    def get(self, key: int) -> int:
        index = int(key % len(self.hashmap))
        for i in range(len(self.hashmap[index])):
            k, v = self.hashmap[index][i][0], self.hashmap[index][i][1]
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = int(key % len(self.hashmap))
        # print(self.hashmap)
        i = 0
        while i < len(self.hashmap[index]):
            k, v = self.hashmap[index][i][0], self.hashmap[index][i][1]
            if k == key:
                del self.hashmap[index][i]
            else:
                i += 1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)