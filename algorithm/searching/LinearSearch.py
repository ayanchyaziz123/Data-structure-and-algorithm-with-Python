class LinearSearch:
    def __init__(self, arr: list, length: int)-> None:
        self.arr = arr
        self.length = length
    def linearSearch(self, target: int)-> bool:
        for ind in range(0, len(self.arr)):
            if(self.arr[ind] == target):
                return True
        return False

arr = [1, 2, 3, 4, 5, 6]
ls = LinearSearch(arr, len(arr))
print(ls.linearSearch(3))
