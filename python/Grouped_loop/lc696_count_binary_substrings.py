"""
696.计数二进制子串

给定一个字符串 s，统计并返回具有相同数量 0 和 1 的非空（连续）子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是成组连续的。
重复出现（不同位置）的子串也要统计它们出现的次数。

data:2025-11-10
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group = []
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                group.append(cnt)
                cnt = 1
        group.append(cnt)  # 记得加上最后一组
        ans = 0
        for i in range(1, len(group)):
            ans += min(group[i], group[i - 1])
        return ans
    
if __name__ == "__main__":
    sol = Solution()
    s = "00110011"
    print(sol.countBinarySubstrings(s))  # 6