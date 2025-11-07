"""
2300.咒语和药水的成功对数

给你两个正整数数组 spells 和 potions ，长度分别为 n 和 m ，其中 spells[i] 表示第 i 个咒语的能量强度，potions[j] 表示第 j 瓶药水的能量强度。
同时给你一个整数 success 。一个咒语和药水的能量强度 相乘 如果 大于等于 success ，那么它们视为一对 成功 的组合。
请你返回一个长度为 n 的整数数组 pairs，其中 pairs[i] 是能跟第 i 个咒语成功组合的 药水 数目。

date: 2025-11-6
"""
from typing import List
class Solution:
    def lower_bound(self, nums:List[int], target: int) ->int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m, n = len(spells), len(potions)
        ans = []
        for spell in spells:
            x = success / spell
            idx = self.lower_bound(potions, x)
            ans.append(n - idx)
        return ans
if __name__ == "__main__":
    sol = Solution()
    spells = [5,1,3]
    potions = [1,2,3,4,5]
    success = 7
    print(sol.successfulPairs(spells, potions, success))  # [4,0,3]