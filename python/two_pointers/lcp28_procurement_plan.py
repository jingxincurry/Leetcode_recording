"""
LCP 28. 采购方案

小力将 N 个零件的报价存于数组 nums。小力预算为 target，假定小力仅购买两个零件，要求购买零件的花费不超过预算，请问他有多少种采购方案。
注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1

data: 2025-11-6
"""
from typing import List

class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0
        while left < right:
            s = nums[left] + nums[right]
            if s <= target:
                ans += right - left
                left += 1
            else:
                right -= 1
        if ans <= 1000000007:
            return ans
        else:
            return ans % 1000000007
if __name__ == "__main__":
    sol = Solution()
    nums1 = [2,5,3,5]
    target1 = 6
    print(sol.purchasePlans(nums1, target1))  # 1

    nums2 = [2,2,1,9]
    target2 = 10
    print(sol.purchasePlans(nums2, target2))  # 4

    nums3 = [999999998,999999997,999999999]
    target3 = 1999999996
    print(sol.purchasePlans(nums3, target3))  # 2