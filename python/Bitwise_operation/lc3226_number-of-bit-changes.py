"""
3226.使两个整数相等的位更改次数

给你两个正整数 n 和 k。
你可以选择 n 的 二进制表示 中任意一个值为 1 的位，并将其改为 0。
返回使得 n 等于 k 所需要的更改次数。如果无法实现，返回 -1。

date: 2025-11-10
"""

class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n & k != k:
            return -1
        else:
            # return (n ^ k).bit_count()  # Python 3.10+
            return bin(n ^ k).count('1')
        
if __name__ == "__main__":
    sol = Solution()
    n = 13
    k = 4
    print(sol.minChanges(n, k))  # 2