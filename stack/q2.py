"""
Question:
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []

        # tokensをあたまから見ていく
        # 四則演算子であればstackから2つPopして演算してstackに戻す。
        # 数字であればintに変換してstackに入れる。
        for i in range(n):
            if tokens[i] == "+":
                b = stack.pop()
                a = stack.pop()
                ans = a + b
                stack.append(ans)
            elif tokens[i] == "-":
                b = stack.pop()
                a = stack.pop()
                ans = a - b
                stack.append(ans)
            elif tokens[i] == "*":
                b = stack.pop()
                a = stack.pop()
                print(f"a = {a}, b = {b}")
                ans = a * b
                stack.append(ans)
            elif tokens[i] == "/":
                b = stack.pop()
                a = stack.pop()
                print(f"a = {a}, b = {b}")
                ans = int(a / b)
                stack.append(ans)
            else:
                stack.append(int(tokens[i]))

        return stack[0]
