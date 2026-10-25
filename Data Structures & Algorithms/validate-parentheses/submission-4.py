class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }
        if s == "":
            return True
        stack = []
        for char in s:
            if char not in valid and not char.isalnum():
                stack.append(char)
            else:
                if stack:
                    pop = stack.pop()
                    if pop != valid[char]:
                        return False
                else:
                    return False
        return True if stack == [] else False