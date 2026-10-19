class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits is None or digits =="":
            return []
        combinations = {
            "2" : ["a","b","c"],
            "3" : [ "d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        result = []

        def backtrack(i, curr):
            if len(curr) == len(digits):
                result.append(curr)
                return
            
            for char in combinations[digits[i]]:
                backtrack(i+1, curr + char)
        backtrack(0, "")
        return result