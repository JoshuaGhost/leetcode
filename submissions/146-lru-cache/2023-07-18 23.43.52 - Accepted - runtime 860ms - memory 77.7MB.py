class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.value = {}
        self.next = {}
        self.prev = {}
        self.head = None
        self.tail = None

    def remove(self, key:int)->None:
        if self.tail == key:
            self.tail = None if key not in self.prev else self.prev[key]
            
        prev = self.prev.pop(key)
        next = self.next.pop(key)
        self.value.pop(key)
        if prev in self.next:
            self.next[prev] = next
        if next in self.prev:
            self.prev[next] = prev
        return None

    def appendhead(self, key: int, value:int) -> None:
        self.prev[key] = None
        self.next[key] = self.head
        self.value[key] = value
        if self.head is not None:
            self.prev[self.head] = key
        self.head = key
        if self.tail is None:
            self.tail = key
        return None

    def get(self, key: int) -> int:
        value = self.value.get(key, -1)
        if value != -1:
            if key != self.head:
                self.remove(key)
                self.appendhead(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.value:
            if key != self.head:
                self.remove(key)
                self.appendhead(key, value)
            else:
                self.value[key] = value
            return None
        
        if len(self.value) < self.c:
            self.appendhead(key, value)
            return None
        
        self.remove(self.tail)
        self.appendhead(key, value)
        return None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)