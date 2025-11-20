"""
1577.数的平方等于两数乘积的方法数

给你两个整数数组 nums1 和 nums2 ，请你返回根据以下规则形成的三元组的数目（类型 1 和类型 2 ）：

类型 1：三元组 (i, j, k) ，如果 nums1[i]2 == nums2[j] * nums2[k] 其中 0 <= i < nums1.length 且 0 <= j < k < nums2.length
类型 2：三元组 (i, j, k) ，如果 nums2[i]2 == nums1[j] * nums1[k] 其中 0 <= i < nums2.length 且 0 <= j < k < nums1.length

date:2025-11-20
"""
from typing import List
from collections import defaultdict
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        for i, x in enumerate(nums1):
            cnt1 = defaultdict(int)
            xx = x * x
            for j, y in enumerate(nums2):
                if xx % y == 0:
                    z = xx // y
                    ans += cnt1[z]
                cnt1[y] += 1
        
        for i, x in enumerate(nums2):
            cnt2 = defaultdict(int)
            xx = x * x
            for j, y in enumerate(nums1):
                if xx % y == 0:
                    z = xx // y
                    ans += cnt2[z]
                cnt2[y] += 1
        return ans
if __name__ == "__main__":
    solu = Solution()
    nums1 = [7,4]
    nums2 = [5,2,8,9]
    print(solu.numTriplets(nums1, nums2))  # 输出1