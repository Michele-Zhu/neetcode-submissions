from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "[", "{"]:
                # opening parenthesis
                stack.append(char)
            else:
                # pop stack and compare
                # valid conditions is:
                # 1. stack non empty
                # 2. the last inserted element matches the closing bracked [")", "]", "}"]

                if (len(stack) != 0 and stack[-1] + char in {"()", "[]", "{}"}):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0