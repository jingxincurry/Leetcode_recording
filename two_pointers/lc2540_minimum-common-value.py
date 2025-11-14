"""
2540.最小公共值

给你两个整数数组 nums1 和 nums2 ，它们已经按非降序排序，请你返回两个数组的 最小公共整数 。如果两个数组 nums1 和 nums2 没有公共整数，请你返回 -1 。
如果一个整数在两个数组中都 至少出现一次 ，那么这个整数是数组 nums1 和 nums2 公共 的。

data:2025-11-14
"""
from typing import List
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(set(nums1) & set(nums2), default = -1)
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2,3]
    nums2 = [2,4]
    print(sol.getCommon(nums1, nums2))  # 2