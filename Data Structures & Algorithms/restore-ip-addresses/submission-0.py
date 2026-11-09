class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        result = []
        curr_parts = []

        def backtrack(start_index):
            if len(curr_parts) == 4:
                if start_index == len(s):
                    result.append(".".join(curr_parts))
                return
            
            if len(curr_parts) > 4:
                return
            
            for i in range(1,4):
                end_index = start_index + i
                if end_index > len(s):
                    break
                part = s[start_index: end_index]
                if len(part)>1 and part[0] == "0":
                    continue
                if int(part) > 255:
                    continue
                curr_parts.append(part)
                backtrack(end_index)
                curr_parts.pop()


        backtrack(0)
        return result