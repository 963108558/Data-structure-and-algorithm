# 思路:快慢指针

# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


# 方案1(快慢指针)
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         slow = 0
#         fast = 1
#         while fast < len(nums):
#             if nums[fast] == nums[slow]:
#                 fast += 1
#             else:
#                 slow += 1
#                 nums[slow] = nums[fast]
#                 fast += 1
#         return slow + 1

# 方案2(运用集合类)
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         longer = len(set(nums))
#         counter = 0
#         while counter < longer-1:
#             if nums[counter] == nums[counter+1]:
#                 temp = nums[counter]
#                 nums[counter+1:len(nums)-1] = nums[counter+2:]
#                 nums[-1] = temp
#             else:
#                 counter +=1
#         return counter+1





# 注:数组有两种情况:
# (1)nums = [0,0,1,1,1,2,2,3,3,4]
# (2)nums = [0,1,1,1,2,2,3,3,4]
