# 给定一个含有 n 个正整数的数组和一个正整数s ，
# 找出该数组中满足其和 ≥ s 的长度最小的连续 子数组，
# 并返回其长度。如果不存在符合条件的子数组，返回 0。

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left,sums,res = 0,0,float('inf')
        for right in range(len(nums)):
            sums += nums[right]
            while sums >= s:
                if right - left + 1 < res:
                    res = right - left + 1
                sums -= nums[left]
                left +=1
        return 0 if res == float('inf') else res