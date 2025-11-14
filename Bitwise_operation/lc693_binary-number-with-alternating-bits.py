"""
693.交替位二进制数

给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。
data:2025-11-13

"""
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        pre = 2
        while n:
            cur = n % 2
            if cur == pre:
                return False
            pre = cur
            n //= 2
        return True
if __name__ == "__main__":
    sol = Solution()
    n = 5
    print(sol.hasAlternatingBits(n))  # True