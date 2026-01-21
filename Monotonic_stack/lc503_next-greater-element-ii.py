"""
503.下一个更大元素 II

给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。
数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。

data: 2025-11-21
"""
from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n * 2
        st = []
        for i in range(2* n - 1, -1, -1):
            x = nums[i % n]
            while st and x >= st[-1]:
                st.pop()
            if st:
                ans[i] = st[-1]
            st.append(x)
        return ans[:n]
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,1]
    print(sol.nextGreaterElements(nums))  # [2,-1,2]