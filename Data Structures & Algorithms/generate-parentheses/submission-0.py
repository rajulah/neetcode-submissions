class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(open_count, close_count, curr_comb):
            if open_count == n and close_count == n:
                result.append(curr_comb[:])
                return
            if open_count < n:
                backtrack(open_count+1, close_count, curr_comb + "(")
            if close_count < open_count and close_count < n:
                backtrack(open_count, close_count + 1, curr_comb + ")")
        backtrack(0,0,"")
        return result