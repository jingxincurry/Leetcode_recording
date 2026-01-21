"""
448.找到所有数组中消失的数字
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

date: 2025-11-23

"""
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            x = (num - 1) % n
            nums[x] += n
        
        ret = [i + 1 for i, num in enumerate(nums) if num <= n]
        return ret
    
    def findDisappearedNumbers_set(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set(nums)
        ret = [i for i in range(1, n + 1) if i not in num_set]
        return ret
    
    def findDisappearedNumbers3(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 将所有正数作为数组下标，置对应数组值为负值。那么，仍为正数的位置即为（未出现过）消失的数字。
        # 举个例子：
        # 原始数组：[4,3,2,7,8,2,3,1]
        # 重置后为：[-4,-3,-2,-7,8,2,-3,-1]
        # 结论：[8,2] 分别对应的index为[5,6]（消失的数字）

        for num in nums:
            index = abs(num) - 1
            # 始终保持nums[index]为负数
            nums[index] = -abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]


if __name__ == "__main__":
    sol = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(sol.findDisappearedNumbers(nums))  # [5,6]