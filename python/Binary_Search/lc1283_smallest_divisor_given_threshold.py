"""
1283.使结果不超过阈值的最小除数

给你一个整数数组 nums 和一个正整数 threshold  ，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。
请你找出能够使上述结果小于等于阈值 threshold 的除数中 最小 的那个。
每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。
题目保证一定有解。

date: 2025-11-7

"""
from typing import List
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            s = 0
            for x in nums:
                s += math.ceil(x / mid)
            if s <= threshold:
                ans = mid
                right = mid - 1           
            else:
                left = mid + 1
        return ans
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,5,9]
    threshold = 6
    print(sol.smallestDivisor(nums, threshold))  # 5