"""
2958.最多K个重复元素的最长子数组

给你一个整数数组 nums 和一个整数 k 。
一个元素 x 在数组中的 频率 指的是它在数组中的出现次数。
如果一个数组中所有元素的频率都 小于等于 k ，那么我们称这个数组是 好 数组。
请你返回 nums 中 最长好 子数组的长度。
子数组 指的是一个数组中一段连续非空的元素序列。

"""
from typing import List
from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        left, ans = 0, 0
        for right, x in enumerate(nums):
            cnt[x] += 1
            while cnt[x] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
    
if __name__ == "__main__":
    solu = Solution()
    nums = [1,2,3,1,2,3,1,2]
    k = 2
    print(solu.maxSubarrayLength(nums, k))  # 输出6