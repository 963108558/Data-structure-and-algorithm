# 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        if len(nums) < 3:
            return 0
        for i in range(2,len(nums)):
            start = 0
            end = i - 1
            while start < end:
                if nums[start] + nums[end] > nums[i]:
                    count += end - start
                    end -=1
                else:
                    start +=1
            return count