"""
2595.奇偶位数

给你一个 正 整数 n 。
用 even 表示在 n 的二进制形式（下标从 0 开始）中值为 1 的偶数下标的个数。
用 odd 表示在 n 的二进制形式（下标从 0 开始）中值为 1 的奇数下标的个数。
请注意，在数字的二进制表示中，位下标的顺序 从右到左。
返回整数数组 answer ，其中 answer = [even, odd] 。

date:2025-11-13
"""
from typing import List
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]
        i = 0
        while n:
            ans[i] += n & 1
            n >>= 1
            i ^= 1
        return ans
if __name__ == "__main__":
    sol = Solution()
    n = 50
    print(sol.evenOddBit(n))  # [1, 2]