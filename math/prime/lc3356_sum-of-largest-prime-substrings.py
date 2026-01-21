"""
3556.最大质数子字符串之和

给定一个字符串 s，找出可以由其 子字符串 组成的 3个最大的不同质数 的和。
返回这些质数的 总和 ，如果少于 3 个不同的质数，则返回 所有 不同质数的和。
质数是大于 1 且只有两个因数的自然数：1和它本身。
子字符串 是字符串中的一个连续字符序列。 
注意：每个质数即使出现在 多个 子字符串中，也只能计算 一次 。此外，将子字符串转换为整数时，忽略任何前导零。

date: 2025-11-18

"""
from math import isqrt
class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def is_prime(x):
            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False
            return x >= 2  # 1 不是质数
        prime = set()
        for i in range(len(s)):
            ans = 0
            for ch in s[i:]:
                ans = ans * 10 + int(ch)
                if is_prime(ans):
                    prime.add(ans)
        return sum(sorted(prime)[-3:])
if __name__ == "__main__":
    sol = Solution()
    s = "12234"
    print(sol.sumOfLargestPrimes(s))  # 11
    