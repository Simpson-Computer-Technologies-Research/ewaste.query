
# // Cache class
class Cache:
    def __init__(self):
        self.data = {}
    
    # // Insert data into the cache
    def insert(self, key: str, value: str) -> None:
        if key not in self.data:
            self.data[key] = value
        else:
            self.data[key] = value
        
        # // Overflow handling
        if len(self.data) > 10:
            del self.data[len(self.data) - 1]
    
    # // Cache a value from the cache
    def get(self, key: str) -> str:
        return self.data[key]

    # // Check if key exists in the cache
    def exists(self, key: str) -> bool:
        return key in self.data