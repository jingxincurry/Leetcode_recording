"""
150.逆波兰表达式求值

根据 逆波兰表示法，求表达式的值。
给你一个字符串数组 tokens ，表示一个根据 逆波兰表示法 表示的算术表达式。
请你计算该表达式。返回一个表示表达式值的整数。

注意：
有效的算符为 '+'、'-'、'*' 和 '/' 。
每个操作数（运算对象）都可以是一个整数或者另一个表达式。
两个整数之间的除法总是 向零截断 。
表达式中不含除零运算。
输入是一个根据逆波兰表示法表示的算术表达式。
答案及所有中间计算结果可以用 32 位 整数表示。

date: 2025-11-23
"""
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token not in "+-*/":
                st.append(int(token))
                continue
                
            b = st.pop()
            a = st.pop()

            if token == "+":
                st.append(a + b)
            elif token == "-":
                st.append(a - b)
            elif token == "*":
                st.append(a * b)
            else:
                st.append(int(a / b))
        return st[-1]
if __name__ == "__main__":
    sol = Solution()
    tokens = ["2","1","+","3","*"]
    print(sol.evalRPN(tokens))  # 9
    tokens = ["4","13","5","/","+"]
    print(sol.evalRPN(tokens))  # 6
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(sol.evalRPN(tokens))  # 22
