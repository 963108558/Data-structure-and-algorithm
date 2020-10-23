# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
# 使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # result = float('inf')
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                about = nums[start] + nums[end] + nums[i]
                if about < target:
                    start +=1
                elif about > target:
                    end -= 1
                else:
                    return about
                if abs(result - target) > abs(about - target):
                    result = about
        return result
