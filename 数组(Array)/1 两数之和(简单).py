# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
from typing import List

# 方案1 对撞指针
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = nums.copy()
        new_list.sort()
        start = 0
        end = len(nums) - 1
        while start < end:
            if new_list[start] + new_list[end] < target:
                start += 1
            elif new_list[start] + new_list[end] > target:
                end -= 1
            else:
                break
        p = nums.index(new_list[start])
        nums.pop(p)
        q = nums.index(new_list[end])
        if q >= p:
            q += 1
        return [p, q]


# 方案2 创建字典
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for i, num in enumerate(nums):
            if target - num in new_dict:
                return [i, new_dict[target - num]]
            else:
                new_dict[num] = i


# 方案3 暴力解法(冒泡排序)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for slow in range(len(nums)-1):
            for fast in range(slow+1,len(nums)):
                if nums[slow] + nums[fast] == target:
                    return slow,fast