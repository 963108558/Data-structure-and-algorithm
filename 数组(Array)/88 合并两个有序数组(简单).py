# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 说明：
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m -1
        j = n - 1
        k = m + n -1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -=1
            else:
                nums1[k] = nums2[j]
                j -=1
            k -=1
        if j >= 0:
            while j >=0:
                nums1[k] = nums2[j]
                j -=1
                k -=1
        return nums1
