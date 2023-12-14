import collections

def twoSum(nums, target):
    dict = {}
    for i, n in enumerate(nums):
        if(n in dict):
            return dict[n], i
        else:
            dict[target - n] = i

arr = [9, 8, 1, 2, 4]
twoSum(arr, 10)        