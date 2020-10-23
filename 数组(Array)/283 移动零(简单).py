# 思路:快慢指针

# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序

# 方案1
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#     for i in nums:
#         if i == 0:
#             nums.remove(0)
#             nums.append(0)


# # 方案2
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#     slow = 0
#     fast = 0
#     while fast < len(nums):
#         if nums[fast] == 0:
#             fast +=1
#         else:
#             nums[slow] = nums[fast]
#             fast +=1
#             slow +=1
#     for i in range(slow,len(nums)):
#         nums[i] = 0

# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]