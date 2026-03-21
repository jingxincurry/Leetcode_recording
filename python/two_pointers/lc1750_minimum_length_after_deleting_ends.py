"""
1750. Minimum Length of String After Deleting Similar Ends

给你一个只包含字符 'a'，'b' 和 'c' 的字符串 s ，你可以执行下面这个操作（5 个步骤）任意次：
选择字符串 s 一个 非空 的前缀，这个前缀的所有字符都相同。
选择字符串 s 一个 非空 的后缀，这个后缀的所有字符都相同。
前缀和后缀在字符串中任意位置都不能有交集。
前缀和后缀包含的所有字符都要相同。
同时删除前缀和后缀。
请你返回对字符串 s 执行上面操作任意次以后（可能 0 次），能得到的 最短长度 。

Date: 2025-11-5

知识点：
left <= right  出错
"""
class Solution:
    def minimumLength(self, s: str) -> int:
        left,right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            ch = s[left]
            while left <= right and s[left] == ch:
                left += 1
            while left <= right and s[right] == ch:
                right -= 1

        return right - left + 1

if __name__ == "__main__":
    sol = Solution()
    s1 = "ca"
    print(sol.minimumLength(s1))  # 2

    s2 = "cabaabac"
    print(sol.minimumLength(s2))  # 0

    s3 = "aabccabba"
    print(sol.minimumLength(s3))  # 3