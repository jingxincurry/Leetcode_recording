"""
342.4的幂

给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x

data:2025-11-13

"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1
if __name__ == "__main__":
    sol = Solution()
    n = 16
    print(sol.isPowerOfFour(n))  # True