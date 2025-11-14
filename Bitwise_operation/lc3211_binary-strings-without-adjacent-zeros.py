"""
3211.生成不含相邻零的二进制字符串

给你一个正整数 n。
如果一个二进制字符串 x 的所有长度为 2 的子字符串中包含 至少 一个 "1"，则称 x 是一个 有效 字符串。
返回所有长度为 n 的 有效 字符串，可以以任意顺序排列。

data:2025-11-14
"""
from typing import List
class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        mask = (1 << n) - 1
        for x in range(1<<n):
            if (x >> 1) & x == 0:
                ans.append(f"{x ^ mask:0{n}b}")
        return ans
if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.validStrings(n))  # ['111', '110', '101', '011', '010']