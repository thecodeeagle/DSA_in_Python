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

    def remove_last(self):
        if self.size == 0:
            raise IndexError("Pop from empty array")
        self.size-=1
        self.array[self.size]=None
        if self.size > 0 and self.size == self.capacity // 4:
            self._resize(self.capacity // 2)

        # Why Shrink at One-Fourth?
        # Shrinking at one-fourth instead of one-half avoids a situation called "thrashing."
        # Thrashing happens when you constantly grow and shrink the array as elements are added and removed.
        # By shrinking only when the size is much smaller, the dynamic array remains efficient.

    def __len__(self):
        return self.size

    def get(self, index):
        if index < 0 or index>=self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]

def test_dynamic_array():
    da = DynamicArray()
    assert len(da)==0

    # When you call len(da):
    # Python internally looks for the __len__() method in the DynamicArray class.

    for i in range(5):
        da.append(i)
        assert da.get(i) == i

    assert len(da)==5

    da.remove_last()
    assert len(da) == 4
    assert da.get(3) == 3

    print("Dynamic Array Tests Passed!")


if __name__ == "__main__":
    test_dynamic_array()




