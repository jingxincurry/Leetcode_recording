"""
344.反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

Date: 2025-11-5
"""
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 写法一：
        # s.reverse()
        
        # 写法二：
        left = 0
        right = len(s) - 1
        while left < right:
            s[left],s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

if __name__ == "__main__":
    sol = Solution()
    s1 = ["h","e","l","l","o"]
    print(sol.reverseString(s1))