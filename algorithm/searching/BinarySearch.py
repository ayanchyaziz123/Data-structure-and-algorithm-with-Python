class BinarySearch:
    def __init__(self, arr: list, length: int)-> None:
        self.arr = arr
        self.length = length
    def binarySearch(self, target: int)-> None:
        left = 0
        right = self.length - 1
        while(left <= right):
            mid = (left + right) // 2
            if(self.arr[mid] == target):
                return True
            elif(self.arr[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        return False        
arr = [1, 2, 3, 4, 5]
length = len(arr)
bs = BinarySearch(arr, length)
print(bs.binarySearch(10))



