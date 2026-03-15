"""
Question:
You are given an integer array target and an integer n.

You have an empty stack with the two following operations:

    "Push": pushes an integer to the top of the stack.
    "Pop": removes the integer on the top of the stack.

You also have a stream of the integers in the range [1, n].

Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target. You should follow the following rules:

    If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.
    If the stack is not empty, pop the integer at the top of the stack.
    If, at any moment, the elements in the stack (from the bottom to the top) are equal to target, do not read new integers from the stream and do not do more operations on the stack.

Return the stack operations needed to build target following the mentioned rules. If there are multiple valid answers, return any of them.
"""


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        operation = []
        stream = list(range(1, n + 1))

        i = 0
        while i < len(target):
            # stackにstreamの一番最初の数字をPush
            stack.append(stream[0])
            operation.append("Push")

            # Pushした数字はPop
            stream.pop(0)

            # targetのi番目がstackの最後と一致していればPopせず先に進む
            if target[i] == stack[len(stack) - 1]:
                i += 1
            # 一致していなければPop
            else:
                stack.pop()
                operation.append("Pop")

        return operation
