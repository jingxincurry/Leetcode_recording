"""
704.二分查找
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1 。

data:2025-11-7
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
    
    def search(self, nums: List[int], target: int) -> int:
        ans = self.lower_bound(nums, target)
        if ans == len(nums) or nums[ans] != target:
            return -1
        return ans
if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    print(sol.search(nums, target))  # 4