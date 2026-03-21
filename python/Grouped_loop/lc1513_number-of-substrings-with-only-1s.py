"""
1513.仅含1的子串数

给你一个二进制字符串 s（仅由 '0' 和 '1' 组成的字符串）。
返回所有字符都为 1 的子字符串的数目。
由于答案可能很大，请你将它对 10^9 + 7 取模后返回。

data:2025-11-16
"""

class Solution:
    def numSub(self, s: str) -> int:
        ans = int(s[0])
        left = 0
        for i in range(1, len(s)):
            if s[i] == '1' and s[i - 1] == '0':
                ans += 1
                left = i
            if s[i] == s[i - 1] and s[i] == '1':
                ans += i - left + 1
        return ans % (10**9 + 7)
    # 答案方法更简洁
    def numSub2(self, s: str) -> int:
        MOD = 1_000_000_007
        ans = 0
        last0 = -1
        for i, ch in enumerate(s):
            if ch == '0':
                last0 = i  # 记录上个 0 的位置
            else:
                ans += i - last0  # 右端点为 i 的全 1 子串个数
        return ans % MOD

if __name__ == "__main__":
    sol = Solution()
    s = "0110111"
    print(sol.numSub(s))  # 9