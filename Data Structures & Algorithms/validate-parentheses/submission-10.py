class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if (len(stack) != 0 and stack[-1] + char in {"()", "[]", "{}"}):
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
            
        