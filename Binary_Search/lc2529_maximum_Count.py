"""
2529.正整数和负整数的最大计数

给你一个按 非递减顺序 排列的数组 nums ，返回正整数数目和负整数数目中的最大值。
换句话讲，如果 nums 中正整数的数目是 pos ，而负整数的数目是 neg ，返回 pos 和 neg二者中的最大值。
注意：0 既不是正整数也不是负整数。

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

    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        ans1 = self.lower_bound(nums, 0)
        ans2 = n - self.lower_bound(nums, 1)
        return max(ans1, ans2)
    
    # 方法二：遍历
        # ans1, ans2 = 0, 0
        # for i, x in enumerate(nums):
        #     if x < 0:
        #         ans1 += 1
        #     elif x > 0:
        #         ans2 += 1
        # return max(ans1, ans2)
if __name__ == "__main__":
    sol = Solution()
    nums = [-2,-1,-1,1,2,3]
    print(sol.maximumCount(nums))  # 3