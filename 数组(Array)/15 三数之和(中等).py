# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i +1
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] + nums[i] > 0:
                    end -=1
                elif nums[start] + nums[end] + nums[i] < 0:
                    start +=1
                else:
                    result += [nums[start],nums[end],nums[i]]
                    while start < end and nums[start] == nums[start+1]:
                        start +=1
                    while end > start and nums[end] == nums[end-1]:
                        end -=1
                    start +=1
                    end -=1
        return result
