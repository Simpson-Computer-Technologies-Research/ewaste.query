
class Cache:
    def __init__(self):
        self.data = {}
    
    def insert(self, key: str, value: str) -> None:
        if key not in self.data:
            self.data[key] = value
        else:
            self.data[key] = value
        
        if len(self.data) > 10:
            del self.data[len(self.data) - 1]
    
    def get(self, key: str) -> str:
        return self.data[key]

    def exists(self, key: str) -> bool:
        return key in self.data