"""
1365.有多少小于当前数字的数字

给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
以数组形式返回答案。

date: 2025-11-15
"""
from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for left in range(len(nums)):
            cnt = 0
            for right in range(len(nums)):
                if right != left and nums[right] < nums[left]:
                    cnt += 1
            ans.append(cnt)
        return ans
if __name__ == "__main__":
    sol = Solution()
    nums = [8,1,2,2,3]
    print(sol.smallerNumbersThanCurrent(nums))  # [4,0,1,1,3]
        