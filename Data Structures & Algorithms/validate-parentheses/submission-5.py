class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        stack = []
        open_parentheses = ["(", "[", "{"]

        for char in s:
            if char in open_parentheses:
                stack.append(char)
            else:
                print(stack)
                if len(stack) == 0:
                    return False
                last_element = stack.pop()
                if last_element == "(" and char == ")":
                    continue
                elif last_element == "[" and char == "]":
                    continue
                elif last_element == "{" and char == "}":
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False