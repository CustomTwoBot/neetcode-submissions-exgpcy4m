class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        resultNum = 0
        for i in tokens:
            stack.append(i)
            if i == "+":
                resultNum = int(stack[-3]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append(resultNum)
            elif i == "-":
                resultNum = int(stack[-3]) - int(stack[-2])
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append(resultNum)
            elif i == "*":
                resultNum = int(stack[-3]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append(resultNum)
            elif i == "/":
                resultNum = int(stack[-3]) / int(stack[-2])
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append(resultNum)
        return int(stack[0])