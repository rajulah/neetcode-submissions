from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif len(stack) < 1:
                return False
            elif char == ")":
                if "(" != stack.pop():
                    return False
            elif char == "}":
                if "{" != stack.pop():
                    return False
            elif char == "]":
                if "[" != stack.pop():
                    return False
            else:
                continue
        if len(stack) > 0:
            return False
        return True
