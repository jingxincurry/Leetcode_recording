"""
1342.将数字变成0的操作次数

给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。

data:2025-11-13
"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num:
            if num % 2 == 0:
                num //= 2
                ans += 1
            else:
                num -= 1
                ans += 1
        return ans
    # 方法2 位运算
        # return num.bit_length() + num.bit_count() - 1 if num else 0
if __name__ == "__main__":
    sol = Solution()
    num = 14
    print(sol.numberOfSteps(num))  # 6