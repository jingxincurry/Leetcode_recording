"""
35.搜索插入位置

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。

"""
from typing import List
class Solution:
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1 
            else:
                right = mid - 1
        return left

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.lower_bound(nums, target)

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,5,6]
    target = 4
    print(sol.searchInsert(nums, target))  # 2