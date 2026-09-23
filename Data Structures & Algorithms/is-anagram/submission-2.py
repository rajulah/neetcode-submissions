class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        s_hashmap = {}
        r_hashmap = {}
        for char in s:
            s_hashmap[char] = s_hashmap.get(char, 0) + 1
        for char in t:
            if char not in s_hashmap:
                return False
            s_hashmap[char] = s_hashmap[char] - 1
            if s_hashmap[char] == 0:
                del s_hashmap[char]
        if len(s_hashmap) > 0:
            return False
        return True
        