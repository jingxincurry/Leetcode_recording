""""
633.平方数之和

给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。

Date: 2025-11-5

"""
from math import isqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, isqrt(c)
        s = 0
        while a <= b:
            s = a * a + b * b
            if s == c:
                return True
            if s < c:
                a += 1
            else:
                b -= 1
        return False
    

if __name__ == "__main__":
    sol = Solution()
    c1 = 5
    print(sol.judgeSquareSum(c1))  # True

    c2 = 3
    print(sol.judgeSquareSum(c2))  # False