class Vector:
    def __init__(self, nums):
       self.nums = nums
       self.dims = len(nums)
       self.norm = self._length()

    def __eq__(self, other):
        return self.nums == other.nums

    def _length(self):
        return sum([num**2 for num in self.nums])**0.5

    def unit_vector(self):
        return Vector([n/self.norm for n in self.nums])

    def scale(self, scalar):
        return Vector([num*scalar for num in self.nums])

    