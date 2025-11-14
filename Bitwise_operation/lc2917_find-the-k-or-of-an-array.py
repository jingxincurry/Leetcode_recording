"""
2917.找出数组中的K-or值

给你一个整数数组 nums 和一个整数 k 。让我们通过扩展标准的按位或来介绍 K-or 操作。在 K-or 操作中，如果在 nums 中，至少存在 k 个元素的第 i 位值为 1 ，那么 K-or 中的第 i 位的值是 1 。
返回 nums 的 K-or 值。

date:2025-11-13

有点吃力
"""
from typing import List
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        max_len = max(nums).bit_length()
        for i in range(max_len):
            cnt = 0
            mask = 1 << i
            for x in nums:
                if x & (1 << i):
                    cnt += 1
            if cnt >= k:
                ans |= mask
        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [7,12,9,8,9,15]
    k = 4
    print(sol.findKOr(nums, k))  # 9