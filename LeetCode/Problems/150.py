# NeetCode - Stack
# 150. Evaluate Reverse Polish Notation
# Difficulty : Medium
# Algorithm : Stack
# Runtime : 75 ms (95.72%), Memory : 16.6 MB (90.60%)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = set(["+", "-", "*", "/"])
        stack = []

        for token in tokens:
            if token in oper:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(token))

        return stack[0]
