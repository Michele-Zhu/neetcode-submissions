class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_parentheses = ["(", "[", "{"]

        for char in s:
            if char in open_parentheses:
                stack.append(char)
            else:
                if (len(stack) != 0 and stack[-1] + char in {"()", "[]", "{}"}):
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False