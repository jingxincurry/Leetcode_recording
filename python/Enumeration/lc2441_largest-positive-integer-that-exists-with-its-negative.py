"""
2441.与对应负数同时存在的最大正整数

给你一个整数数组 nums ，请你找出并返回满足  -x 也存在于 nums 中的 最大正整数 x 。
如果不存在这样的正整数，返回 -1 。

"""
from math import inf
from typing import List
class Solution:
    def findMaxK(self, nums:List[int]) -> int:
        idx = {}
        max_num = -1
        for i, x in enumerate(nums):
            if -x in idx:
                max_num = max(max_num, abs(x))
                 
            idx[x] = i
        return max_num

if __name__ == "__main__":
    sol = Solution()
    nums = [-30,34,1,32,26,-9,-30,22,-49,29,48,47,38,4,43,12,-1,-8,11,-37,32,40,9,15,-34,-34,-16,-5,26,-44,-36,-13,-16,10,39,-17,-22,17,-16]
    print(sol.findMaxK(nums))  # 3
