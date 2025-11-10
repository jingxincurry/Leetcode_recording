"""
1869. 哪种连续子字符串更长

给你一个二进制字符串 s 。如果字符串中由 1 组成的 最长 连续子字符串 严格长于 由 0 组成的 最长 连续子字符串，返回 true ；否则，返回 false 。
例如，s = "110100010" 中，由 1 组成的最长连续子字符串的长度是 2 ，由 0 组成的最长连续子字符串的长度是 3 。
注意，如果字符串中不存在 0 ，此时认为由 0 组成的最长连续子字符串的长度是 0 。字符串中不存在 1 的情况也适用此规则。

date: 2025-11-10

"""

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        cnt0, cnt1 = 0, 0
        max_0,max_1 = 0, 0
        for ch in s:
            if ch == '1':
                cnt1 += 1
                cnt0 = 0
            else:
                cnt0 += 1
                cnt1 = 0
            max_0 = max(max_0, cnt0)
            max_1 = max(max_1, cnt1)
        return max_1 > max_0
    
if __name__ == "__main__":
    sol = Solution()
    s = "1101"
    print(sol.checkZeroOnes(s))  # True