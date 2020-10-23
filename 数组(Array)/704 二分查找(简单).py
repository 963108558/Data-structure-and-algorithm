# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target
# ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            result = (start + end) // 2
            if nums[result] > target:
                end = result - 1
            elif nums[result] < target:
                start = result + 1
            else:
                return result
        return -1