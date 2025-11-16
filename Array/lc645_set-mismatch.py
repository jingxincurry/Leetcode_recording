"""
645.错误的集合

集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。
给定一个数组 nums 代表了集合 S 发生错误后的结果。
请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

date: 2025-11-15
"""
from typing import List
from collections import defaultdict
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = defaultdict(int)
        s = set(nums)
        c = 0
        d = 0
        for i,x in enumerate(nums):
            cnt[x] += 1
            if cnt[x] > 1:
                c = x
            if (i + 1) not in s:
                d = i + 1
        return [c, d]
    # 写法二
    def findErrorNums2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set(nums)
        dup = sum(nums) - sum(s)
        miss = (n*(n+1))//2 - sum(s)
        return [dup, miss]
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,2,4]
    print(sol.findErrorNums(nums))  # [2,3]
            