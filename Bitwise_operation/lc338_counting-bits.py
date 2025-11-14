"""
338.比特位计数

给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。

data:2025-11-13
"""
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ans.append(i.bit_count())
        return ans
if __name__ == "__main__":
    sol = Solution()
    n = 5
    print(sol.countBits(n))  # [0,1,1,2,1,2]