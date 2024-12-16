

class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = [None]*self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize(2*self.capacity)
        self.array[self.size] = value
        self.size+=1

    def _resize(self, new_capacity):
        new_array = [None]*new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def pop(self):
        if self.size == 0:
            raise IndexError("Pop from e")
