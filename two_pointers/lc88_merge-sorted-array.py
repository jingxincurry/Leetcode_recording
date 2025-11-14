"""
88.合并两个有序数组

给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

data:2025-11-14

可以用倒序双指针来做
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans = [] 
        sp1, sp2 = 0, 0
        while sp1 < m and sp2 < n:
            if nums1[sp1] < nums2[sp2]:
                ans.append(nums1[sp1])
                sp1 += 1
            else:
                ans.append(nums2[sp2])
                sp2 += 1
        while sp1 < m:
            ans.append(nums1[sp1])
            sp1 += 1
        while sp2 < n:
            ans.append(nums2[sp2])
            sp2 += 1

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(sol.merge(nums1, m, nums2, n))  # [1,2,2,3,5,6]